# User-User Similarity with 200 Users(Top 3)
# A step to Collaborative Similarity
from __future__ import division, unicode_literals
from Tfidf_cs3 import Tf_cs
from Input_User_User import Input
import pickle 
import time 

start=time.time()
c=Input()                       # c is object of class Input
doc=[]
doc=c.all_words(200)           # Number of Users
t=Tf_cs() 
t.tf_idf(doc)                   #Calculate Tfidf
t.cs(200)                      #Calculate Cosine Similarity for 2000 Users
p=pickle.load(open("Cosine_Similarity3.p","rb"))    #Storing results in Cosine_similarity3.p File
print p
end=time.time()
#print end-start