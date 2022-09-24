from flask import Flask

app = Flask(name)

template = """
<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <header></header>
    <main>hello</main>
    <footer></footer>
  </body>
</html>
"""

@app.route('/')
def index():
    return template

@app.route('/lybrary')
def lybrary():
    return "Welcome, to lybrary!"

@app.route('/<name>')
def print_name(name):
    return f"<h1>Hello {name} </h1>"

app.run(debug=True)