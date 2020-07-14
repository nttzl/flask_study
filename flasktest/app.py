from flask import Flask, url_for, redirect, render_template, make_response
from flask import request, abort

app = Flask(__name__)
app.config.update({
    "SECRET_KEY": b'\xda\xc3\xff\xc2[\x9e\xf3\xae"\xde>`\xf9\x8c\xdf\xf4'
})


@app.route("/")
def index():
    username = request.cookies.get('username')
    if username:
        return f"hello {username}"
    else:
        abort(404)


@app.route("/user/<username>")
def user_index(username):
    print("user-agent:", request.headers.get("User-Agent"))
    print("time:", request.args.get("time"))
    print("q:", request.args.get("q"))
    print("Q:", request.args.getlist("Q"))  # 参数不止一个用 getlist

    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
    return resp
    # return render_template('user_index.html', username=username)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"post {post_id}"


@app.route("/courses/<name>")
def courses(name):
    return f"course:{name}"


@app.route("/test")
def test():
    print(url_for('index'))
    print(url_for('user_index', username="nttzl"))
    print(url_for('show_post', post_id=9, _external=1))
    print(url_for('show_post', post_id=2, q="python 03"))
    print(url_for('show_post', post_id=2, q="python 可以"))
    print(url_for('show_post', post_id=2, _anchor="a"))
    return "test"


@app.route("/register", methods=['get', 'post'])
def register():
    print('method:', request.method)
    print('name:', request.form['name'])
    print('password:', request.form.get('password'))
    print('hobbies:', request.form.getlist('hobbies'))
    return "register successed"


@app.route("/httptest", methods=['get', 'post'])
def httptest():
    print(request.method)
    if request.method == "GET":  # 注意大小写
        print('t', request.args.get('t'))
        print('q', request.args.get('q'))
        return "its a get request"
    elif request.method == "POST":
        print('Q', request.form.getlist('Q'))
        return "its a post request"
    return 'good'


if __name__ == "__main__":
    app.run(debug=1, host="127.0.0.1", port=5000)
