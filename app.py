import os
from flask import Flask


app = Flask(__name__)


@app.route("/web-hook")
def deploy():
    
    os.system(os.path.dirname(os.path.abspath("__file__"))+"/deploy.sh")
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=False)