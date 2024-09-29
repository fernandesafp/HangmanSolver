import unidecode #To remove accented characters during comparisons

def SortByGivenWord(freqList, word, notLetters, notWords):
    newFreqList = []
    for freqWord in freqList:
        #First checks if the length are the same
        if (len(freqWord) == len(word)):
            wordIsPossible = True

            #Checks if freqWord contains any of the letters that are given as not there
            for notLetter in notLetters:
                if notLetter in unidecode.unidecode(freqWord):
                    wordIsPossible = False
                    break

            #Checks if freqWord contains any notWord
            notWordsSplit = notWords.replace('\n',',').split(',')
            for notWord in notWordsSplit:
                if notWord and notWord in freqWord:
                    wordIsPossible = False
                    break

            if (wordIsPossible):
                #Then with the solved word checks if known letters are found in the same place
                for letter in enumerate(word):
                    if (letter[1] != '.'):
                        if (unidecode.unidecode(freqWord[letter[0]]) != letter[1]):
                            wordIsPossible = False
                            break
                if (wordIsPossible):
                    newFreqList.append(freqWord)

    return newFreqList