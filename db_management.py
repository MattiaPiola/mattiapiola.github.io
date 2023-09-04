from tinydb import TinyDB, Query, operations


db = TinyDB('./elo_database.json')
players = db.table("players")
matches = db.table('matches')

def new_player(name, elo):
    players.insert({'name': name, 'elo': elo})

def new_match(name1, name2, elo1, elo2, exp1, exp2, res1, res2):
    matches.insert({'player1':name1, 'player2': name2, 'elo1':elo1, 'elo2':elo2, 'exp1':exp1, 'exp2':exp2, 'res1':res1, 'res2':res2})

def get_elo(name):
    query = Query()
    elo = players.search(query.name == name)[0]['elo']
    return(elo)

def update_elo(name,delta):
    query = Query()
    players.update(operations.add('elo',delta), query.name==name)