import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myObj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myObj, headers = header)
    if response.status_code == 400:
        return {'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None}

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    highest_score = 0.0
    highest_emotion = ""

    emotion_keys = emotions.keys()

    for emotion in emotion_keys:
        if emotions[emotion] > highest_score:
            highest_emotion = emotion
            highest_score = emotions[emotion]
    
    emotions['dominant_emotion'] = highest_emotion

    return emotions 