from bottle import route, run

@route('/prova')

def hello():
    return "Hello World!"

run(host='localhost', port=1990, debug=True)
