from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('cookie_index.html')

@app.route('/setcookie', methods = ['get','post'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('read_cookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome, ' + name + '</h>'

if __name__ == "__main__":
    app.run(debug=1)
