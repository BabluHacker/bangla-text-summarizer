from flask import Flask, request, jsonify
from mainFile import start
app = Flask(__name__)
@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    try:
        ret = start(text)
        return jsonify(ret), 200
    except Exception as e:
        ret_text = {}
        ret_text['status'] = 0
        return jsonify(ret_text), 400
if __name__ == '__main__':
    app.run()