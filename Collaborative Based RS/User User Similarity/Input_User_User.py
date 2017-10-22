import pickle

class Input():
    def all_words(self,no):        
        d=pickle.load(open("Document.p","rb"))                      # All Artclies are stored in Document.p File
        p=pickle.load(open("Cosine_Similarity2.p","rb"))              # Fetching Users from User-Article
        doc=[]
        ls=[]
        for k in range(no):                                         # Iterating for each User
            sen=''
            for i in range(3):
                a=int(p.loc[3*k+i][1])                              # Second Column in Table CosineSimilarity2.p
                ls.append(a)                                        #       contains Aricle of each User
                sen+=d[a-1]+' '
            doc.append(sen)                                         #doc conatins all articles of each user
        pickle.dump(ls,open("Users_Docs.p","wb"))                   # Users_Docs.p File contains list of Articles
        return doc                                                  #           of each User