import tldextract
import random
import string


url = input("Enter the url")


def extractor(url):
    extratcted_url = tldextract.extract(url)
    token_size = 5
    letters = string.ascii_letters
    if extratcted_url.domain == "amazon":
        print("ama--shp-" + "".join(random.choice(letters) for i in range(token_size)))
    return "".join(random.choice(letters) for i in range(token_size))


extractor(url)
# https://www.amazon.in/
