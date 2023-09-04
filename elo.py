from tinydb import TinyDB, Query

db = TinyDB('./db.json')

def expected_result(elo_1, elo_2):
    expected_1 = 1 / ( 1 + 10** ( ( elo_2 - elo_1)/400 ) )
    return expected_1

def delta_elo(expected_results, actual_results, k = 40):
    total_expected = sum(expected_results)
    total_actual = sum(actual_results)
    delta = k * (total_actual - total_expected)
    return delta

# marco = 1000
# gianna = 700
# sandro = 650

# matches = [("marco","gianna",marco,gianna,0,1)]

# print("L'Exp_res di "+ str(matches[0][0])+" è " + str(expected_result(matches[0][2], matches[0][3])))
