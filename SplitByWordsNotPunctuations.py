#load text
filename = 'metamorphosis_clean.txt'
file = open(filename,'rt')
text = file.read()
file.close()

#split file into words by whitespaces
words = text.split()

#remove punctuation from each word
import string
table = str.maketrans('','',string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])
