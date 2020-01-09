import talon
# don't forget to init the library first
# it loads machine learning classifiers
talon.init()

from talon import signature


message = """Thanks Sasha, I can't go any higher and is why I limited it to the
homepage.

John Doe
via mobile"""




text, signature = signature.extract(message, sender='john.doe@example.com')
# text == "Thanks Sasha, I can't go any higher and is why I limited it to the\nhomepage."
# signature == "John Doe\nvia mobile"

print(text)
print('########')
print(signature)

# from talon.signature.bruteforce import extract_signature
#
#
# # message = """Wow. Awesome!
# # --
# # Bob Smith"""
# message = """Thanks Sasha, I can't go any higher and is why I limited it to the
# homepage.
#
# John Doe
# via mobile"""
#
# text, signature = extract_signature(message)
# print(signature)
# # text == "Wow. Awesome!"
# # signature == "--\nBob Smith"