import requests
import json

def emotion_detector(text):
    text_to_analyze = text
    response = requests.post(
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze } }
    )
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_score = max(emotions.values())
    for key, value in emotions.items():
        if value == max_score:
            dominant_emotion = key
            break
    
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions



    
    