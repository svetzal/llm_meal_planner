from langchain import PromptTemplate, LLMChain
from langchain.output_parsers import PydanticOutputParser

from meal_plan import MealPlan


class MealPlanner:
    def __init__(self, household, llm):
        self.household = household
        self.llm = llm

    def plan(self, days):
        prompt = """
        You are an expert meal planner who really cares about your family's happiness, health
        and nutrition. You never include foods to which your family members have
        allergies, and you try to limit the amount of foods they dislike. You also
        try to include their favourite foods as much as possible. The house only has
        a limited number of appliances and cookware, so you need to make sure that
        you don't plan meals that require different appliances or cookware than you
        have. Try to re-use ingredients between meals and snacks as much as possible
        to reduce waste.

        Food Allergies (never include food that will trigger these): {allergies}
        Available appliances: {available_appliances}    
        Available cookware: {available_cookware}
        Favourite foods: {favourite_foods}
        Disliked foods: {disliked_foods}

        Respond in the following format:
        {format_instructions}

        Create a meal plan for a household of {family_size} that includes breakfast,
        lunch, dinner, and snacks for {days} days.
        """

        parser = PydanticOutputParser(pydantic_object=MealPlan)
        task = PromptTemplate(
            input_variables=["days"],
            template=prompt,
            partial_variables={
                "allergies": ", ".join(self.household.allergies),
                "available_appliances": ", ".join(self.household.equipment.appliances),
                "available_cookware": ", ".join(self.household.equipment.cookware),
                "favourite_foods": ", ".join(self.household.food_preferences.likes),
                "disliked_foods": ", ".join(self.household.food_preferences.dislikes),
                "family_size": self.household.size,
                "format_instructions": parser.get_format_instructions(),
            }
        )
        chain = LLMChain(llm=self.llm, prompt=task, verbose=True)
        response = chain.run(
            output_parser=parser,
            days=days,
        )
        return response
