from app import app
from flask import render_template

@app.route('/')
def hello():
    return render_template("hello.html")

@app.route('/test')
def test():
    return """
<!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <title>Test</title>
 </head>
 <body>
     <h1>Test fonctionne toujours</h1>
 </body>
 </html> """
