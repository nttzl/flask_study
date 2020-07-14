from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    teacher = {
        'name': 'nttzl',
        'email': 'nttzl@qq.com'
    }

    course = {
        'name': 'Python basic',
        'teacher': teacher,
        'user_count': 5348,
        'price': 199.0,
        'is_private': False,
        'tags': ['python', 'big data', 'linux']
    }
    return render_template("index.html", course=course)

app.run(debug=1)
