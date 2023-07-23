text = open('zen.txt', 'r')
data = text.read()
text_conversely = []
for string in data.split('\n'):
    text_conversely.append(string)
print('\n'.join(text_conversely[::-1]))
text.close()
