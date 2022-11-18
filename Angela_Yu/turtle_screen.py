from turtle import Screen,Turtle
from prettytable import PrettyTable


table = PrettyTable()
table.add_column("Pockemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = 'c'
table.horizontal_char='*'

print(table)






# timmy=Turtle()
# timmy.shape('turtle')
# timmy.forward(100)
# timmy.color('red')
#
#
#
#
#
# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
# my_screen.exitonclick()