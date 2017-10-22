 # -*- coding: utf-8 -*-
class Hindi_Tokenizer():
    
 def clean_text(self, text):
		'''working:)'''
		text1 = text
		text1 = text1.replace(u',','')
		text1 = text1.replace(u'"','')
		text1 = text1.replace(u'(','')
		text1 = text1.replace(u')','')
		text1 = text1.replace(u'``','')
		text1 = text1.replace(u':','')
		text1 = text1.replace(u"'",'')
		text1 = text1.replace(u"?",'')
		text1 = text1.replace(u"‘‘",'')
		text1 = text1.replace(u"‘",'')
		text1 = text1.replace(u"`",'')
		text1 = text1.replace(u"@",'')
		text1 = text1.replace(u"''",'')
		text1 = text1.replace(u".",'')
		text1 = text1.replace(u"\n",'')
		text1 = text1.replace(u'\u200c','')  #Half Space Symbol no representation
		text1 = text1.replace(u'\ufffd','')  #Special Symbol if not recognised by Compiler <?>
		text1 = text1.replace(u"/",' ')
		text1 = text1.replace(u"-",' ')
		text = text1
		return text
 
 def tokenize(self, text):
		'''done'''
		sentence = text.split(u"।")
		sentences_list=sentence
		tokens=[]
		for each in sentences_list:
			word_l = each.replace("\r\n"," ").split(" ")
			word_list = [i for i in word_l if not i == ''] 
			tokens += [i for i in word_list if i.isdigit() or len(i) not in [0,1]]
		
		return tokens