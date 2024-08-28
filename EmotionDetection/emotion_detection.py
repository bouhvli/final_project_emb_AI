import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 400:
        output_res = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return output_res

    response_in_json = json.loads(response.text)
    emotions = response_in_json['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    output_res = {
        'anger': response_in_json['emotionPredictions'][0]['emotion']['anger'],
        'disgust': response_in_json['emotionPredictions'][0]['emotion']['disgust'],
        'fear': response_in_json['emotionPredictions'][0]['emotion']['fear'],
        'joy': response_in_json['emotionPredictions'][0]['emotion']['joy'],
        'sadness': response_in_json['emotionPredictions'][0]['emotion']['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return output_res
