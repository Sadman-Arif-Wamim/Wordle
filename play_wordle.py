from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("apple")

    while wordle.can_attempt:
        x = input("Type your guess: ")

        if len(x) != wordle.Word_length:
            print(f"Word must be {wordle.Word_length} characters long")
            continue

        wordle.attempts.append(x)
        result = wordle.guess(x)
        print(*result, sep="\n")
       
    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve!")

if __name__ == "__main__":
    main()