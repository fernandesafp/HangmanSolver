import os
from Modules.LanguagesConnector import GetFrequencyArr, GetLanguages
from Modules.Solver import SortByGivenWord

currentDirectory = os.path.dirname(os.path.realpath(__file__))
languageDirectory = currentDirectory + '/Languages/'
supportedLanguages = GetLanguages(languageDirectory)

langPath = languageDirectory + supportedLanguages[1] + '.txt'
freqList = GetFrequencyArr(langPath)

word = 'r....'
nots = 'oiue'
SortByGivenWord(freqList, word, nots)