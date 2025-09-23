import requests
import json

def emotion_detector(text_to_analyze ):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    status_code  = response.status_code
    emotions = (json.loads(response.text))['emotionPredictions'][0]['emotion']
    if status_code == 400:
        for key in emotions:
            emotions[key] = None
    # emotions = (json.loads(response.text))['emotionPredictions'][0]['emotion']
    else:
        emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions