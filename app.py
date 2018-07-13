from flask import Flask, request
import re

app = Flask(__name__)

PORT = 4390


@app.route('/')
def homepage():
    return "Howdy hacker!!"


@app.route('/scheduleme', methods=['POST'])
def scheduleme():
    # Get the text from the request sent by Slack
    raw_text = request.form.get('text')

    # The raw_text is in wrapped in single quotes in the format '"title" "start" "end"'
    # This regular expression unwraps the single quotes and puts all strings into an array with
    # the format: ["title", "start", "end"]
    text_array = re.findall(r'"(.*?)"', raw_text)
    if len(text_array) != 3:
        return 'The format is /scheduleme "[title]" "[start date & time]" "[end date & time]"'

    title, start, end = text_array
    return f'Sweet I parsed the title: {title}, start: {start} and end: {end}'


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
