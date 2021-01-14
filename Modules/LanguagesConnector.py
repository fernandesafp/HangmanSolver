import os#, iso639

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
            language = file.replace('.txt', '')
            #native = iso639.to_native(language).split(';')[0]
            #english = iso639.to_name(language).split(';')[0]
            #if (native == english):
            #    language = native
            #else:
            #    language = '{} ({})'.format(native, english)
            languagesArr.append(language)
    return languagesArr