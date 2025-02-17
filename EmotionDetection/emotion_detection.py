import requests, json

# Define a maximum size limit for incoming jsons (in bytes) - for security
_MAX_SIZE = 100000

# Calling IBM embedded NLP
_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
_STATUES400 = {
"anger": None, 
"disgust": None, 
"fear": None, 
"joy": None, 
"sadness": None, 
"dominant_emotion": None
}

# Conforming to API's rules
def _ibm_text_requirement_format(text_to_analyse):
    return { "raw_document": { "text": f"{text_to_analyse}" } }

# There are malicious jsons! TODO
def _safe_load_json(response):
    content_length = len(response.content)
    if content_length > _MAX_SIZE:
        raise ValueError("JSON data exceeds the size limit")
    return json.loads(response.content)

def emotion_detector(text_to_analyse):
    formatted_text = _ibm_text_requirement_format(text_to_analyse)
    response = requests.post(url = _URL, headers = _HEADERS, json = formatted_text)
    if response.status_code == 400:
        return _STATUES400
    try:
        # returns python dictionary
        response = _safe_load_json(response)
        # returns a dictonary with the emotions and respecitve scores by IBM
        emotions_scores = response['emotionPredictions'][0]['emotion']
        # logic for finiding dominant emotion
        dominant_emotion = None
        highest_score = 0
        for emotion, score in emotions_scores.items():
            if score > highest_score:
                highest_score = score
                dominant_emotion = emotion
                emotions_scores[emotion] = emotions_scores[emotion]
        emotions_scores['dominant_emotion'] = dominant_emotion
        return emotions_scores
    except ValueError as e:
        return f"Error: {e}"
    except json.JSONDecodeError as e:
        return f"Failed to decode JSON: {e}"
