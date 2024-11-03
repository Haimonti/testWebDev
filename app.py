from flask import Flask

app = Flask(_name_)
app.config['TESTING']=True

@app.route("/")
def hello_world():
  return "<p>Hello World!</p>"

if _name_ == "_main_":
  app.run(debug=True)
