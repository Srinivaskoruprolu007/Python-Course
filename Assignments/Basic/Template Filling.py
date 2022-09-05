# template filling
name = input("Enter your name >>")
date = input("Enter the date :")
template = '''
Dear <|name|> ,
you are selected
<|date|>
'''
print(template.replace('<|name|>', name).replace('<|date|>', date))
