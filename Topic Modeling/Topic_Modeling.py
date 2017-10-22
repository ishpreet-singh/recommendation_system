# Topic Modeling using LDA and Collapsed Gibbs sampling
import operator
import numpy as np
import lda
import pickle
import time
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from Input_Topic_Modeling import Input

start=time.time()
# Defining the vocabulary(vocab)
st=['=','_','+','-','*','/','!','@','#','$','%','^','[',']','/','{','}']
s=[]
article_id=[]
topic_id=[]
topic_id2=[]
topic_w=[]
topic_weight=[]
word_weight=[]
s1=[]                                    # list s[] will contain all words from each article in hindi only
t=Input()
d=pickle.load(open("Original_Document.p","rb"))
stop=stopwords.words('english')         # list of stopwords in english
p=t.clean_and_store()
for i in range(len(p)):                 # s -> clean words
    s=[x.encode('utf-8') for x in p[i].split() if x not in stop and x not in st and (x.isdigit() or x.isalpha() or x.isalnum())==False]  
    for word in s:
        f=0
        for char in word:
            if char in st:
                f=1
                break
        if f==0:
            s1.append(word)
vocab=tuple(set(s1))                     # vocab -> Vocabulary of all words        

# Calculating Document term matrix(X)
vectorizer = CountVectorizer(stop_words='english')      
tf_matrix=vectorizer.fit_transform(p)   
X=tf_matrix.toarray()                   # X -> Document term matrix 

# Fitting the LDA
model = lda.LDA(n_topics=30, n_iter=1500, random_state=1) 
model.fit(X)                            # Learn a vocabulary dictionary of all tokens in arr

# Defining topic_word
topic_word = model.topic_word_          # narray of Shape: n_topics*vocab

# Predicting most similar Topics
doc_topic = model.doc_topic_            # doc_topic size(2004*10)-> distribution over the 10 topics for each of the 2004 articles
for n in range(len(p)):
    dic={}
    for i in range(30):                 # ***Enter No of Topic here***
        dic.update({i:doc_topic[n][i]})
    e=sorted(dic.items(),key=operator.itemgetter(1),reverse=True)   # Sorting the topics in decreasing order
    for i in range(3): 
        article_id.append(n+1)          # Appending article id
        x=e[i][0]                       # Fetching the ith most similar topic
        topic_id.append(x)              # Topic id
        topic_weight.append(e[i][1])    # Topic Weight
        
for i in range(30):
    y=[]
    y=sorted(topic_word[i],reverse=True)
    word=np.array(vocab)[np.argsort(topic_word[i])][:-6:-1]
    for j in range(5):
        topic_id2.append(i)             # Topic Id
        word_weight.append(y[j])        # Word Weight
        topic_w.append(word[j])            # Word
        
df=pd.DataFrame({'Article Id':article_id,'Topic Id':topic_id,'Topic Weight':topic_weight},
                columns=['Article Id','Topic Id','Topic Weight']) 
pickle.dump(df,open("Output_Topic_Modeling1.p","wb"))
df.to_csv("Output_Topic_Modeling1.csv")
df=pd.DataFrame({'Topic Id':topic_id2,'Word':word_weight,'Weight':topic_w},
                columns=['Topic Id','Word','Weight'])
pickle.dump(df,open("Output_Topic_Modeling2.p","wb"))
df.to_csv("Output_Topic_Modeling2.csv")
end=time.time()
print 'Time:',end-start