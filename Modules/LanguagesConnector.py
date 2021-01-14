import os

def GetFrequencyArr(langPath):
    with open(langPath) as f:
        words = f.readlines()
    freqArr = []
    for word in words:
        freqArr.append(word.split(' ')[0])
    return freqArr

def GetLanguages(folderPath):
    languagesArr = []
    for file in os.listdir(folderPath):
        if file.endswith('.txt'):
            languagesArr.append(file.replace('.txt', ''))
    return languagesArr