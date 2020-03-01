from app import app


@app.route('/index')
@app.route('/')
def index():
    return 'Hello World!'
    
@app.route('/test/', defaults={'name': None})
@app.route('/test/<name>')
def teste(name):
    if name:
        return f'Olá, {name}!'
    else:
        return 'Olá!'
