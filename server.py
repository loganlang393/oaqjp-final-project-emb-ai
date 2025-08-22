"""
server.py

This module contains the configuration of the Flask web application 
for the emotion detection project. It handles incoming requests, and 
either processes text input to return an emotional analysis of the 
input, or displays the template for the main page.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/")
def index_route():
    """
    Displays the web application that is constructed in the index.html in the root route /

    Returns:
        template: index.html
    """

    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detects the emotions present within the text provided.

    Args:
        text_to_analyze (str): the text provided by the user to be analyzed

    Returns:
        str: a string constructed by the response from the Emotion Detection API
    """

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again"

    reply = ("For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, "
    f"'joy': {response['joy']} "
    f"and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
    )

    return reply

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
