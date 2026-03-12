import json
from utils.llm_client import ask_ai

def test_prompt_regression():

    with open("test_data/baseline_responses.json") as f:
        baseline = json.load(f)

    for prompt, expected in baseline.items():

        response = ask_ai(prompt)

        print("\nPrompt:", prompt)
        print("Expected:", expected)
        print("Actual:", response)

        assert expected.lower() in response.lower()