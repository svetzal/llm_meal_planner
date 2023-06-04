from pydantic import BaseModel, Field


class Equipment(BaseModel):
    appliances: list[str] = Field(default_factory=list, description="A list of appliances")
    cookware: list[str] = Field(default_factory=list, description="A list of cookware")


class FoodPreferences(BaseModel):
    dislikes: list[str] = Field(default_factory=list, description="A list of dislikes")
    likes: list[str] = Field(default_factory=list, description="A list of likes")


class Household(BaseModel):
    allergies: list[str] = Field(default_factory=list, description="A list of allergies")
    size: int = Field(default=4, description="The number of people in the household")
    equipment: Equipment = Field(default_factory=Equipment, description="The equipment in the household")
    food_preferences: FoodPreferences = Field(default_factory=FoodPreferences,
                                              description="The food preferences of the household")
