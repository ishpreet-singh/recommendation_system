from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle

class Tf_cs():
    def tf_idf(self,doc):                           #Calculate Tfidf
        vectorizer = TfidfVectorizer()
        tfidf_matrix=vectorizer.fit_transform(doc)
        pickle.dump(tfidf_matrix,open("Tfidf3.p","wb")) 
        
    def cs(self,r):                      #Calculate Cosine Similarity
        i=0
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        z=0
        tfidf_matrix=pickle.load(open("Tfidf3.p","rb"))
        d=pickle.load(open("Users_Docs.p","rb"))
        for i in range(r):                              # Itereating to all Users(r)
            cs_matrix=cosine_similarity(tfidf_matrix[i], tfidf_matrix)  # Calculting Cosine Similarity
            ls=cs_matrix[0].tolist()                    
            y=cs_matrix[0].tolist()
            ls.sort(reverse=True)               # Cosine Similarity in Decreasing Order in List ls
            for j in range(1,4):                # Fetching Top 3 Similar Users
                l1.append(i+1)                  # User No.
                x=y.index(ls[j])
                l2.append(x+1)                  # Actual postion in unsorted list
                l3.append(ls[j])                # Cosine Similarity
                l4.append(d[z+j-1])             # Articles of each User
            z=z+3
            
        df=pd.DataFrame({'User':l1,'Article':l4,'Similar User':l2,'Cosine Similarity':l3},
                    columns=['User','Article','Similar User','Cosine Similarity'])  
        pickle.dump(df,open("Cosine_Similarity3.p","wb"))
        #print df