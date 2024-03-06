from flask import Flask
app = Flask(__name__)
@app.route('/app')
def hello():
    return 'HELLO'
@app.route('/')
def hi():
    return 'HI'
if __name__ == '_main_':
    app.run()

