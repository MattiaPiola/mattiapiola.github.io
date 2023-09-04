def expected_result(elo_1, elo_2):
    expected_1 = 1 / ( 1 + 10** ( ( elo_2 - elo_1)/400 ) )
    return expected_1

def delta_elo(expected_results, actual_results, k = 40):
    total_expected = sum(expected_results)
    total_actual = sum(actual_results)
    delta = k * (total_actual - total_expected)
    return delta


