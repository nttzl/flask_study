from flask import Flask, render_template, request
import os, json

app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir('files')
    names = []
    for file in files:
        with open('files/'+file) as f:
            names.append(json.load(f))
    return render_template('index.html', a=names)

@app.route('/files/<filename>')
def file(filename):
    name = 'files/' + filename + '.json'
    if os.path.exists(name):
        with open(name) as f:
            data = json.load(f)
            return render_template('file.html', data=data)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=1, port=3000)