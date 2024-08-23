import random
import inflect
from deep_translator import GoogleTranslator


language='en' #what is your language mate? 
#print(GoogleTranslator().get_supported_languages(as_dict=True))#un comment this to make it show supported langs

total_sides = 20 #makes since?
PossibleSen = [#God save me
    'You rolled an ', 
    'Congrats for the ', 
    'Another one bites the dust, ', 
    'You summoned a number from the depths of randomness! ', 
    'The dice gods have spoken: ', 
    'Hold your breath... it’s a ', 
    'Your fate is sealed with a ', 
    'Destiny decided: ', 
    'Drumroll, please... ', 
    'As luck would have it, you got a ', 
    'This is the one! You rolled a ', 
    'No turning back now, it’s a ', 
    'Feel the suspense... ', 
    'In a shocking twist of events, it’s a ', 
    'The universe aligns for a ', 
    'You’ve been chosen by the RNG deities! It’s a ', 
    'Against all odds, it’s a ', 
    'Brace yourself... ', 
    'Prepare to be amazed by your roll of ', 
    'The stars have aligned to give you a ', 
    'And the number is... ', 
    'Here comes the big one... ', 
    'With a flick of the wrist, you rolled a ',
    'And just like that, it’s a ', 
    'The suspense is over, you rolled a ', 
    'Your destiny reveals... ',
    'You’ve rolled the mystical number of ', 
    'God, Glory, and Dice, ',
    'And You Won... a ',
    'what do you get when you roll a dice? ',
    'What do you like about this ',
    '1+1=',
]
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