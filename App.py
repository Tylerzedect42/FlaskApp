from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for files (simulated)
files = []

@app.route('/')
def index():
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if filename and filename not in files:
        files.append(filename)
    return redirect(url_for('index'))

@app.route('/update_file', methods=['POST'])
def update_file():
    old_filename = request.form.get('old_filename')
    new_filename = request.form.get('new_filename')
    if old_filename in files:
        index = files.index(old_filename)
        files[index] = new_filename
    return redirect(url_for('index'))

@app.route('/delete_file', methods=['POST'])
def delete_file():
    filename = request.form.get('filename')
    if filename in files:
        files.remove(filename)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)