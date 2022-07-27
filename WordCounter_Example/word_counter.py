import os

from pyparsing import empty

currDirectory = os.getcwd()

def wordCounter(file: str):
    inputFile = file
    #check if file exists
    if not os.path.exists(inputFile):
        return None

    #set up output
    outputFile = os.path.join(currDirectory, "WordCounter_Example", "Outputs", file.split('\\')[-1])

    if os.path.exists(outputFile):
        os.remove(outputFile)

    wordDict = {} # {"word":"wordCount"}

    #read in test file
    with open(inputFile, "r") as iFile:
        for line in iFile:
            words = line.split(' ')
            for word in words:
                word = word.strip()
                if not word:
                    continue
                if word in wordDict.keys():
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
    
    outputLines = []
    for key in sorted(wordDict):
        outputLines.append(key + " " + str(wordDict[key]))

    print(outputLines)
    with open(outputFile, "a") as oFile:
        oFile.writelines("\n".join(outputLines))





inputFile = os.path.join(currDirectory, "WordCounter_Example", "Inputs", "test2.txt")
wordCounter(inputFile)