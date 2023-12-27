from flask import Flask,request,render_template
from youtube_transcript_api import YouTubeTranscriptApi 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    url = request.form['url']
    data = YouTubeTranscriptApi.get_transcript(url)
    text = ""
    for i in data:
        text += i['text'] + '\n'
    print(text)
    return render_template('main.html',info = text)

if __name__ == "__main__":
    app.run()