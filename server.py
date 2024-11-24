'''a. Import the relevant libraries and functions'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    '''c. Define the function sent_analyzer'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extracting emotions from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the emotions
    return  f"For the given statement, the system response is 'anger' : {anger}, \
        'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy} and 'sadness' : {sadness}. \
        The dominant emotion is <b>{dominant_emotion}</b>."

@app.route("/")
def render_index_page():
    '''d. Render the HTML template using render_index_page'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
