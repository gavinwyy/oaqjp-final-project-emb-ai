import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named emotion_detector that takes a string input (text_to_analyse)
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion detection service

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the emotions from the response
    if response.status_code == 200:
        # Extracting emotions from the response
        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        emotion_scores['dominant_emotion'] = dominant_emotion
    # If the response status code is 400, set emotions to None
    elif response.status_code == 400:
        emotion_scores =  {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}

    # Returning a dictionary containing emotions detection results
    return emotion_scores
