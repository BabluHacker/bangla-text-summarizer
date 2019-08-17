from flask import Flask, render_template, request, redirect, send_from_directory, url_for, jsonify
from mainFile import start
app = Flask(__name__)
@app.route('/summarize', methods=['GET'])
def summarize():
    text = request.args.get('text')
    ret = start(text)
    return jsonify(ret), 200
if __name__ == '__main__':
    app.run()