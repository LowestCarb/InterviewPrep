from ensurepip import version
import os

globalVersion = 0
versionDict = {}
currDirectory = os.getcwd()

def PUT(key: str, value: int):
    value = value.strip()
    global globalVersion
    globalVersion += 1

    if key in versionDict.keys():
        versionDict[key][globalVersion] = value
    else:
        subDict = {}
        subDict[globalVersion] = value
        versionDict[key] = subDict

    # versionDict[key] = versionDict[key][globalVersion]
    outputstring = []
    outputstring.append("PUT(#" + str(globalVersion) + ")")
    outputstring.append(key)
    outputstring.append("=")
    outputstring.append(value)
    return " ".join(outputstring)

def GET(key: str, version: int = None):
    key = key.strip()
    if version != None:
        version = version.strip()

    if key not in versionDict.keys():
        return "NULL"

    if version == None:
        subDict = versionDict[key]
        lastVal = subDict[sorted(subDict.keys())[-1]]
        return "GET " + key + " = " + lastVal

    else:
        value = "NULL"
        subDict = versionDict[key]
        if version in subDict.keys():
            value = subDict[version]
        else:
            keys = sorted(subDict.keys(), reverse=True)
            for currkey in keys:
                if int(currkey) < version:
                    value = subDict[currkey]
                    break

        return "GET " + key + "(#" + str(version) + ") = " + str(value)

def readFile(file: str):
    inputFile = file
    #check if file exists
    if not os.path.exists(inputFile):
        return None

    #set up output
    outputFile = os.path.join(currDirectory, "LaptopCodingInterview", "Outputs", file.split('\\')[-1])

    if os.path.exists(outputFile):
        os.remove(outputFile)

    outputLines = []

    with open(inputFile, "r") as iFile:
        for line in iFile:
            words = line.split(' ')
            currOutLine = ""
            if words[0] == "PUT":
                currOutLine = PUT(words[1], words[2])
            else: #GET
                if len(words) == 2:
                    currOutLine = GET(words[1])
                else:
                    currOutLine = GET(words[1], words[2])

            outputLines.append(currOutLine)

    with open(outputFile, "a") as oFile:
        oFile.writelines("\n".join(outputLines))

inputFile = os.path.join(currDirectory, "LaptopCodingInterview", "Inputs", "test1.txt")
readFile(inputFile)