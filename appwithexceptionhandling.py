from flask import Flask, request, render_template, flash
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/form_login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        url = request.form['url']
        try:
            data = YouTubeTranscriptApi.get_transcript(url)
            text = ""
            for i in data:
                text += i['text'] + '\n'
            return render_template('main.html', info=text)
        except Exception as e:
            flash(f"Error: {str(e)}")
    return render_template('main.html', info=None)

if __name__ == "__main__":
    app.run(debug=True)
