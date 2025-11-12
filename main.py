# importing library with psuedo-random number generator capability
import random

# list of classmates' names
names = ['Asher','Nate','Caspian','Shaan','Colin','Rayan','Alex','Dennis','Naoki','Maddox','Evan','Mr. Jeffers','Blake','David']

# randomly chooses a number value, which corresponds with a name listed
selection = random.choice(names)
print(selection)