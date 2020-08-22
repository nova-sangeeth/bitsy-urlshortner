import tldextract
import random
import string


url = input("Enter the url")


class url_sep:
    token_size = 5

    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def extractor(self):
        extratcted_url = tldextract.extract(self)
        token_size = 5
        letters = string.ascii_letters
        if extratcted_url.domain == "amazon":

            return "amz--shp-" + "".join(
                random.choice(letters) for i in range(token_size)
            )
        return "".join(random.choice(letters) for i in range(token_size))
        print(token_size)

    def issue_token(self):
        letters = string.ascii_letters
        # n = "shorter"
        # return n + "".join(random.choice(letters) for i in range(self.token_size))
        return "".join(random.choice(letters) for i in range(self.token_size))


# extractor(url)
# https://www.amazon.in/
