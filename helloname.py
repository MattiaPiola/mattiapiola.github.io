from bottle import template, route, run 

@route('/')
@route('/hello/<name>')
def saluto(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host='localhost',port=1990, debug=True)


### https://bottlepy.org/docs/dev/tutorial.html#installation