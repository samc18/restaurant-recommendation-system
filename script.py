from linkedlist import LinkedList
from data import types, restaurant_data
from welcome import print_welcome

# Creating LinkedList data structure

def set_restaurant_types():
    restaurant_types = LinkedList()

    for type in types:
        restaurant_types.insert_beginning(type)

    restaurant_types.remove_node(None)

    return restaurant_types

def set_restaurants():
    restaurants = LinkedList()

    for restaurant in restaurant_data:
        restaurants.insert_beginning(restaurant)

    restaurants.remove_node(None)

    return restaurants

# Searching LinkedList data structure

def get_restaurant_type_desires(answer):
    types = set_restaurant_types()
    current_node = types.get_head_node()
    possible_types_list = []

    while current_node:
        if current_node.get_value()[0: len(answer)] == answer:
            possible_types_list.append(current_node.get_value())
        current_node = current_node.get_next_node()
    
    return possible_types_list

def get_restaurants(answer):
    restaurants = set_restaurants()
    current_node = restaurants.get_head_node()
    restaurants_list = []

    while current_node:
        current_node_value = current_node.get_value()
        if current_node_value[0] == answer:
            restaurants_list.append(current_node.get_value())
        current_node = current_node.get_next_node()

    return restaurants_list

# Displaying restaurants info

def display_restaurants(restaurants):
    for restaurant in restaurants:
        print("Place name: {name}".format(name = restaurant[1]))
        print("Price: {price}/5".format(price = restaurant[2]))
        print("Score: {score}/5".format(score = restaurant[3]))
        print("Address: {address}".format(address = restaurant[4]))
        print("-------------------------------------------")

# User interaction

print_welcome()

while True:
    print("What type of food would you like to eat?")
    print("Type the beginning of that food type and press enter to see if it's here.")

    type_desire = input().lower()

    options = get_restaurant_type_desires(type_desire)

    if len(options) == 0:
        print("We don't have any restaurants starting with those letters.")
    elif len(options) == 1:
        print("We only have the following option: {option}".format(option=options[0]))
        print("Would you like to see {option} places?".format(option=options[0]))
        print("Please answer 'y' for yes and 'n' for no")
        answer = input()
        if answer == "y":
            restaurants = get_restaurants(options[0])
            display_restaurants(restaurants)
            print("Would you like to see more places?")
            answer2 = input()
            if answer2 == "n":
                break
            else:
                print("Please enter a valid answer.")
        elif answer == "n":
            break
        else:
            print("Please enter a valid answer.")
    else:
        print("We have the following options: {possible_types}".format(possible_types = ", ".join(options)))