from pydantic import BaseModel, Field

from food_preferences import FoodPreferences
from person import Person


class Equipment(BaseModel):
    appliances: list[str] = Field(default_factory=list, description="A list of appliances")
    cookware: list[str] = Field(default_factory=list, description="A list of cookware")


class Household(BaseModel):
    people: list[Person] = Field(default_factory=list, description="A list of people in the household")
    equipment: Equipment = Field(default_factory=Equipment, description="The equipment in the household")

    @property
    def size(self):
        """The number of people in the household"""
        return len(self.people)

    @property
    def food_allergies(self):
        """A list of food allergies"""
        return list(set([allergy for person in self.people for allergy in person.food_allergies]))

    @property
    def food_preferences(self):
        """A list of food preferences"""
        return FoodPreferences(
            likes=list(set([like for person in self.people for like in person.food_preferences.likes])),
            dislikes=list(set([dislike for person in self.people for dislike in person.food_preferences.dislikes]))
        )
