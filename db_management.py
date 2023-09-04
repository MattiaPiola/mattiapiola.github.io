from tinydb import TinyDB, Query

db = TinyDB('./elo_database.json')
players = db.table("players")

def new_player(name, elo):
    players.insert({'name': name, 'elo': elo})

# def update_elo(name, elo_delta):

