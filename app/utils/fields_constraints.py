from typing import Annotated

from pydantic import Field

from .fields_length import SHORT_NAME_LENGTH_FIELD, NAME_FIELD_LENGTH, LOCATION_LENGTH_FIELD


NameField = Annotated[str, Field(max_length=NAME_FIELD_LENGTH)]
ShortNameField = Annotated[str, Field(max_length=SHORT_NAME_LENGTH_FIELD)]
LocationField = Annotated[str, Field(max_length=LOCATION_LENGTH_FIELD)]
