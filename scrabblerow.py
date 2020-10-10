def author():
    return ""
def student_id():
    return ""
def fill_words(pattern,words,scoring_f,minlen,maxlen):
    fill=""
    highest=0
    # for letter in range (len(pattern)):
    #     for w in words:
    #         if pattern[letter] in w:
    #             if scoring_f(w) > highest:
    #                 fill=w
    #                 highest=scoring_f(w)
    return fill

def bestWord(pattern,words,scoring_f):
    
    
    
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
#
