from flask import Flask, render_template, request, redirect
import os
from fetch import fetch


base_path = os.path.dirname(os.path.abspath(__file__))
upload_path = base_path + "/uploads/"

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_csv():

    if request.method == 'POST':

        if request.files:
            file = request.files["resume"]

            # creating folder to save the file if doesnt exist.
            if not os.path.isdir(upload_path):
                os.mkdir(upload_path)

            # creating a file path for saving the file
            file_path = upload_path + file.filename
            file.save(file_path)
            result = fetch(file_path)
            return render_template('result.html', result=result)


@app.route('/result')
def result():
    return render_template('result.html', result)

if __name__ == "__main__":
    app.run(debug=True,port=5002,host='127.0.0.1')





