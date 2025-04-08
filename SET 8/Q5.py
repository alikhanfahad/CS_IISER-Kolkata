stop=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
sentence=str(input("Enter the sentence:"))

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

sentenced=preprocess(sentence)
print(sentenced)
