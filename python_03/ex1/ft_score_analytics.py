import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score_list = []
    for i in sys.argv[1:]:
        try:
            score = int(i)
            score_list.append(score)
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    if len(score_list) == 0:
        print("No scores provided. Usage:"
              " python ft_score_analytics.py <score1> <score2> ...\n")
        return
    print(f"Scores processed: {score_list}")
    print(f"Total players: {len(score_list)}")
    print(f"Total score: {sum(score_list)}")
    print(f"Average score: {sum(score_list) / len(score_list):.1f}")
    print(f"High score: {max(score_list)}")
    print(f"Low score: {min(score_list)}")
    print(f"Score range: {max(score_list) - min(score_list)}\n")


if __name__ == "__main__":
    main()
