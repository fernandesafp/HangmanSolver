import os
import iso639

def GetFrequencyArr(langPath):
    with open(langPath) as f:
        words = f.readlines()
    freqArr = []
    for word in words:
        freqArr.append(word.split(' ')[0])
    return freqArr

def GetLanguages(folderPath):
    languagesDict = {}
    languagesList = []
    for file in os.listdir(folderPath):
        if file.endswith('.txt'):
            language_iso = file.replace('.txt', '')
            native = iso639.to_native(language_iso).split(';')[0]
            english = iso639.to_name(language_iso).split(';')[0]
            if (native == english):
                language_name = native
            else:
                language_name = '{} ({})'.format(native, english)
            languagesDict[language_name] = language_iso
            languagesList.append(language_name)
    return languagesList, languagesDict