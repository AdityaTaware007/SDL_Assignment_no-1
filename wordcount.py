file = open("C:/Users/Aditya/Downloads/Text.txt", "r")

d=dict()

for line in file:
    line=line.strip()
    line=line.lower()
    words=line.split(" ")
    for word in words:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1

print('Number of words in text file :', len(words))
for key in list(d.keys()):
    print(key,":",d[key])

