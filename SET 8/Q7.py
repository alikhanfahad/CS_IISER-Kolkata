stop=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#sentence=str(input("Enter the sentence:"))

#string = input()

#for letter in string:
 #   if letter.isupper():
  #      string = string.replace(letter, "_" + letter.lower())
#print(string)

#str_list = ["Python", "is", "fun"]
#delimiter = " " # Define a delimiter
#join_str = delimiter.join(str_list)

#def censor(text, word):
 #   lex = text.split()
  #  for i in range(len(lex)):
   #     if lex[i] == word:
    #        lex[i] = ('*' * len(word))
    #return ' '.join(lex)
    
doc1 ="Information Retrieval is the science of search engines" 
doc2 ="This is the age of information technology"
doc3 ="Mathematics in the language of science"
doc4 ="Efficient retrieval of important data is the feature of any sound search system."
doc5 ="Gerard Salton is the father of Information Retrieval"
    
def preprocess(sentence):
   
    for x in range(len(sentence)):
        if sentence[x].isupper():
            sentence=sentence.replace(sentence[x],sentence[x].lower())
            
    splited_sentence=sentence.split()
    
    for x in range(len(splited_sentence)):
         if splited_sentence[x] in stop:
             splited_sentence[x]=''
    ref_sen=" ".join(splited_sentence)
        
    return ref_sen
    
#sentenced=preprocess(sentence)
doc1_p=preprocess(doc1)
doc2_p=preprocess(doc2)
doc3_p=preprocess(doc3)
doc4_p=preprocess(doc4)
doc5_p=preprocess(doc5)
#print(doc5_p)
#print(sentenced)
q=str(input("Enter Query String:"))
q=preprocess(q)

splited_q=q.split()
doc1_split=doc1_p.split()
doc2_split=doc2_p.split()
doc3_split=doc3_p.split()
doc4_split=doc4_p.split()
doc5_split=doc5_p.split()
#print(doc5_split)
#for y in range(len(splited_q)):
 #   if splited_q[y] in doc1_split:
  #     print("doc1")
   #    break
#for y in range(len(splited_q)):
 #   if splited_q[y] in doc2_split:
  #     print("doc2")
   #    break
#for y in range(len(splited_q)):
 #   if splited_q[y] in doc3_split:
  #     print("doc3")
   #    break
#for y in range(len(splited_q)):
 #   if splited_q[y] in doc4_split:
  #     print("doc4")
   #    break
#for y in range(len(splited_q)):
 #   if splited_q[y] in doc5_split:
  #     print("doc5")
   #    break
   # else:
    #   print("Not even a single word of q in any document")
count1=0 
for y in range(len(splited_q)):      
   if splited_q[y] in doc1_split:
      count1+=1
   #if count1==len(splited_q):   
    #  print("doc1")
count2=0 
for y in range(len(splited_q)):       
   if splited_q[y] in doc2_split:
      count2+=1
   #if count2==len(splited_q):   
    #  print("doc2")
count3=0 
for y in range(len(splited_q)):     
   if splited_q[y] in doc3_split:
      count3+=1
   #if count3==len(splited_q):   
    #  print("doc3")
count4=0 
for y in range(len(splited_q)):
   if splited_q[y] in doc4_split:
      count4+=1
   #if count4==len(splited_q):   
    #  print("doc4")
count5=0 
for y in range(len(splited_q)): 
   if splited_q[y] in doc5_split:
      count5+=1
   #if count5==len(splited_q):   
    #  print("doc5")

z={'doc1':count1,'doc2':count2,'doc3':count3,'doc4':count4,'doc5':count5}
z_sorted=dict(sorted(z.items(),key=lambda item:item[1],reverse=True))
answer=list(z_sorted.keys())
for answeri in answer:
    print(answeri,"\n")
