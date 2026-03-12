import json
from utils.llm_client import ask_ai
from utils.evaluator import similarity_score

def test_ai_responses():

    with open("test_data/prompts.json") as file:
        tests = json.load(file)

    for test in tests:

        prompt = test["prompt"]
        expected_keywords = test["expected_keywords"]

        # Ask AI
        response = ask_ai(prompt)

        # Expected answer
        expected = " ".join(expected_keywords)

        # Calculate similarity
        score = similarity_score(expected, response)

        print("\n-----------------------------")
        print("Prompt:", prompt)
        print("AI Response:", response)
        print("Similarity Score:", round(score, 2))

        assert score > 0.5