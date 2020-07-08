import logging

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from mainapp.models import User, Study
from mainapp.utils import lib
from mainapp.utils.elasticsearch_service import MonitorEvents, ElasticsearchService
from mainapp.utils.response_handler import BadRequestErrorResponse

logger = logging.getLogger(__name__)


class Monitoring(GenericAPIView):
    def post(self, request):
        event_type = request.data["event_type"]
        if not event_type:
            return BadRequestErrorResponse("Event Type not specified. Cannot log event")
        if event_type == MonitorEvents.EVENT_REQUEST_NOTEBOOK.value:
            user = User.objects.get(id=request.data.get("data")["user"])
            study = Study.objects.get(id=request.data.get("data")["study"])
            event_id = request.data.get("data")["event_id"]
            if not user or not study:
                logger.exception(
                    "Data for event was not specified correctly. Can not log event"
                )
                return

            ElasticsearchService.write_monitoring_event(
                event_type=MonitorEvents.EVENT_REQUEST_NOTEBOOK,
                user_ip=lib.get_client_ip(request),
                event_id=event_id,
                study_id=study.id,
                study_name=study.name,
                user_name=user.display_name,
                execution_token=study.execution.token if study.execution else "",
                environment_name=study.organization.name,
                user_organization=user.organization.name,
            )

            logger.info(
                f"User {user.display_name} from org {user.organization.name} "
                f"has requested the notebook for Study {study.name}:{study.id} "
                f"as jupyter-{study.execution.token if study.execution else ' '}"
            )
        elif event_type == MonitorEvents.EVENT_NOTEBOOK_READY.value:
            user = User.objects.get(id=request.data.get("data")["user"])
            study = Study.objects.get(id=request.data.get("data")["study"])
            load_time = request.data.get("data")["load_time"]
            event_id = request.data.get("data")["event_id"]
            if not user or not study or not load_time:
                logger.exception(
                    "Data for event was not specified correctly. Can not log event"
                )
                return

            ElasticsearchService.write_monitoring_event(
                event_type=MonitorEvents.EVENT_NOTEBOOK_READY,
                event_id=event_id,
                user_ip=lib.get_client_ip(request),
                study_id=study.id,
                study_name=study.name,
                execution_token=study.execution.token if study.execution else "",
                user_name=user.display_name,
                environment_name=study.organization.name,
                user_organization=user.organization.name,
                additional_data={"load_time": load_time},
            )
            logger.info(
                f"Notebook jupyter-{study.execution.token if study.execution else ' '} "
                f"for Study {study.name}:{study.id} "
                f"is ready for User {user.display_name} "
                f"from org {user.organization.name} "
                f"and took {load_time} ms to load"
            )
        elif event_type == MonitorEvents.EVENT_NOTEBOOK_LOAD_FAIL.value:
            user = User.objects.get(id=request.data.get("data")["user"])
            study = Study.objects.get(id=request.data.get("data")["study"])
            if not user or not study:
                logger.exception(
                    "Data for event was not specified correctly. Can not log event"
                )
                return

            ElasticsearchService.write_monitoring_event(
                event_type=MonitorEvents.EVENT_NOTEBOOK_LOAD_FAIL,
                study_id=study.id,
                study_name=study.name,
                execution_token=study.execution.token if study.execution else "",
                user_name=user.display_name,
                user_ip=lib.get_client_ip(request),
                environment_name=study.organization.name,
                user_organization=user.organization.name,
            )
            logger.info(
                f"Notebook jupyter-{study.execution.token if study.execution else ' '} "
                f"for Study {study.name}:{study.id} "
                f"failed to load for User {user.display_name} "
                f"from org {user.organization.name} "
            )
        elif event_type == MonitorEvents.EVENT_USER_LOGIN.value:
            user = User.objects.get(id=request.data.get("data")["user"])
            if not user:
                logger.exception(
                    "Data for event was not specified correctly. Can not log event"
                )
                return
            ElasticsearchService.write_monitoring_event(
                event_type=MonitorEvents.EVENT_USER_LOGIN,
                user_ip=lib.get_client_ip(request),
                user_name=user.display_name,
                user_organization=user.organization.name,
            )
            logger.info(
                f"User {user.display_name} from org {user.organization.name} has logged in"
            )

        return Response()
