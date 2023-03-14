L=int(input())
sent=input()
sent=sent.split(' ')
length=0
word=""
for i in sent:
    if len(i)>length:
        length=len(i)
        word=i
print (word)
print (length)
    
