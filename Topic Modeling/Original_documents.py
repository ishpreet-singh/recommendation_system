import unicodecsv
import pickle

f=open('amarujaladb.csv')               #opening amarujaladb.csv which is the Database containg 2004 articles
csv_f = unicodecsv.reader(f)
next(csv_f)                             #Skip top two lines as they are blank
next(csv_f)
doc=[]
x=1
sen1=''
for row in csv_f:
    if int(row[0])==x:
        sen1+=row[5]+' '
    else:                                                       #Tokenizing
        doc.append(sen1)                                        #Appending each article in each row in doc
        x=int(row[0])
        sen1=''
        sen1+=row[5]+' '
if len(doc)==2003:
    doc.append(sen1)
pickle.dump(doc,open("Original_Document.p","wb"))