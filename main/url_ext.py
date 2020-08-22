import tldextract
import random
import string


# url = input("Enter the url:")


class url_sep:
    token_size = 5

    def __init__(self):
        self.token_size = token_size if token_size is not None else 5

    def extractor(self):
        extratcted_url = tldextract.extract(self)

        letters = string.ascii_letters
        if extratcted_url.domain == "amazon":
            # print(
            #     "ama--shp-" + "".join(random.choice(letters) for i in range(token_size))
            # )
            return "ama-shp".join(random.choice(letters) for i in range(token_size))

        elif extratcted_url.domain == "google":
            # print(
            #     "ggle-sch" + "".join(random.choice(letters) for i in range(token_size))
            # )
            return "ggle-sch".join(random.choice(letters) for i in range(token_size))
        # print(token_size)
        else:
            return "".join(random.choice(letters) for i in range(token_size))

    # def issue_token(self):
    #     letters = string.ascii_letters
    #     # n = "shorter"
    #     # return n + "".join(random.choice(letters) for i in range(self.token_size))
    #     return "".join(random.choice(letters) for i in range(self.token_size))


# url_sep.extractor(url)
# https://www.amazon.in/


# import tldextract
# import random
# import string


# url = input("Enter the url")


# def extractor(url):
#     extratcted_url = tldextract.extract(url)
#     token_size = 5
#     letters = string.ascii_letters
#     if extratcted_url.domain == "amazon":
#         print("ama--shp-" + "".join(random.choice(letters) for i in range(token_size)))
#     return "".join(random.choice(letters) for i in range(token_size))
#         print(token_size)

#     def issue_token(self):
#         letters = string.ascii_letters
#         # n = "shorter"
#         # return n + "".join(random.choice(letters) for i in range(self.token_size))
#         return "".join(random.choice(letters) for i in range(self.token_size))


# # extractor(url)
# # https://www.amazon.in/
