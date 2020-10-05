from dateutil import parser
from .actions import (
    DeidentificationAction,
    FreeTextReplacement,
    LowerResolution,
    Mask,
    Offset,
    Omission,
    RandomOffset,
    SaltedMask,
)
from .common import (
    Actions,
    DataTypes,
    DeidentificationError,
    GlueDataTypes,
    InvalidValueError,
    LynxDataTypeNames,
    InvalidDeidentificationArguments,
    MismatchingActionError,
    MismatchingTypesError,
    UnsupportedActionArgumentError,
    GROUP_OVER_AGE_VALUE,
)

from .lynx_data_types import (
    AccountNumber,
    Address,
    Age,
    BirthDate,
    Boolean,
    CertificateOrLicenseNumber,
    Date,
    DeviceIdentifier,
    Email,
    FaxNumber,
    FreeText,
    HealthPlanBeneficiaryNumber,
    IPAddress,
    MedialRecordNumber,
    Name,
    Number,
    PhoneNumber,
    SocialSecurityNumber,
    UniqueIdentifier,
    VehicleIdentifier,
    WebUniversalResourceLocator,
    ZipCode,
)

DATA_TYPE_CASTING = {
    DataTypes.STRING.value: str,
    DataTypes.INT.value: int,
    DataTypes.FLOAT.value: float,
    DataTypes.DATE.value: parser.parse,
    DataTypes.BOOLEAN.value: bool,
}

LYNX_DATA_TYPES = {
    LynxDataTypeNames.NAME.value: Name,
    LynxDataTypeNames.ADDRESS.value: Address,
    LynxDataTypeNames.ZIP_CODE.value: ZipCode,
    LynxDataTypeNames.DATE.value: Date,
    LynxDataTypeNames.AGE.value: Age,
    LynxDataTypeNames.PHONE_NUMBER.value: PhoneNumber,
    LynxDataTypeNames.FAX_NUMBER.value: FaxNumber,
    LynxDataTypeNames.EMAIL.value: Email,
    LynxDataTypeNames.SSN.value: SocialSecurityNumber,
    LynxDataTypeNames.MRD.value: MedialRecordNumber,
    LynxDataTypeNames.HPBN.value: HealthPlanBeneficiaryNumber,
    LynxDataTypeNames.ACCOUNT_NUMBER.value: AccountNumber,
    LynxDataTypeNames.CERTIFICATE_NUMBER.value: CertificateOrLicenseNumber,
    LynxDataTypeNames.IP_ADDRESS.value: IPAddress,
    LynxDataTypeNames.NUMBER.value: Number,
    LynxDataTypeNames.TEXT.value: FreeText,
    LynxDataTypeNames.BOOLEAN.value: Boolean,
    LynxDataTypeNames.VIDSN.value: VehicleIdentifier,
    LynxDataTypeNames.DIDSN.value: DeviceIdentifier,
    LynxDataTypeNames.WURL.value: WebUniversalResourceLocator,
    LynxDataTypeNames.UID.value: UniqueIdentifier,
    LynxDataTypeNames.BIRTH_DATE.value: BirthDate,
}

GLUE_LYNX_TYPE_MAPPING = {
    GlueDataTypes.BIGINT.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.BOOLEAN.value: LynxDataTypeNames.BOOLEAN.value,
    GlueDataTypes.CHAR.value: LynxDataTypeNames.TEXT.value,
    GlueDataTypes.DATE.value: LynxDataTypeNames.DATE.value,
    GlueDataTypes.DECIMAL.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.DOUBLE.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.FLOAT.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.INT.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.SMALLINT.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.STRING.value: LynxDataTypeNames.TEXT.value,
    GlueDataTypes.TIMESTAMP.value: LynxDataTypeNames.DATE.value,
    GlueDataTypes.TINYINT.value: LynxDataTypeNames.NUMBER.value,
    GlueDataTypes.VARCHAR.value: LynxDataTypeNames.TEXT.value,
}


GLUE_DATA_TYPE_MAPPING = {
    GlueDataTypes.BIGINT.value: DataTypes.INT.value,
    GlueDataTypes.BOOLEAN.value: DataTypes.BOOLEAN.value,
    GlueDataTypes.CHAR.value: DataTypes.STRING.value,
    GlueDataTypes.DATE.value: DataTypes.DATE.value,
    GlueDataTypes.DECIMAL.value: DataTypes.FLOAT.value,
    GlueDataTypes.DOUBLE.value: DataTypes.FLOAT.value,
    GlueDataTypes.FLOAT.value: DataTypes.FLOAT.value,
    GlueDataTypes.INT.value: DataTypes.INT.value,
    GlueDataTypes.SMALLINT.value: DataTypes.INT.value,
    GlueDataTypes.STRING.value: DataTypes.STRING.value,
    GlueDataTypes.TIMESTAMP.value: DataTypes.DATE.value,
    GlueDataTypes.TINYINT.value: DataTypes.INT.value,
    GlueDataTypes.VARCHAR.value: DataTypes.STRING.value,
}


ACTIONS = {
    Actions.OMIT.value: Omission,
    Actions.OFFSET.value: Offset,
    Actions.RANDOM_OFFSET.value: RandomOffset,
    Actions.MASK.value: Mask,
    Actions.SALTED_HASH.value: SaltedMask,
    Actions.FREE_TEXT_REPLACEMENT.value: FreeTextReplacement,
    Actions.LOWER_RESOLUTION.value: LowerResolution,
}
