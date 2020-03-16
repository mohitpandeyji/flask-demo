# Using flask to make an api
# import necessary libraries and functions
import os
from flask import Flask, jsonify, request, flash
from werkzeug.utils import secure_filename

# creating a Flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]iasdfffsd/'


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

    # A simple function to calculate the square of a number


# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})


@app.route('/form-example', methods=['GET', 'POST'])  # allow both GET and POST requests
def form_example():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        text = request.form.get('text')

        file = request.files['file']
        # create the folders when setting up your app
        os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

        # when saving the file
        file.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(file.filename)))
        flash('File successfully uploaded')
        return '''<h1>The text value is: {}</h1>
        <h1>The file value is: {}</h1>
                  '''.format(text, file)

    return '''
    <form enctype="multipart/form-data" method="post">
        <p>
        Type some text (if you like):<br>
        <input type="text" name="text" size="30">
        </p>
        <p>
        Please specify a file, or a set of files:<br>
        <input type="file" name="file" size="40">
        </p>
        <div>
        <input type="submit" value="Submit">
        </div>
    </form>
     '''


# driver function
if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    sess.init_app(app)
    app.debug = True
    app.run()
