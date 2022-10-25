from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("apple")

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempts.append(x)
       
    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve!")

if __name__ == "__main__":
    main()