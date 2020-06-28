import random
import string


class shortner:
    token_size = 5

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def issue_token(self):
        n = "nova_"
        letters = string.ascii_letters
        return n + "".join(random.choice(letters) for i in range(self.token_size))

