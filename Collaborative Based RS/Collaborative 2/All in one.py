# User-User Similarity with 200 Users(Top 3)
from __future__ import division, unicode_literals
from Tfidf_all import Tf_cs
from Input_All import Input
import pickle 
import time 

start=time.time()
c=Input()                       # c is object of class Input
no=200                          # Number of Users
doc=c.all_words(no)           
t=Tf_cs() 
t.tf_idf(doc)                   #Calculate Tfidf
t.cs(no)                      #Calculate Cosine Similarity for 2000 Users
t.analysis()
t.cs_i()
p=pickle.load(open("Cosine_Similarity_all.p","rb"))    
#print p
p=pickle.load(open("Cosine_Similarity_in_one.p","rb"))    
print p
t.count_users(no)
for i in range(1,6):
    t.random_recommendation(i)
    t.extra_recommendation(i)
end=time.time()
#print end-start