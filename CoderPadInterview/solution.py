# We are given a corpus and a target sequence. We want to find the first minimal (shortest) substring in the corpus, which contains all of the characters from the target sequence. Order does not matter but characters in the target sequence may appear multiple times. Assume a valid string input for the target and corpus.

# Basic cases
# assert min_substring("abc", "abc") == "abc"
# assert min_substring("a", "abc") == "a"

# # Substring in the middle of the corpus
# assert min_substring("abc", "aaaaaabbcccccc") == "abbc"

# # No match case
# assert min_substring("abc", "bbcccccc") == ""

# # Out of order case
# assert min_substring("abc", "aabbccab") == "cab"

# # First match found case
# assert min_substring("abc", "aabbccabc") == "cab"

# # Extra cases
# assert min_substring("aab", "abbbbbbbbba") == "abbbbbbbbba"
# assert min_substring("aabc", "abbbbbccccca") == "abbbbbccccca"

#iterate corpus letter by letter
#dictionary of target {"letter": numLetters}
#have to iterate whole string
#outputlist of all possibles

def isValid(targetDict, targetCheck):
    for key in targetDict.keys():
        if key in targetCheck.keys():
            if targetCheck[key] < targetDict[key]:
                return False
        else:
            return False
    return True


def substringGrab(corpus: str, target: str):
    #populate target dictionary
    targetDict = {}
    for letter in target:
        if letter in targetDict.keys():
            targetDict[letter] += 1
        else:
            targetDict[letter] = 1
    
    outputList = []
    #iterate over corpus
    targetCheck = {}
    start = 0
    finish = 0
    for letter in corpus:
        if letter in targetDict.keys():
            if letter in targetCheck.keys():
                targetCheck[letter] += 1
            else:
                targetCheck[letter] = 1
            if isValid(targetDict, targetCheck):
                return "".join()
            
        else:
            targetCheck = {}

print(substringGrab("abbbbbbbbba", "aab"))
# 1. expand the window (end)
    # update your target check
    # have I found a valid substring (targetDict, targetCheck) -> bool
        # can I shrink this
    # go on
#