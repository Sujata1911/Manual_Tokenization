#load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#splits on words only
#armour-like will be 2 words : armour, like (its okay)
#What's is not What, s (not great)
import re
words = re.split(r'\W+', text)
print(words[:100])

