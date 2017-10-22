from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import pickle
import csv

class Tf_cs():
    def tf_idf(self,doc):                           #Calculate Tfidf
        vectorizer = TfidfVectorizer()
        tfidf_matrix=vectorizer.fit_transform(doc)
        pickle.dump(tfidf_matrix,open("Tfidf1.p","wb"))     # Stores tfidf( sparse matrix ) in tfidf1.p file
        
    def cs(self):                      #Calculate Cosine Similarity
        l1=[]
        l2=[]
        l3=[]
        tfidf_matrix=pickle.load(open("Tfidf1.p","rb"))
        file = open('myfile.csv','wb')
        writer = csv.writer(file)
        writer.writerow(['Article','Similar Article'])
        #Iterating all articles
        for i in range(2004):
            #Calculating Cosine Similarity
            cs_matrix=cosine_similarity(tfidf_matrix[i], tfidf_matrix)
            ls=cs_matrix[0].tolist()                    
            y=cs_matrix[0].tolist()
            ls.sort(reverse=True)               # Cosine Similarity in Decreasing Order in List ls
            for j in range(1,4):                # Find Top 3 similar Articles
                l1.append(i+1)                  # Article No.
                x=y.index(ls[j])
                l2.append(x+1)                  # Actual postion in unsorted list
                l3.append(ls[j])                # Cosine Similarity
                writer.writerow([i+1,x+1])
        df=pd.DataFrame({'Article':l1,'Similar Article':l2,'Cosine Similarity':l3},
                    columns=['Article','Similar Article','Cosine Similarity'])  
        pickle.dump(df,open("Cosine_Similarity1.p","wb"))