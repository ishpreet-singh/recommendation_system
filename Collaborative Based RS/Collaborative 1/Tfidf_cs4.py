from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import random
import pandas as pd

class Tf_cs():
    def __init__(self):                             # All List that will be used in Program
        self.l1=[]
        self.l2=[]
        self.l3=[]
        self.user_articles=[]  
        self.user_ids=[]
        
    def tf_idf(self,doc):                           #Calculate Tfidf
        vectorizer = TfidfVectorizer()
        tfidf_matrix=vectorizer.fit_transform(doc)
        pickle.dump(tfidf_matrix,open("Tfidf4.p","wb")) 
        
    def cs(self,pos,i):                      #Calculate Cosine Similarity
        tfidf_matrix=pickle.load(open("Tfidf4.p","rb"))
        cs_matrix=cosine_similarity(tfidf_matrix[pos], tfidf_matrix)
        ls=cs_matrix[0].tolist()                    
        y=cs_matrix[0].tolist()
        ls.sort(reverse=True)               # Cosine Similarity in Decreasing Order in List ls
        for j in range(1,4):
            self.l1.append(i+1)                  # User No.
            x=y.index(ls[j])
            self.l2.append(x+1)                  # Actual postion in unsorted list
            self.l3.append(ls[j])                # Cosine Similarity
            
    def insert(self,u):
        p=pickle.load(open("Cosine_Similarity3.p","rb"))
        d=pickle.load(open("Document.p","rb"))
        sen=''
        for j in range(3):
            x=int(p.loc[3*u+j][1])          
            self.user_articles.append(x)        #Articles of Each Users
            self.user_ids.append(u+1)             #User Id is the User No.
            sen+=d[x-1]+' '
        
        for k in range(3):
            ne=int(p.loc[3*u+k][2])             #Neighbours of each User
            for j in range(3):
                x=int(p.loc[(ne-1)*3+j][1])      
                self.user_articles.append(x)    # Articles of each Neighbour
                self.user_ids.append(ne)        # User No of each Neighbour
                sen+=d[x-1]+' '
        a=random.randint(1,2000)            # Appeding Random Article
        sen+=d[a]+' '
        self.user_articles.append(a)
        self.user_ids.append(0)             # For Random Article the User Id is 0
        d.append(sen)   
        return d
    
    def enter(self,total):
        for u in range(total):          # Iterating all 200 Users
            d=self.insert(u)
            self.tf_idf(d)
            self.cs(len(d)-1,u)
            
        df=pd.DataFrame({'User':self.l1,'Similar Article':self.l2,'Cosine Similarity':self.l3},
                    columns=['User','Similar Article','Cosine Similarity'])  
        pickle.dump(df,open("Cosine_Similarity4.p","wb"))
        
    def show(self,total):               # Table 2 
        l4=[]
        for i in range(total):
            for j in range(13):
                l4.append(i+1)
        ds=pd.DataFrame({'User':l4,'Articles':self.user_articles,'User Ids':self.user_ids},
                        columns=['User','Articles','User Ids'])
        pickle.dump(ds,open("Collaborative_Table2.p","wb"))
        
    def solve(self,no):
        p=pickle.load(open("Cosine_Similarity4.p","rb"))
        q=pickle.load(open("Cosine_Similarity2.p","rb"))
        count=0
        for i in range(no):
            co=0
            for j in range(3):
                x=int(p.loc[3*i+j][1])
                for k in range(3):
                    if(int(q.loc[3*i+k][1])==x):
                        co+=1
            if co==3:
                count+=1
        #print count
    