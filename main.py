from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store notes
programmer_notes = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            programmer_notes[title] = content
        return redirect(url_for('notes'))
    return render_template('notes.html', notes=programmer_notes)

if __name__ == '__main__':
    app.run(debug=True)