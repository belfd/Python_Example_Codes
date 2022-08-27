words = ['PYTHON','is','NOT','an','easy','language']
sentence = " ".join(filter(lambda x:x!='NOT',words))
#above will filter 'NOT' from words and join with spaces
print(sentence) # output: PYTHON is an easy language