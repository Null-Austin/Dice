import random
import inflect
import ast
#from deep_translator import GoogleTranslator removed due to scripting conflict.
from termcolor import colored, cprint
from os import system, name



# not used no more!? language='en' #what is your language mate? 
#print(GoogleTranslator().get_supported_languages(as_dict=True))#un comment this to make it show supported langs

total_sides = 20 #makes since?
file=open('prompts.txt')
PossibleSen = ast.literal_eval(file.read())
s=len(PossibleSen)
def n2t(num):
    return(inflect.engine().number_to_words(num))
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
while(True):
    a=n2t(random.randrange(0,total_sides))
    clear()
    input(colored(PossibleSen[random.randrange(0,s)],'blue')+colored(a,'yellow'))