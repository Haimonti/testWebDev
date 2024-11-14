from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True 

@app.route("/work")
def hello_world():
    return "<p>Hello, World!</p>"

#if __name__ == "__main__":
#    app.run(port=8000, debug=True)
