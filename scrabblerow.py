alphabet = "abcdefghijklmnopqrstuvwxyz"

def author():
    return ""
def student_id():
    return ""
def fill_words(pattern,words,scoring_f,minlen,maxlen):
    
    
    
    return find_words(pattern,words,scoring_f,minlen,maxlen)

def find_words(pattern,words,scoring_f,minlen,maxlen):
    patternCopy = pattern
    bestWord=("",0)
    bestState=[("",0),[],[]]
    toConsider = ""
    possibleWords=[]
    length = minlen
    wordDict = {}
    beg_point = 0
    states = []
    position=(0,0)
    
    
    if len(pattern) == 0:
        #NEED TO SET A BASE CASE
        return ""
    
    for w in words:
        if len(w) in wordDict:
            wordDict[len(w)] += [w]
        else:
            wordDict[len(w)] = [w]
    
    while len(patternCopy) > 1:
        if length in wordDict:
            for w in wordDict[length]:
                snip = patternCopy[:length]
                for p in range(len(snip)):
                    if patternCopy[p] != "-" and patternCopy[p] != w[p]:
                        toConsider = ""
                        break
                    toConsider = w
                try:
                    if patternCopy[len(toConsider)] == "-" and toConsider != "" and toConsider not in possibleWords:
                        if scoring_f(toConsider) > bestWord[1]:
                            bestWord = (toConsider, scoring_f(toConsider))
                except:
                    break
        if length == maxlen:
            patternCopy = patternCopy[1:]

            leftHalf =  pattern[:beg_point]
            rightHalf = pattern[len(leftHalf) + len(bestWord[0]):]
            beg_point += 1
            
            if len(leftHalf) > 0 and leftHalf[-1] == "-":
                states.append([bestWord,leftHalf,rightHalf])

            bestWord = ("",0)
            length = minlen
        length+=1

    for s in states:
        if s[0][1] > bestState[0][1]:
            bestState = s
            
    leftState = fill_words(bestState[1],words,scoring_f,minlen,maxlen)
    rightState = fill_words(bestState[2],words,scoring_f,minlen,maxlen)
    #print(leftState,rightState)
    return leftState + bestState[0][0] + rightState

minlen, maxlen = 4, 30
letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

# Dictionary used to count the frequency of each letter.

letter_counts = {c: 0 for c in letter_values}

with open('words_sorted.txt', 'r', encoding='utf-8') as f:
    words = [x.strip() for x in f]
    words = [x for x in words if minlen <= len(x) <= maxlen]
    wordset = set(words)
    for word in words:
        for c in word:
            letter_counts[c] += 1
            
def scrabble_value(word):
    if minlen <= len(word) <= maxlen:
        return sum(letter_values.get(c, 0) for c in word)
    else:
        return 0

def length_squared(word):
    if minlen <= len(word) <= maxlen:
        return len(word) ** 2
    else:
        return 0
    
def scoring_f(w):
    return length_squared(w) + scrabble_value(w)

pattern = "-l-h--i-o--w--s--u--g-d-u-n-c-c--b--c-t-"

print(pattern)
print(fill_words(pattern,words,scoring_f,minlen,maxlen))