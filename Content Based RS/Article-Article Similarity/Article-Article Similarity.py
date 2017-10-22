# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals
from Tfidf_cs1 import Tf_cs
from Input_Article_Article import Input
import pickle 

c=Input()                           # c is object of class Input()
doc=[]                              # list doc[] will contain all articles
doc=c.clean_and_store()             # clean_and_store Tokenises and remove Stopwords & store all articles in lidt doc[]               
t=Tf_cs()                           # t is object of class Tf_cs
t.tf_idf(doc)                       #Calculate Tfidf
t.cs()                              #Calculate Cosine Similarity
p=pickle.load(open("Cosine_Similarity1.p","rb"))	# Comment Lines from 7-12 since pcikle is already created
print p