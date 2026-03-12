import json
import pandas as pd
import streamlit as st
from utils.llm_client import ask_ai
from utils.evaluator import similarity_score

st.title("AI QA Evaluation Dashboard")

results = []

with open("test_data/prompts.json") as file:
    tests = json.load(file)

for test in tests:

    prompt = test["prompt"]
    expected = " ".join(test["expected_keywords"])

    response = ask_ai(prompt)

    score = similarity_score(expected, response)

    status = "PASS" if score > 0.5 else "FAIL"

    results.append({
        "Prompt": prompt,
        "AI Response": response,
        "Score": round(score, 2),
        "Status": status
    })

df = pd.DataFrame(results)

st.dataframe(df)

st.bar_chart(df["Score"])