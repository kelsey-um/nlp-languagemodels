def ngram(text, n): #n is size of ngrams

    ngramCounts = {} #dict to store ngrams

    for i in range(len(text)-n+1): #len(text)-n+1 is the number of all possible ngrams

        ngram = tuple(text[i:i+n]) #creates ngram

        if ngram in ngramCounts: #check to see if it already exists
            ngramCounts[ngram] += 1
        else:
            ngramCounts[ngram] = 1

    return ngramCounts

def TriGramProbabilties(ngrams):

    ngramProbs = {}
    
    for x in ngrams:
        
        count = 0
        prefix = x[:-1] # getting each element from first to second to last

        for ngram in ngrams:
            
            if prefix in zip(ngram, ngram[1:]):
                count += 1
            
        probability = ngrams[x]/count
        ngramProbs[x] = probability
        

    return ngramProbs



teststring = '<s> I am Sam </s> <s> Sam I am </s> <s> I do not like green eggs and ham </s>'
testlist = list(teststring.split(" "))

output = TriGramProbabilties(ngram(testlist,3))

print(output)