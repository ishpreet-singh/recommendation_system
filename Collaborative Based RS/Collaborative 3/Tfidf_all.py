#Analysis:  User Profile: 3 Articles + Neighbour + 1 Random Article per Neighbour(Maximim Neighbour is 5)
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from operator import itemgetter
import pandas as pd
import pickle
import random

class Tf_cs():
    def __init__(self):
        self.doc_all=[]                         
        self.all_articles=[]                    # Contains ALl articles
        self.users=[]                           # User Id/Number
        self.random_articles=[]                 # Articles No. of Random Article for each Neighbour
        self.user_articles=[]                   # Articles No. of each User
        self.neighbour_articles=[]              # Articles No. of each neighbour
        self.neighbour_count=[]                 # Returns Count of neighbours of each User
        self.article_count=[]                   # Count of Article of each User Profile        
        self.count_u=[0]*6                      # Count of User based on Neighbours
        self.articles_from_neighbours=[]        # Articles from Neighbours in Recommendation from Neighbours
    
    def tf_idf(self,doc):                           #Calculate Tfidf
        vectorizer = TfidfVectorizer()
        tfidf_matrix=vectorizer.fit_transform(doc)
        pickle.dump(tfidf_matrix,open("Tfidf_all.p","wb")) 
        
    def cs(self,r):                      #Calculate Cosine Similarity
        i=0                              #Reduce Count
        l1=[]
        l2=[]
        l3=[]
        tfidf_matrix=pickle.load(open("Tfidf_all.p","rb"))
        for i in range(r):                              # Itereating to all Users(r)
            cs_matrix=cosine_similarity(tfidf_matrix[i], tfidf_matrix)  # Calculting Cosine Similarity
            ls=cs_matrix[0].tolist()                    
            y=cs_matrix[0].tolist()
            ls.sort(reverse=True)               # Cosine Similarity in Decreasing Order in List ls
            j=1
            count=0
            max_neighbour_count=5               # max_neighbour_count is the count of Maximum Neighbours a user can have  
            while(ls[j]>0.20 and count<max_neighbour_count):      
                l1.append(i+1)                  # User No.
                x=y.index(ls[j])
                l2.append(x+1)                  # Actual postion in unsorted list
                l3.append(ls[j])                # Cosine Similarity
                j=j+1
                count=count+1
            
        df=pd.DataFrame({'User':l1,'Similar User':l2,'Cosine Similarity':l3},
                    columns=['User','Similar User','Cosine Similarity'])  
        pickle.dump(df,open("Cosine_Similarity_all.p","wb"))
        
    def cs_i(self):                     #Calculate Cosine Similarity
        l1=[]
        l2=[]
        l3=[]
        for i in range(len(self.doc_all)):                      # Itereating to all Users(r)
            d=[]
            d=pickle.load(open("Document.p","rb"))
            sen=''                                              # sen is a string contains all articles
            sen+=self.doc_all[i]+' '
            d.append(sen)
            vectorizer = TfidfVectorizer()
            tfidf_matrix=vectorizer.fit_transform(d)
            cs_matrix=cosine_similarity(tfidf_matrix[len(d)-1], tfidf_matrix)  # Calculting Cosine Similarity
            ls=cs_matrix[0].tolist()                    
            y=cs_matrix[0].tolist()
            ls.sort(reverse=True)               # Cosine Similarity in Decreasing Order in List ls
            for j in range(1,4):                # Fetching Top 3 Similar Users
                l1.append(self.users[i])                  # User No.
                x=y.index(ls[j])
                l2.append(x+1)                  # Actual postion in unsorted list
                l3.append(ls[j])                # Cosine Similarity
                
        df=pd.DataFrame({'User':l1,'Similar Articles':l2,'Cosine Similarity':l3,'Random Articles':self.random_articles},
                    columns=['User','Similar Articles','Cosine Similarity','Random Articles'])  
        pickle.dump(df,open("Cosine_Similarity_in_one.p","wb"))
        
    def analysis(self):                         # main function of program 
        p=pickle.load(open("Cosine_Similarity_all.p","rb"))
        q=pickle.load(open("Input_All.p","rb"))
        d=pickle.load(open("Document.p","rb"))
        k=0
        while (k<int(len(p))):                      
            sen=''
            y=0
            z=random.randint(1,2003)                # Random Article
            c=0
            u=int(p.loc[k][0])
            for i in range(3):
                a=int(q[3*(u-1)+i])                 # Article of User(3)
                self.all_articles.append(a)
                self.user_articles.append(a)
                sen+=d[a-1]+' '
            i=k
            c=c+1
            x=int(p.loc[k][0])                      # Iterating over the same articles
            f=0
            while (i<len(p) and int(p.loc[i][0])==x ):      # Iterating all neighbours of each user
                if f==0:
                    self.users.append(x)
                    f=f+1
                u=int(p.loc[i][1])               # Neighbour
                for j in range(3):
                    a=int(q[3*(u-1)+j])           
                    self.neighbour_articles.append(a)   # Appending Articles from Neighbour
                    self.all_articles.append(a)
                    sen+=d[a-1]+' '
                    c=c+1
                sen+=d[z-1]+' '
                self.all_articles.append(z)         #Appending 1 random article per neighbour
                y=y+1
                c=c+1
                i=i+1
            k=max(k+1,i)
            self.neighbour_count.append(y)      
            self.article_count.append(c)
            for i in range(3):
                self.random_articles.append(z)
            self.doc_all.append(sen)

    def count_users(self,no):                       # To calculate count_u
        total=0                                     # count_u returns count of users with sepcific neighbours 0-5
        for i in range(1,6):
            for j in range(len(self.neighbour_count)):
                if self.neighbour_count[j]==i:
                    self.count_u[i]+=1
            total+=self.count_u[i]
        self.count_u[0]=no-total                    # count_u[0] is count of user with 0 neighbours
        print self.count_u
         
    def random_recommendation(self,y):
        p=pickle.load(open("Cosine_Similarity_in_one.p","rb"))
        count=0
        for i in range(len(self.article_count)):
            r=int(p.loc[3*i][3])                    # Random Article
            for j in range(3):
                a=int(p.loc[3*i+j][1])              # Top 3 Similar Articles of User
                if a==r and self.neighbour_count[i]==y:
                    count=count+1
                    break
        print 'Percentage of Random Recommendation ',y,' :',((count*100.0)/(self.count_u[y]))
        
    def extra_recommendation(self,y):                  
        p=pickle.load(open("Cosine_Similarity_in_one.p","rb"))
        count=0
        s=0
        for k in range(len(self.article_count)):
            i=self.article_count[k]
            s=s+i
            for l in range(3):
                a=p.loc[3*k+l][1]               # Article
                f=False
                for j in range(s-i,s):          # For each article in user,neighbour,random
                    if a==self.all_articles[j] and self.neighbour_count[k]==y:
                        f=True
                        break
                if f==True:
                    count+=1
                    break
        print 'Percentage of Extra Recommendation ',y,' :',((count*100.0)/(self.count_u[y]))
        
    def recommendation_from_neighbours(self):
        p=pickle.load(open("Cosine_Similarity_all.p","rb"))
        c=p['Cosine Similarity'].tolist()
        u=[]
        cs_from_neighbours=[]
        t=0
        for i in range(len(self.users)):            # Iterating all users  
            x=self.neighbour_count[i]
            t+=x
            d={}
            for l in range(t-x,t):            # Iterating all Neighbours
                cs=c[l]                             # Fetching Cosine Similarity of Each Neighbour
                for j in range(l*3,(l+1)*3):        # Iterating all articles of Neighbours
                    n=self.neighbour_articles[j]   
                    d[n]=0                          # Setting CS of Each article=0
                    f=0
                    for k in range(3*i,3*(i+1)):    # Comparing Neighbour Articles with user one
                        if n==self.user_articles[k]:
                            f=f+1
                            break
                    if f==0:                        # If Neighbour article is not present in User List Increse its weight 
                        d[n]+=cs
            ls=sorted(d.items(),key=itemgetter(1),reverse=True)
            for j in range(3):
                u.append(self.users[i])
                self.articles_from_neighbours.append(ls[j][0])
                cs_from_neighbours.append(ls[j][1])
        df=pd.DataFrame({'Users':u,'Articles from Neighbours':self.articles_from_neighbours,'Cosine Similarity':cs_from_neighbours},
                        columns=['Users','Articles from Neighbours','Cosine Similarity'])
        pickle.dump(df,open("Articles_from_Neighbour.p","wb"))
