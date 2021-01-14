import os
import unidecode #To remove accentted characters during comparisons
from tkinter import *
from tkinter import messagebox

from Modules.Solver import SortByGivenWord
from Modules.LanguagesConnector import GetLanguages, GetFrequencyArr

currentDirectory = os.path.dirname(os.path.realpath(__file__))
languageDirectory = currentDirectory + '/Languages/'
supportedLanguages = GetLanguages(languageDirectory)

def UpdateList():
    freqList = GetFrequencyArr(languageDirectory + selectedLanguage.get() + '.txt')
    sortedFreqList = SortByGivenWord(freqList, givenWord.get(), wrongLetters.get(), wrongWords.get())
    newList = '\n'.join(sortedFreqList[0:10])
    possibleWordsList['text'] = 'Possible words:\n' + newList

if __name__ == '__main__':
    if (len(supportedLanguages) == 0):
        messagebox.showerror('Load error.', 'Could not load language files.')
    else:
        window = Tk()
        window.title('Hangman Solver')
        window.geometry('300x350')

        selectedLanguage = StringVar()
        selectedLanguage.set(supportedLanguages[0])

        Label(window, text='Language').grid(row=0, column=0, sticky='nw')
        OptionMenu(window, selectedLanguage, *supportedLanguages).grid(row=0, column=1, sticky='nw')

        Label(window, text='Word').grid(row=1, column=0, sticky='nw')
        givenWord = Entry(window)
        givenWord.grid(row=1, column=1, sticky='nw')

        Label(window, text='Wrong letters').grid(row=2, column=0, sticky='nw')
        wrongLetters = Entry(window)
        wrongLetters.grid(row=2, column=1, sticky='nw')

        Label(window, text='Wrong words').grid(row=3, column=0, sticky='nw')
        wrongWords = Entry(window)
        wrongWords.grid(row=3, column=1, sticky='nw')

        Button(text='Search', command=UpdateList).grid(row=4, column=0, sticky='ne')
        possibleWordsList = Label(window)
        possibleWordsList.grid(row=5, column=1, sticky='nw')

        window.mainloop()