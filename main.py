import os
from langchain.chat_models import ChatOpenAI

from allergy import Allergy, TYPE_DRUG, TYPE_ENVIRONMENT
from household import Household, Equipment
from food_preferences import FoodPreferences
from meal_planner import MealPlanner
from person import Person

os.environ['OPENAI_API_KEY'] = os.environ['OPENAI_ACCESS_TOKEN']


def main():
    if os.path.exists("household.json"):
        with open("household.json", "r") as file:
            household = Household.model_validate_json(file.read())
    else:
        household = create_demo_household()

    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

    planner = MealPlanner(household, llm)
    plan = planner.plan_days(7)

    print(plan)


def create_demo_household():
    child = Person(
        name="Child",
        allergies=[
            Allergy(name="Penicillin", type=TYPE_DRUG),
            Allergy(name="Bee stings", type=TYPE_ENVIRONMENT)],
        food_preferences=(FoodPreferences(
            likes=["pizza", "chocolate", "ice cream", "chicken", "pasta"],
            dislikes=[],
        ))
    )
    parent1 = Person(
        name="First Parent",
        allergies=[],
        food_preferences=(FoodPreferences(
            likes=["pizza", "chocolate", "ice cream", "chicken", "pasta"],
            dislikes=[]
        ))
    )
    parent2 = Person(
        name="Second Parent",
        allergies=[],
        food_preferences=(FoodPreferences(
            likes=["pizza", "chocolate", "ice cream", "chicken", "pasta"],
            dislikes=["cilantro"]
        ))
    )
    household = Household(
        allergies=["shellfish"],
        people=[child, parent1, parent2],
        equipment=(Equipment(
            appliances=["fridge", "microwave", "oven", "toaster", "air fryer", "kettle", "blender"],
            cookware=["pot", "pan", "baking tray", "baking dish", "frying pan", "saucepan", "pizza stone"]
        ))
    )
    return household


if __name__ == '__main__':
    main()
