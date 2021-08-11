

book={}
f2=open("C:\\Python\\Code\\jsonbook.txt","w")
book['Tom']={'name':'tom','address': 'qa1-34 sfde sds'}
book['rose']={'name':'rose','address':'qe1-4 sds 45e'}

print(book)
import json
s = json.dumps(book)
print(s)
print(type(book))
print(type(s))
f2.write(s)
