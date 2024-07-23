""" Question2

The Shopping List Maker


Objective: The aim of this assignment is to create a program that helps users make a shopping list.


Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 

Task 2: Include a feature to remove items from the list. 

Task 3: Add a function that prints out the entire list. """


def display_list (items):
    for item in items:
        print(item)

def add_to_list(items):
    shopping_item = input("Please type one item at a time you would like to add here: ")
    item =[shopping_item]
    items.append(item)
    print(f"{shopping_item} has been added to list ")
    return items

def rem_from_list(items):
    shopping_item = input("Please type type one item at a time you would like to remove here: ")
    item =[shopping_item]
    items.remove(item)
    return items



def main(): # creating a customizee function
    Shopping_list = [] #creating an empty list to store, add and remove list
    flag = True # creating a loop that can be control.
    while flag:
        ans = input('''
Welcome to your Shopping list.
Select from the options below:
1 - View list.
2 - Add item to list.
3 - Remove item from list.
4 - Quit application.
''')



        if ans == "1":
            display_list(Shopping_list)
        #print list
        elif ans == "2":
            list_update = add_to_list(Shopping_list)
            Shopping_list = list_update
        #add item to list
        elif ans == "3":
            list_update = rem_from_list(Shopping_list)
            Shopping_list = list_update
        #add remove from list
        elif ans == "4":
            flag = False
            print("Closing Shopping List application")
        else:
            print("Invalid entry. Please try again")

main()


        
