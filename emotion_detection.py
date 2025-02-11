import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    JSON = { "raw_document": { "text": text_to_analyse } }
    results = requests.post(url = URL, headers = HEADERS, json = JSON)
    return results

emotion_analysis = emotion_detector("Am I happy or glad?")
print(emotion_analysis)

