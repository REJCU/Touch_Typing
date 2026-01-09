import random


words_str = "place leave stop around mile very very its found men took number about earth the with does earth large for try now if paper must as may seem idea never high so be little fire what another many year both try must long own his but oil soon you know would got which began book near those will life watch idea try was ask in know began later get is follow out there feet river walk enough different come such every you with study these any way point show has" 

def turn_list(x):
    words = x.split()
    quoted_string = ' ,'.join([f'"{word}"' for word in words])

    print(quoted_string)

turn_list(words_str)



