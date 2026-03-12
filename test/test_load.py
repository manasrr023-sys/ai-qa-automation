import time
from utils.llm_client import ask_ai

def test_load():

    prompt = "Explain artificial intelligence"

    start = time.time()

    for i in range(5):
        response = ask_ai(prompt)
        print("Response", i+1)

    end = time.time()

    print("Total Time:", end - start)

    assert (end - start) < 20