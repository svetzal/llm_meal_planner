import os
from langchain.chat_models import ChatOpenAI

from household import FoodPreferences, Household, Equipment
from meal_planner import MealPlanner

os.environ['OPENAI_API_KEY'] = os.environ['OPENAI_ACCESS_TOKEN']


def main():
    household = Household(
        allergies=["shellfish"],
        size=4,
        equipment=(Equipment(
            appliances=["fridge", "microwave", "oven", "toaster", "kettle", "blender"],
            cookware=["pot", "pan", "baking tray", "baking dish", "frying pan", "saucepan"]
        )),
        food_preferences=(FoodPreferences(
            likes=["pizza", "chocolate", "ice cream", "chicken", "pasta"],
            dislikes=["mushrooms", "onions", "tomatoes", "peppers", "olives"]
        ))
    )

    llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

    response = MealPlanner(household, llm).plan_days(7)

    print(response)


if __name__ == '__main__':
    main()
