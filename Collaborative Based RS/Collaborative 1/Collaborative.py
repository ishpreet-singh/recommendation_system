# Collaborative Filtering with 200 Users
# Uses Result from User-User Similarity
import pickle
from Tfidf_cs4 import Tf_cs
import time

start=time.time()
t=Tf_cs()                       # t is the object of Tf_cs 
no=200                          # No of  users Must be<=No of Users in User-User Similarity 
t.enter(no)                      
t.show(no)
df=pickle.load(open("Cosine_Similarity4.p","rb"))       #Storing the result in Cosine_Similarity4.p File
print df
df=pickle.load(open("Collaborative_Table2.p","rb"))     #Stroring the Frequency count of Users
print df
t.solve(no)
end=time.time()
#print end-start