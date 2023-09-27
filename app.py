from flask import Flask, request
from utils import get_finance_data

app = Flask(__name__)


@app.route('/')
def index():
    args = request.args
    return get_finance_data(args.to_dict()["ticker"])


if __name__ == '__main__':
    app.run()
