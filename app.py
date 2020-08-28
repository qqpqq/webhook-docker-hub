import os
import http
from flask import Flask


app = Flask(__name__)


@app.route("/web-hook")
def deploy():
    os.system("deploy.sh")
    return http.HTTPStatus.OK


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)