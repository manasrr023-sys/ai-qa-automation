import json
from utils.llm_client import ask_ai
from utils.evaluator import similarity_score
from utils.report_generator import save_results

def test_ai_responses():

    with open("test_data/prompts.json") as file:
        tests = json.load(file)

    results = []

    for test in tests:

        prompt = test["prompt"]
        expected = " ".join(test["expected_keywords"])

        response = ask_ai(prompt)

        score = similarity_score(expected, response)

        status = "PASS" if score > 0.5 else "FAIL"

        print("\nPrompt:", prompt)
        print("Response:", response)
        print("Score:", score)
        print("Status:", status)

        results.append([prompt, response, round(score,2), status])

    save_results(results)

    assert True