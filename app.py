import random
import prometheus_client
from flask import Flask, Response, render_template
from helpers.middleware import setup_metrics

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
app = Flask(__name__)
setup_metrics(app)


@app.route("/")
def hello():
    RandNumber = random.randint(0, 10)
    if RandNumber <= 5:
        return "Hello Universe!"
    else:
        return "Internal Server Error", 500


@app.route("/version")
def version():
    return "0.3.0"


@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
