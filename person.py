from pydantic.fields import Field
from pydantic.main import BaseModel

from allergy import Allergy, TYPE_FOOD
from food_preferences import FoodPreferences


class Person(BaseModel):
    name: str = Field(default_factory=str, description="The person's name")
    email: str = Field(default_factory=str, description="The person's email")
    phone: str = Field(default_factory=str, description="The person's cell phone number")
    allergies: list[Allergy] = Field(default_factory=list, description="A list of allergies")
    food_preferences: FoodPreferences = Field(default_factory=FoodPreferences, description="The person's food preferences")

    @property
    def food_allergies(self):
        """A list of food allergies"""
        return [allergy for allergy in self.allergies if allergy.type == TYPE_FOOD]
