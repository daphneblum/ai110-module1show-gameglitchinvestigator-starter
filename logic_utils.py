def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"


# Bugs fixed using Claude Code:
# 1. Score was initialized to 0 and win added points on top (e.g. first-try win gave 100
#    added to 0, but later guesses produced inflated totals like 180). Fixed by starting
#    score at 100 and having a win simply return the current score unchanged.
# 2. Wrong guesses used inconsistent +5/-5 adjustments instead of a flat -10 penalty.
#    Fixed so each incorrect guess deducts 10 points, with a minimum score of 10.
# 3. attempts was initialized to 1 instead of 0, causing the first guess to be counted
#    as the second attempt and awarding 90 points instead of 100 on a first-try win.
#    Fixed by initializing attempts to 0 in app.py.
def update_score(current_score: int, outcome: str):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        return current_score

    if outcome in ("Too High", "Too Low"):
        return max(current_score - 10, 10)

    return current_score
