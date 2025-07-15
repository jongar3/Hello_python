import pandas
import pathlib

BASE_PATH = pathlib.Path(__file__).resolve().parent
data= pandas.read_csv(BASE_PATH / 'nato_phonetic_alphabet.csv')

phonetic_dictionary= {row.letter:row.code for (index, row) in data.iterrows()}

word= input("Introduce a Word: ")
phonetic_word= [phonetic_dictionary[letter] for letter in word.upper() if letter in phonetic_dictionary.keys()]
print(phonetic_word)