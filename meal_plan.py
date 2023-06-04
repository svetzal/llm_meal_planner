from pydantic import BaseModel, Field


class DayMealPlan(BaseModel):
    breakfast: list[str] = Field(default_factory=list, description="A list of breakfasts")
    lunch: list[str] = Field(default_factory=list, description="A list of lunches")
    dinner: list[str] = Field(default_factory=list, description="A list of dinners")
    snacks: list[str] = Field(default_factory=list, description="A list of snacks")


class MealPlan(BaseModel):
    days: list[DayMealPlan] = Field(default_factory=list, description="A list of day meal plans")
