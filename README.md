# LLM Meal Planner

Consider this, for now, a starter project for illustrating how to use `langchain` and generative LLMs to populate
programmatic structures.

A few places you'll find interesting:

`main.py` - this is the main entry point. It sets up a `Household` and then uses that as input to the `MealPlanner`.
Then it has the planner plan out 7 days worth of meals and prints the `MealPlan` data structure to the console.

`meal_planner.py` - this is where the LLM interesting bits are. Pay particular attention to the multi-line prompt string
in the initializer. See how there are two sets of input variables - one set is defined up front based on the household,
and then the number of days to plan is provided as a run-time argument.

# Running this code

You'll need to set up your python environment. I usually do something like:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Make sure your OpenAI key is in your environment:

```bash
export OPENAI_ACCESS_TOKEN=<your access token here>
```

Then you can run the code:

```bash
python main.py
```