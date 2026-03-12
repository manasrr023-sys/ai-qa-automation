import json
from utils.llm_client import ask_ai
from utils.validator import validate_response, hallucination_score

def test_ai_responses():

    with open("test_data/prompts.json") as file:
        tests = json.load(file)

    for test in tests:

        prompt = test["prompt"]
        keywords = test["expected_keywords"]

        response = ask_ai(prompt)

        expected_text = " ".join(keywords)

        score = hallucination_score(expected_text, response)

        print("\n----------------------------------")
        print("Prompt:", prompt)
        print("Expected Keywords:", keywords)
        print("AI Response:", response)
        print("Similarity Score:", round(score, 2))

        if score > 0.5:
            print("Evaluation: PASS")
        else:
            print("Evaluation: FAIL")

        assert score > 0.3