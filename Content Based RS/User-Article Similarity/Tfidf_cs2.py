from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle
import random

class Tf_cs():
    def __init__(self):                         # Defining All the List used in Program
        self.l1=[]  
        self.l2=[]
        self.l3=[]
        self.l4=[]
        self.l5=[]
        
    def gen(self,no):                           # Generating 3 Random Articles for each User
        for i in range(no):                     # List L4 contains all random articles for No. users
            for j in range(3):
                x=random.randint(0,2004)
                self.l4.append(x)               # 0 indexing
        
    def input(self,x):                          # Appending the new article(user attribute) in original Articles
        d=pickle.load(open("Document.p","rb"))  # Article X Article  
        sen=''
        for i in range(3*x,3*x+3):
            sen+=d[self.l4[i]]+' '
        d.append(sen)
        return d                                # ALl articles + User's attribute(at last)
        
    def tf_idf(self,doc):                           #Calculate Tfidf
        vectorizer = TfidfVectorizer()
        tfidf_matrix=vectorizer.fit_transform(doc)
        pickle.dump(tfidf_matrix,open("Tfidf2.p","wb")) 
        
    def cs(self,x,y):                                       #Calculate Cosine Similarity
        tfidf_matrix=pickle.load(open("Tfidf2.p","rb"))
        cs_matrix=cosine_similarity(tfidf_matrix[x], tfidf_matrix)  # x is the last article id Doc(User attribute)
        ls=cs_matrix[0].tolist()                        # Converting Sparse Matrix into List
        z=cs_matrix[0].tolist()
        ls.sort(reverse=True)                           # ls contains Cosine Similarities in Decreasing Order
        for j in range(1,4):
            self.l1.append(y+1)                           # y is User No
            a=z.index(ls[j])                            # Artile No of Nth Similar Article
            self.l2.append(a+1)                         # O->1 Indexing
            self.l3.append(ls[j])                       # Cosine Similarity of Nth Similar Article
            self.l5.append(self.l4[3*y+j-1]+1)      # Article present in User Attribute
        
    def ans(self):
        df=pd.DataFrame({'Users':self.l1,'Articles':self.l5,'Similar Articles':self.l2,'Cosine Similarity':self.l3},
                    columns=['Users','Articles','Similar Articles','Cosine Similarity'])
                    
        return df