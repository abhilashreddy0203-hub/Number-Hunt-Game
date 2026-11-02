import random
import json
import os
DIFFICULTIES = [
    {"id": "easy", "label": "Easy", "min": 1, "max": 50, "attempts": 8, "blurb": "A small haystack."},
    {"id": "classic", "label": "Classic", "min": 1, "max": 100, "attempts": 7, "blurb": "The original hunt."},
    {"id": "hard", "label": "Hard", "min": 1, "max": 500, "attempts": 9, "blurb": "Think in halves."},
    {"id": "insane", "label": "Insane", "min": 1, "max": 1000, "attempts": 10, "blurb": "No room for luck."},
]
DEFAULT_DIFFICULTY_ID = "classic"
BEST_FILE = "number_hunt_best.json"
def find_difficulty(difficulty_id):
    return next((d for d in DIFFICULTIES if d["id"] == difficulty_id), DIFFICULTIES[1])
def generate_number(min_val, max_val):
    return random.randint(min_val, max_val)
def check_guess(guess, secret):
    if guess == secret:
        return "correct"
    return "low" if guess < secret else "high"
def validate_guess(raw, min_val, max_val):
    trimmed = str(raw or "").strip()
    if not trimmed:
        return {"ok": False, "error": "Enter a number to guess."}
    if not (trimmed.lstrip("-").isdigit()):
        return {"ok": False, "error": "Whole numbers only."}
    value = int(trimmed)
    if value < min_val or value > max_val:
        return {"ok": False, "error": f"Stay between {min_val} and {max_val}."}
    return {"ok": True, "value": value}
def narrowed_range(min_val, max_val, history):
    low, high = min_val, max_val
    for guess in history:
        if guess["outcome"] == "low" and guess["value"] + 1 > low:
            low = guess["value"] + 1
        if guess["outcome"] == "high" and guess["value"] - 1 < high:
            high = guess["value"] - 1
    return {"low": low, "high": high}
def read_best_scores():
    try:
        with open(BEST_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def record_best_score(difficulty_id, attempts):
    scores = read_best_scores()
    current = scores.get(difficulty_id)
    if isinstance(current, int) and current <= attempts:
        return {"scores": scores, "improved": False}
    scores[difficulty_id] = attempts
    try:
        with open(BEST_FILE, "w") as f:
            json.dump(scores, f)
    except OSError:
        pass
    return {"scores": scores, "improved": True}
def choose_difficulty():
    print("\nChoose a difficulty:")
    for i, d in enumerate(DIFFICULTIES, 1):
        print(f"  {i}. {d['label']}  ({d['min']}–{d['max']}, {d['attempts']} tries) — {d['blurb']}")
    while True:
        choice = input("\nPick 1-4: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(DIFFICULTIES):
            return DIFFICULTIES[int(choice) - 1]
        print("Invalid choice. Enter a number 1-4.")
def play_round(difficulty):
    secret = generate_number(difficulty["min"], difficulty["max"])
    history = []
    print(f"\n=== {difficulty['label'].upper()} ===  range {difficulty['min']}–{difficulty['max']}")

    while len(history) < difficulty["attempts"]:
        attempts_left = difficulty["attempts"] - len(history)
        bounds = narrowed_range(difficulty["min"], difficulty["max"], history)
        print(f"\nTries left: {attempts_left}  |  still possible: {bounds['low']}–{bounds['high']}")
        raw = input("Your guess: ")
        validation = validate_guess(raw, difficulty["min"], difficulty["max"])
        if not validation["ok"]:
            print(f"  ✗ {validation['error']}")
            continue
        if any(g["value"] == validation["value"] for g in history):
            print("  ✗ You already tried that number.")
            continue

        outcome = check_guess(validation["value"], secret)
        history.append({"value": validation["value"], "outcome": outcome})

        if outcome == "correct":
            result = record_best_score(difficulty["id"], len(history))
            print(f"\n🎉 Correct! You found {secret} in {len(history)} "
                  f"{'attempt' if len(history) == 1 else 'tries'}.")
            if result["improved"]:
                print("🏆 New best score on " + difficulty["label"] + "!")
            return

        label = "Too low — aim higher" if outcome == "low" else "Too high — aim lower"
        print(f"  {validation['value']}: {label}")

    print(f"\n💥 Out of tries. The secret was {secret}.")
def main():
    print("Number Hunt — find the secret number!")
    best_scores = read_best_scores()
    if best_scores:
        print("Best scores: " + ", ".join(f"{k}: {v}" for k, v in best_scores.items()))

    while True:
        difficulty = choose_difficulty()
        play_round(difficulty)
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break
if __name__ == "__main__":
    main()