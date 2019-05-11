#Cleaning Data Manually

#load text
fiename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

#Tokenization
#(i) Split by whitespaces
#problems: "wasn't" "dream." "room," - punctuations still there
#words = text.split()
#print(words[:100])

#(ii) Split by words
#problems: "wasn" "t" - you lost your word!!
#import re
#words = re.split(r'\W+', text)
#print(words[:100])

#(iii) split by whitespaces and remove punctuations
#problem solved as: "wasnt"
import string
table = str.maketrans('','',string.pinctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:100])

#Capitalization
# split into words by white space
#words = text.split()
# convert to lower case
#words = [word.lower() for word in words]
#print(words[:100])

