alphabet = "abcdefghijklmnopqrstuvwxyz"

def author():
    return ""
def student_id():
    return ""
def fill_words(pattern,words,scoring_f,minlen,maxlen):
    highest=("",0)
    words_list=words
    word_idx=0
    letter_idx = 0
    currentRow=""
    
    #preprocessing
    wordTrie = Trie()
    for word in words:
        wordTrie.insert(word)
    
    
    possibleWords=[]
    
    patternCopy = pattern
    wordsCopy = words
    
    toConsider = ""
    
    #current issues:
    #NEED TO ACCOUNT FOR THE "-" AT THE END OF EACH POSSIBLE WORD
    #NEED TO CLOSE THE WHILE LOOP
    
    while len(patternCopy) >= 0:
        for w in words:
            while p in range(len(patternCopy)):
                if patternCopy[p] != "-" and patternCopy[p] != w[p]:
                    break
                if pattern[len(toConsider)] == "-":
                    toConsider = w
                
            if scoring_f(toConsider) > highest[1]:
                highest = (toConsider,scoring_f(toConsider))
        currentRow = highest[0] + pattern[len(highest[0]:)]
        
    #trial 1
    # for p in range(len(pattern)):
    #     if pattern[p] != "-":
    #         for w in words:
    #             if w[p] == pattern[p]:
    #                 possibleWords.append(w)
    #         words = possibleWords
    #         possibleWords=[]
    
    
    return build_word(pattern,wordTrie,scoring_f)
    # for letter_idx in range(len(pattern)):
    #     if pattern[letter_idx] == "-":
    #         for char in alphabet:
    #             currentWord+= char
    #             possibleWords = Trie.autoComplete(currentWord)
    #             for word in possibleWords:
    #                 if scoring_f(word) > highest[1]:
    #                     highest = (word,scoring_f(word))
                        
def build_word(pattern,wordTrie,scoring_f,currentWord="",possibleWords=[],highest=("",0)):
    if currentWord and not possibleWords :
        return None
    
    autocomplete=wordTrie.autoComplete(currentWord)
    
    for p in range(len(pattern)):
        if pattern[p] != "-":
            for w in autocomplete:
                if w[p] == pattern[p]:
                    possibleWords.append(w)
            autocomplete=possibleWords
    
    
    
    
    if pattern[0] == "-":
        for char in alphabet:
            currentWord+=char
            possibleWords = wordTrie.autoComplete(currentWord)
            
            
            
            
            
            
    else:
        currentWord+= pattern[0]
        
    possibleWords = wordTrie.autoComplete(currentWord)
    for word in possibleWords:
        currentWord=word
        currentScore = scoring_f(build_word(pattern[1:],wordTrie,scoring_f,currentWord,possibleWords))
        print(currentScore)
        if currentScore > highest[1]:
            highest = (currentWord,currentScore)
    return highest[0]


    # while word_idx < len(words_list):
    #     if scoring_f(words_list[letter_idx]) > highest:
    #         for letter_idx in range (len(pattern)):
    #             try:
    #                 #exception catching may not work for certain cases, like "-ahaaaaa-"
    #                 if pattern[letter_idx] == words[word_idx][letter_idx]:
    #                     #print(words[word_idx][letter_idx])
    #                     viableWords.append(words[word_idx])
    #                     #print(currentWord)
    #                 elif pattern[letter_idx] == "-":
    #                     #print("this happened")
    #                     continue
    #                 else:
    #                     viableWords.pop()
    #                     break
    #             except:
    #                 break
    #     #NOT RETURNING ANYTHING RIGHT NOW
    #     word_idx+=1
        
    for word_idx in range(len(words_list)):
        
        while letter_idx < 0:
            if pattern[letter_idx] == words[word_idx][letter_idx]:
                currentWord=words[word_idx]
            elif pattern[letter_idx] == "-":
                if scoring_f(currentWord) > highest:
                    print("do something")
            letter_idx -= 1
                
        # if pattern[letter_idx] != "-":
        #     try:
        #         if pattern[letter_idx] == words[word_idx][letter_idx]:
        #             toConsider = words[word_idx]
                    
        #     except:
        #         if scoring_f(toConsider) > highest:
        #             bestPattern = bestPattern + toConsider + "-"
    word_idx+=1
        
class Trie:
    def __init__(self):
        self.children = {}
        
    def insert(self, word):
        currentNode=self
        for letter in word:
            if letter in currentNode.children:
                currentNode = currentNode.children[letter]
            else:
                currentNode.children[letter]=Trie()
                currentNode=currentNode.children[letter]
        currentNode.children['#']=word

    def exists(self, word):
        if word == '':
            if self.isTerminal():
                return True
            return False
        if word[0] in self.children:
            return self.children[word[0]].exists(word[1:])
        return False
            

    def isTerminal(self):
        if '#' in self.children:
            return True
        return False

    def autoComplete(self, prefix):        
        toReturn=[]
        if self.isTerminal():
            terminalWord=self.children['#']
            if prefix == terminalWord[:len(prefix)]:
                toReturn+= [terminalWord]

        for key in self.children:
            if key != '#':
                toReturn+=self.children[key].autoComplete(prefix)
        #returns non-sorted list
        return toReturn
                
    def __len__(self):
        toReturn=0
        
        for key in self.children:
            if key == '#':
                toReturn+=1
            else:
                toReturn+=len(self.children[key])
        return toReturn

    

#what to do, roughly speaking
#begin with a greedy algorithm to maximize individual word score
#need to keep track of overall word score as guiding heuristic (alpha/beta pruning?)
#what constraints do we need to consider here???
#   min/max len word
#   
#USE AS MANY GIVEN LETTERS AS POSSIBLE TO CREATE WORDS
#ON FINDING COMPATIBLE WORDS, MEMO THEM
#essentially, ENUMERATE ALL POTENTIAL MOVE SEQUENCES
#perform a BFS, step through initial layer and explore possibilities

