from bottle import template, route, run, request, get, post
from tinydb import TinyDB, Query
import backend
from datetime import datetime

db = TinyDB('./database.json')
players = db.table("players")
matches = db.table('matches')

@route('/classifica')
def classifica():
    page = '<head>'
    page += '<style>table, th, td {border: 1px solid black;}</style>'
    page += '</head>'
    page += '<body><h1>Classifica</h1><table><tr>'
    for voice in players.all()[0].keys():
        header = '<th>' + voice + '</th>'
        page += header
    page += '</tr>'
    for player in players:
        element = '<tr><td>' + player['name'] + '</td><td>' + str(player['elo']) + '</td></tr>'
        page += element
    page += '</table></body>'
    return page
               
@get('/newmatch')               
def newmatch():
    page = '<form action="/newmatch" method="POST">'
    
    date = '<div><input type="date" name="date" value='+datetime.now().strftime("%Y-%m-%d") + '></input></div>'
    page += date
    
    player1 = '<div><select name="player1">'
    for player in players.all():
        option = '<option value=' + player['name'] + '>' + player['name'] + '</option>'
        player1 += option
    player1 += '</select>'
    page += player1
    
    player2 = '<select name="player2">'
    for player in players.all():
        option = '<option value=' + player['name'] + '>' + player['name'] + '</option>'
        player2 += option
    player2 += '</select></div>'
    page += player2

    win1 = '<div><input type="radio" name="res1" value=1 label="giocatore 1"/>'
    win2 = '<input type="radio" name="res1" value=0 label="giocatore 2"/></div>'
    page += win1 + win2
    page += '<input type="submit" value="INVIA">'
    page += '</form>'

    page += matches_table()
    
    return (page)

@post('/newmatch')
def newmatch():
    date = request.forms.get('date')
    player1 = request.forms.get('player1')
    player2 = request.forms.get('player2')
    elo1 = players.search(Query().name == player1)[0]['elo']
    elo2 = players.search(Query().name == player2)[0]['elo']
    exp1 = backend.expected_result(elo1, elo2)
    exp2 = backend.expected_result(elo2, elo1)
    res1 = int(request.forms.get('res1'))
    # res2 should be 1 when res1 is 0 and viceversa
    res2 = 1 - res1
    backend.new_match(date, player1, player2,elo1,elo2,exp1,exp2,res1,res2)
    page = ('<p>Match added</p><a href="/newmatch">New match</a>')
    page += matches_table()
    return page


@route('/hello/<name>')
def saluto(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

def matches_table():
    today = datetime.now().strftime("%Y-%m-%d")
    today_matches = backend.get_today_matches(today)
    table = '<table><tr><th>Giocatore 1</th><th>Giocatore 2</th><th>Risultato</th></tr>'
    for match in today_matches:
        row = '<tr><td>' + match['player1'] + '</td><td>' + match['player2'] + '</td><td>' + str(match['res1']) + ' - ' + str(match['res2']) + '</td></tr>'
        table += row
    table += '</table>'
    return table


run(host='localhost',port=1990, debug=True)

### https://bottlepy.org/docs/dev/tutorial.html#installation