# detect the spam words
spamWords = ["buy now", "subscribe this", "click this"]
spam = False
# email = "this is a nice stock. you need to click this and buy this stock"
email = input("Enter your email: ").lower()
if 'buy now' in email:
    spam = True

if 'subscribe now' in email:
    spam = True

if "click this" in email:
    spam = True

print("spam is", spam)