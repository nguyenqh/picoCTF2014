import string
# initialize dictionary
letterdict = {}
for letter in string.ascii_lowercase:
    letterdict[letter] = 0

# count letter frequency    
f = open("encrypted.txt", 'r')
for line in f:    
    for word in line.split():
        for letter in word:            
            letterdict[letter] += 1
f.close()

total = sum(letterdict.values())

import operator
sortedbyfreq = sorted(letterdict.items(), key=operator.itemgetter(1), reverse=True)

for item in sortedbyfreq:
    print('{0} : {1:.4f}'.format(item[0], 1.0*item[1]/total))

# mapping letters for decryption
standardfreq = 'eotarsihnumfglywdbckvpqzjx'
lettermap = dict(zip([tup[0] for tup in sortedbyfreq],standardfreq))
print(lettermap)

# decrypt by substitution
fi = open("encrypted.txt", 'r')
fo = open("decrypted.txt", 'w')
for line in fi:
    newline=[]
    for word in line.split():
        newword=[]
        for letter in word:
            newword.append(lettermap[letter])
        newline.append(''.join(newword))
    newline.append('\n')
    #print(' '.join(newline))
    fo.write(' '.join(newline))
    
fi.close()
fo.close()

