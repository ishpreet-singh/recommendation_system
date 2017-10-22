# User Article Similarity with 200 Users
import pandas as pd
import pickle
from Tfidf_cs2 import Tf_cs

t=Tf_cs()
df=pd.DataFrame(columns=['Users','Articles','Similar Articles','Cosine Similarity'])
t.gen(200)
for user in range(200):       # 200 Users:)
    d=''
    d=t.input(user)             # Defining User attributs i.e. 3 Random articles
    t.tf_idf(d)                 # It's Tfidf Calculation
    ds=t.cs(len(d)-1,user)      # Cosine similarity Calculation of only the last article(user attributes)
df=t.ans()                      # Returing the DataFrame
pickle.dump(df,open("Cosine_Similarity2.p","wb"))   # Saving the result in Cosine_Similarity2 pickle file
print df