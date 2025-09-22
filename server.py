from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion_Detector')

@app.route("/emotionDetector")
def run_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Check for empty or invalid input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input. Please provide a text to analyze."

    emotions = emotion_detector(text_to_analyze)
    
    # Check if a dominant emotion was found
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Try again."

    dominant_emotion = emotions['dominant_emotion']
    emotions.pop('dominant_emotion', None)  # Remove dominant_emotion from dictionary
    
    # Format the emotions for display
    emotion_list = [f"'{emotion}': {score}" for emotion, score in emotions.items()]
    formatted_emotions = ", ".join(emotion_list)
    
    # Replace the last comma with " and" for better readability
    if ", " in formatted_emotions:
        formatted_emotions = formatted_emotions.rsplit(", ", 1)
        formatted_emotions = " and ".join(formatted_emotions)
    
    # Construct the final output string
    output_text = f"For the given statement, the system response is {formatted_emotions}. "
    output_text += f"The dominant emotion is <b>{dominant_emotion}</b>."
    
    return output_text

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)