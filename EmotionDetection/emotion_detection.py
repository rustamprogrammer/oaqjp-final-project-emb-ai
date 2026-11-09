"""Detect emotions in English text using the Watson NLP service."""

import requests


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network"
        "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=payload, headers=headers, timeout=15)
    emotions = ("anger", "disgust", "fear", "joy", "sadness")
    if response.status_code == 400:
        return dict.fromkeys((*emotions, "dominant_emotion"))
    response.raise_for_status()
    prediction = response.json()["emotionPredictions"][0]["emotion"]
    scores = {name: prediction[name] for name in emotions}
    return {**scores, "dominant_emotion": max(scores, key=scores.get)}
