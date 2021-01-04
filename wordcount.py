import operator
#Read File
#Format "(file,action)"
file = open("","r")
text =file.read()
file.close()
#Count the words
words = {}
for word in text.split():
    if word.lower() in words:
        words[word.lower()]+=1
    else:
        words[word.lower()]=1
sorted_words = sorted(words.items(), key = operator.itemgetter(0))

#Write the countered numbers
file = open("","w")
file.write("Total words - {}\n Unique Words -{}\n \n ".format(len(text.split()),len(sorted_words)))
for wordinfo in sorted_words:
    file.write("{} - {} \n".format(wordinfo[0],wordinfo[1]))
file.close()
