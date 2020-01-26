from app import app



@app.route('/')
def hello():
    return """
<!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <title>Hello</title>
 </head>
 <body>
     <h1>Hello World réussi</h1>
 </body>
 </html> """

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
     <h1>Test réussi</h1>
 </body>
 </html> """
