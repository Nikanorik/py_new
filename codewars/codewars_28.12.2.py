def how_much_i_love_you(nb_petals):
    list_flowers=['I love you','a little', 'a lot', 'passionately', 'madly', 'not at all']
    return list_flowers[nb_petals%6-1]


how_much_i_love_you(9)