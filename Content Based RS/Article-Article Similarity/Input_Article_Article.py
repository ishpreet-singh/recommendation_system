# Tokenizing and Cleaning
import unicodecsv
from Tokenise import Hindi_Tokenizer
import pickle

class Input():
    def clean_and_store(self):                        #defining Hindi Stopwords
        sw=[]
        fl=open('stopwords.csv')
        csv_f = unicodecsv.reader(fl,encoding='utf-8')
        for row in csv_f:
            sw.append(row[0])
        
        f=open('amarujaladb.csv')               #opening amarujaladb.csv which is the Database containg 2004 articles
        csv_f = unicodecsv.reader(f)
        next(csv_f)                             #Skip top two lines as they are blank
        next(csv_f)
        t = Hindi_Tokenizer()
        doc=[]
        x=1
        sen1=''
        for row in csv_f:
            if int(row[0])==x:
                sen1+=row[5]+' '
            else:                                                       #Tokenizing
                A_text = t.clean_text(sen1)                 
                A_tokens = t.tokenize(A_text)
                
                sen3=[word for word in A_tokens if word not in sw]      #Stopword Removal 
                sen4=' '.join(sen3)
                doc.append(sen4)                                        #Appending each article in each row in doc
                x=int(row[0])
                sen1=''
                sen1+=row[5]+' '
        
        A_text = t.clean_text(sen1)                                     # Again Tokenizing                 
        A_tokens = t.tokenize(A_text)
        
        sen3=[word for word in A_tokens if word not in sw]              # Again Stopword Removal 
        sen4=' '.join(sen3)
        doc.append(sen4)                                                # doc is list of Strings(Articles)
        pickle.dump(doc,open("Document.p","wb"))                        # Documents.p File contains all articles(2004)   
        return doc
