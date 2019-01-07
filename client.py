from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def index_post():
    if request.form['submit'] == 'Submit':
        company_id = request.form['ID']
        url = "http://192.168.43.204:8000/req"
        data = {"ID": company_id}
        resp = requests.post(url, data=data)
        return render_template('home.html', resp=resp.text)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
