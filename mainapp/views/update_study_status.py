import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.exceptions import InvalidEc2Status
from mainapp.models import Study, Execution, User
from mainapp.utils.monitoring import handle_event
from mainapp.utils.response_handler import BadRequestErrorResponse
from mainapp.utils.status_monitoring_event_map import status_monitoring_event_map
from mainapp.utils.study_vm_service import update_study_state

logger = logging.getLogger(__name__)


class UpdateStudyStatus(APIView):
    """View to allow study status updates externally"""

    def post(self, request):
        try:
            study = Study.objects.get(
                execution=Execution.objects.get(
                    execution_user=User.objects.get(email=request.user.email)
                )
            )

            status = request.data.get("status")

            monitor_event = status_monitoring_event_map.get(status, None)
            if monitor_event:
                handle_event(monitor_event, {"study": study, "view_request": request})

            update_study_state(study, status)
            return Response(status=201)
        except InvalidEc2Status as ex:
            return BadRequestErrorResponse(message=str(ex))
