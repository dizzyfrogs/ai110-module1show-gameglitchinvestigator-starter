from logic_utils import check_guess, get_range_for_difficulty, update_score

def test_hard_range_wider_than_normal():
    # Hard difficulty should have a wider range than Normal to be genuinely harder
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high


def test_too_high_message_says_lower():
    # When guess exceeds the secret, the hint should direct the player downward
    _, message = check_guess(60, 50)
    assert "LOWER" in message


def test_too_low_message_says_higher():
    # When guess is below the secret, the hint should direct the player upward
    _, message = check_guess(40, 50)
    assert "HIGHER" in message


def test_too_high_on_even_attempt_deducts_score():
    # A wrong guess should never earn points, regardless of attempt parity
    score = update_score(100, "Too High", attempt_number=2)
    assert score < 100


def test_easy_range_is_1_to_20():
    # Easy range must be narrow so new games generate secrets within the correct bounds
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20


def test_win_on_first_attempt_uses_attempt_number_1():
    # Scoring a win on attempt 1 should give 100 - 10*(1+1) = 80 points,
    # confirming attempt counting starts at 1 (not 0)
    score = update_score(0, "Win", attempt_number=1)
    assert score == 80


def test_each_difficulty_has_distinct_range():
    # Each difficulty should produce a different range so the UI displays correct bounds
    easy = get_range_for_difficulty("Easy")
    normal = get_range_for_difficulty("Normal")
    hard = get_range_for_difficulty("Hard")
    assert easy != normal
    assert normal != hard
    assert easy != hard


def test_numeric_comparison_not_lexicographic():
    # 9 < 10 numerically but "9" > "10" lexicographically; must use int comparison
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
