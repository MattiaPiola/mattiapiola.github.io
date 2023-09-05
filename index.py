from bottle import template, route, run
from tinydb import TinyDB, Query
import backend

db = TinyDB('./elo_database.json')
players = db.table("players")
matches = db.table('matches')

@route('/')
@route('/hello/<name>')
def saluto(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/classifica')
def classifica():
    page = '<ol>'
    for player in players:
        element = '<li>' + player['name'] + ': ' + str(player['elo']) + ' points.'
        page += element
    page += '</ul>'
    return page
               
run(host='localhost',port=1990, debug=True)


### https://bottlepy.org/docs/dev/tutorial.html#installation