class Wordle:

    Max_Attempts = 6
    Word_length = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    @property
    def is_solved(self):
        return self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        self.Max_Attempts - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts == 0 and self.is_solved