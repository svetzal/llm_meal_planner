import enum
from pydantic.fields import Field
from pydantic.main import BaseModel

TYPE_FOOD = "food"
TYPE_DRUG = "drug"
TYPE_ENVIRONMENT = "environment"


class Allergy(BaseModel):
    name: str = Field(default_factory=str, description="The name of the allergy")
    type: str = Field(default_factory=str, description="The type of allergy")
