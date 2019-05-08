#load data
filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
#split into words by whitespace
words = text.split()
print(words[:100])
