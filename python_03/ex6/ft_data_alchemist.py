import random


def main() -> None:
    initial_names = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
                     "john", "kevin", "Liam"]
    print(f"Initial list of players: {initial_names}")

    all_capitalized = [name.capitalize() for name in initial_names]
    print(f"New list with all names capitalized: {all_capitalized}")

    only_capitalized = [name for name in initial_names if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f"Score average: {average:.2f}")

    highscores = {name: score for name, score in scores.items()
                  if score > average}
    print(f"Highscores: {highscores}")


if __name__ == "__main__":
    main()
