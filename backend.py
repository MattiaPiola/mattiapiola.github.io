from tinydb import TinyDB, Query, operations
import datetime
from random import choice, randint

db = TinyDB('./database.json')
players = db.table("players")
matches = db.table('matches')

def database_setup():
    db = TinyDB('./database.json')
    players = db.table("players")
    matches = db.table('matches')

def database_cleanup():
    db.drop_tables()

def new_player(name, elo):
    players.insert({'name': name, 'elo': elo})

# data si fa così: date= datetime.now() e poi date = date.strftime('%d%m%y')
def new_match(date, name1, name2, elo1, elo2, exp1, exp2, res1, res2):
    matches.insert({'date':date, 'player1':name1, 'player2': name2, 'elo1':elo1, 'elo2':elo2, 'exp1':exp1, 'exp2':exp2, 'res1':res1, 'res2':res2})

def get_elo(name):
    query = Query()
    elo = players.search(query.name == name)[0]['elo']
    return(elo)

def update_elo(name,delta):
    query = Query()
    players.update(operations.add('elo',delta), query.name==name)

def get_total_exp(date, name):
    query = Query()
    total_exp = 0
    day_matches = matches.search(query.date == date)
    for match in day_matches:
        if match['player1'] == name:
            total_exp += match['exp1']
        elif match['player2'] == name:
            total_exp += match['exp2']
    return total_exp

def get_total_res(date, name):
    query = Query()
    total_res = 0
    day_matches = matches.search(query.date == date)
    for match in day_matches:
        if match['player1'] == name:
            total_res += match['res1']
        elif match['player2'] == name:
            total_res += match['res2']
    return total_res

def expected_result(elo_1, elo_2):
    expected = 1 / ( 1 + 10** ( ( elo_2 - elo_1)/400 ) )
    expected = round(expected, 2)
    return expected

def delta_elo(expected_results, actual_results, k = 40):
    total_expected = sum(expected_results)
    total_actual = sum(actual_results)
    delta = k * (total_actual - total_expected)
    return delta

###################################################################

#FUNCTIONS FOR FAST PROTOTYPING
def fill_players():
    players.truncate()
    pls = ['edo','gio','teo','fra','eli','tia','pio']
    for pl in pls:
        new_player(pl,randint(700,1500))

def empty_matches():
    matches.truncate()

def random_match():
    date = datetime.datetime.now().strftime('%d%m%y')
    pl1 = choice(players.all())['name']
    other_pls= list(filter(lambda i:i['name']!=pl1,players.all()))
    pl2 = choice(other_pls)['name']
    elo1 = get_elo(pl1)
    elo2 = get_elo(pl2)
    exp1 = expected_result(elo1,elo2)
    exp2 = 1 - exp1
    res1 = randint(0,1)
    res2 = -1 * (res1 - 1)
    new_match(date,pl1,pl2,elo1,elo2,exp1,exp2,res1,res2)