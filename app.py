from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

        return '''
<html>
    <head>
        <title>Vezba</title>
    </head>
    <body>
        <h1>Welcome!</h1>
    </body>
</html>'''