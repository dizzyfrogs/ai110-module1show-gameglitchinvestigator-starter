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


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
