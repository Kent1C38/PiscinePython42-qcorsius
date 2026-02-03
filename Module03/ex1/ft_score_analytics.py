from sys import argv

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(argv) <= 1:
        print("No scores provided. Usage:" +
              "python3.13 ft_score_analytics.py <score1> <score2> ...")
    else:
        valid = True
        scores = []
        for arg in argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError as e:
                print(f"Couldn't parse arguments into numbers: {e}")
                valid = False
        if valid:
            print(f"Score processes: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
