# detecting Double spaces
myStr = "This is me  and I  am a good boy"

print(myStr.find("  "))
# detecting Single spaces
print(myStr.find(" "))
# replace double spaces with single spaces
print(myStr.replace("  ", " "))