from app import app


@app.route('/')
def hello():
    return 'Déploiement validé !'

@app.route('/test')
def test():
    return 'test validé !'
