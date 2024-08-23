import random
import inflect
import ast
from deep_translator import GoogleTranslator


language='en' #what is your language mate? 
#print(GoogleTranslator().get_supported_languages(as_dict=True))#un comment this to make it show supported langs

total_sides = 20 #makes since?
file.open('prompts.txt')
PossibleSen = 
s=len(PossibleSen)
def n2t(num):
    return(inflect.engine().number_to_words(num))
def trans(text):
    if language != 'en':
        return(GoogleTranslator(source='auto', target=language).translate(text))
    else:
        return(text)
while(True):
    a=n2t(random.randrange(0,total_sides))
    input(trans(PossibleSen[random.randrange(0,s)]+a))