from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


'''    
@app.route('/start')
def start():
    return '<h1>Start!! </h1>'


@app.route('/select/<name>') #매개변수를 줄 수 있다. 이렇게 사용하면 name이라는 변수를 넣을 수 있음
def select(name):
    return 'hi %s' % name


@app.route('/')
def hello_world():
    return '<h1>Hello world</h1><input type = "textbox"/>'
    #return 'Hello world!'  #여기 return 값은 html 그 자체!
'''

if __name__ == "__main__":
    app.run()