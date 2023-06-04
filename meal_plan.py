from pydantic import BaseModel, Field


class DayMealPlan(BaseModel):
    breakfast: str = Field(default_factory=list, description="Breakfast description")
    morning_snack: str = Field(default_factory=list, description="Morning snack description")
    lunch: str = Field(default_factory=list, description="Lunch description")
    afternoon_snack: str = Field(default_factory=list, description="Afternoon snack description")
    dinner: str = Field(default_factory=list, description="Dinner description")
    evening_snack: str = Field(default_factory=list, description="Evening snack description")


class MealPlan(BaseModel):
    days: list[DayMealPlan] = Field(default_factory=list, description="A list of day meal plans")
