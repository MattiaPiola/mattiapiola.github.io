from bottle import template, route, run
from tinydb import TinyDB, Query
import backend

db = TinyDB('./database.json')
players = db.table("players")
matches = db.table('matches')

# @route('/')
# @route('/hello/<name>')
# def saluto(name='Stranger'):
#     return template('Hello {{name}}, how are you?', name=name)

@route('/classifica')
def classifica():
    page = '<table><tr>'
    for voice in players.all()[0].keys():
        header = '<th>' + voice + '</th>'
        page += header
    page += '</tr>'
    for player in players:
        element = '<tr><td>' + player['name'] + '</td><td>' + str(player['elo']) + '</td></tr>'
        page += element
    page += '</table>'
    return page
               
@route('/prova')
def prova():
    page = ''
    dropdown = '<select>'
    for player in players.all():
        option = '<option>' + player['name'] + '</option>'
        dropdown += option
    dropdown += '</select>'
    page += dropdown*2
    page += '<input type= "button">INVIA</input>'
    return (page)

run(host='localhost',port=1990, debug=True)



### https://bottlepy.org/docs/dev/tutorial.html#installation