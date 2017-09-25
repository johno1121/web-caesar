from flask import Flask, request 
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
        <html>
            <head>
                <title>Web-caesar</title>
            </head>
            <style>
                form{{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px
                }}
                textarea{{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
            <body>
            <form method="POST">
            <div>
            <label for="rotate_by">Rotate by:</label>
            <input type="text" id="rotate_by" name="rot" value="0" />
            <p class="error"></p>
            </div>
            <textarea name="text" type="text">{0}</textarea>
            <input type="submit" />

            </form>
            </body>
        </html>
    """
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    answer = ""
    new = rotate_string(text, rot)
    answer = answer + new
    rotated = form.format(answer)
    return  rotated 
    
@app.route("/")
def index():
    return form.format("")

app.run()