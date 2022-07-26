import os
import requests
import sys
from collections import deque

inCache = " IN_CACHE "
downLoaded = " DOWNLOADED "
currDirectory = os.getcwd()

def imageCache(file: str):
    inputFile = file
    #check if file exists
    if not os.path.exists(inputFile):
        return None

    #set up output
    outputFile = os.path.join(currDirectory, "Cache_Example", "Outputs", file.split('\\')[-1])

    if os.path.exists(outputFile):
        os.remove(outputFile)

    #set up cache data structures
    cache_dict = {} #key - url, val - img data -> {"url": "imgSize", ...}
    cache_deque = deque() #store just the url

    #Open output file
    oFile = open(outputFile, "a")
    oLines = []

    #read in test file
    with open(inputFile, "r") as iFile:
        #set up cache based on max cache size
        cacheSize = int(iFile.readline())
        numURL = int(iFile.readline())
        
        #start reading file by line
        for i in range(numURL):
            imageSize = 0
            currURL = iFile.readline()
            currURL = currURL.rstrip('\n')

            #setup output append line
            outputLine = []
            outputLine.append(currURL)

            # check cache for URL
            if currURL in cache_dict.keys():
                #if exists, grab image from cache
                ##move url to top of cache list
                cache_deque.remove(currURL)
                cache_deque.appendleft(currURL)
                outputLine.append(inCache)
                imageSize = sys.getsizeof(cache_dict[currURL])
            else:
                #else, download image from web
                outputLine.append(downLoaded)
                img_data = requests.get(currURL).content
                imageSize = sys.getsizeof(img_data)
                #try save image to cache
                if imageSize <= cacheSize: #Note: probably don't want to cache something that takes up the entire struct
                    while sys.getsizeof(cache_dict) + imageSize > cacheSize:
                        #if cache full, remove LRU url and image from cache
                        lru_removed = cache_deque.pop()
                        del cache_dict[lru_removed]
                    #else, add image to cache
                    cache_dict[currURL] = img_data
                    cache_deque.appendleft(currURL)

            
            outputLine.append(str(imageSize) + "\n")
            oLines.append(" ".join(outputLine))

    with open(outputFile, "a") as oFile:
        oFile.writelines(oLines)

inputFile = os.path.join(currDirectory, "Cache_Example", "Inputs", "test1.txt")
imageCache(inputFile)