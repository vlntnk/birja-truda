from flask import Flask, render_template, url_for, request



app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/regist.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
    return render_template('regist.html')



if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)