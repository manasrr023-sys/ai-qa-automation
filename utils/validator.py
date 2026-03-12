from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def validate_response(response, expected_keywords):

    response_lower = response.lower()

    for keyword in expected_keywords:
        if keyword.lower() in response_lower:
            return True

    return False


def hallucination_score(expected_text, ai_response):

    emb1 = model.encode([expected_text])
    emb2 = model.encode([ai_response])

    score = cosine_similarity(emb1, emb2)[0][0]

    return score