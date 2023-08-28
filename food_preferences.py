from pydantic import BaseModel, Field


class FoodPreferences(BaseModel):
    dislikes: list[str] = Field(default_factory=list, description="A list of dislikes")
    likes: list[str] = Field(default_factory=list, description="A list of likes")
