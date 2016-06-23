import random

flavours = ['pineapple', 'mushroom', 'jalapeno', 'olive', 'cheese']

# instead of one flavour, should be a combination of flavours
# should be random, but to keep it simple, it's a predetermined list

perfect_pizza = ['pineapple', 'mushroom']

# guess will store a list i.e
# 'pineapple,mushroom,jalapeno'
#['pineapple', 'mushroom', 'jalapeno']

print('What\'s the perfect pizza?')

while True:

    pizza_guess = input('> ').split(',')

    incorrect_pizzas = []
    correct_pizzas = []
    pizza_likes = 0
    pizza_dislikes = 0

    for pizza in pizza_guess:

        if pizza in perfect_pizza:
            correct_pizzas.append(pizza)
            pizza_likes += 1
            # print("Arno likes {}".format(pizza))
            print("More toppings")
        else:
            incorrect_pizzas.append(pizza)
            pizza_dislikes += 1
            print("There's something on that I don't like!")


    if pizza_likes == len(perfect_pizza) and pizza_dislikes == 0:
        print("The perfect pizza! Om nom nom!")
        print("The perfect pizzas are {}".format(', '.join(correct_pizzas)))
        break
    # else:
    #     print("He doesn't like {}".format(', '.join(incorrect_pizzas)))
