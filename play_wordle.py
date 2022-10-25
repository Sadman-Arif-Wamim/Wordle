from wordle import Wordle

def main():
    print("Hello Wordle!")
    wordle = Wordle("apple")
    print(wordle)
    while True:
        x = input("Type your guess: ")
        if x == wordle.secret:
            print("You have guessed the word!")
            break
        print("Your guess is incorrect!")

if __name__ == "__main__":
    main()