from flask import Flask, request, jsonify
from mainFile import start
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "https://summarize.technocrats.io"}})
@app.route('/', methods=['POST'])
def summarize():
    text = request.form['text']
    try:
        ret = start(text)
        ret['status'] = 1
        return jsonify(ret), 200
    except Exception as e:
        ret_text = {}
        ret_text['status'] = 0
        return jsonify(ret_text), 400
if __name__ == '__main__':
    app.run()