
'''
Author: Zdenek Andrew Bocek
Description: Project 2 and improvement to Quiz 4 Question 6, in one program
Menu's Please
Professor Tsaasan
3/8/2020
Orange Coast College
CS A131
'''


import os


# The program greets the user and prompts to interact

print("\n*****************************")
print("Business Owner Portal - Menu File Upload Program")
print("*******************************")

print("Please follow these instructions:")
print("- When prompted please enter *only one* restaurant name")
print(" (Only one menu is allowed per restaurant)\n")


#********************
# New Functionalities
#********************

def check_if_file_available(file_name):
    '''
    WHAT: checking if menu file is located in correct directory
    WHY: need to check if the menu file is available if not
         restaurant needs to upload it
    RESOURCES: using the OS module
    '''
    
    # gets the current working directory
    current_dir = os.getcwd()
    
    file_list = os.listdir(current_dir + "\\costa_menus")
    
#    print(file_list)
    
    for file in file_list:
        if file == file_name:
            print("...menu file found!")
            print("filename:",file)
            return True
        
    print(f"filename '{file_name}' not found!")
    return False

#************

def add_to_menu_index(rest_name, file_name):
    '''
    WHAT: Appending the restaurant name to a menu_index file
    WHY: We have to use the menu_index file 
    RESOURCES: using open() with "append" mode
    '''    
    # append-mode = "a" (instead of "w")
    with open("menu_index.txt", "a") as file:
        items = f"{rest_name}, {file_name}"
        file.write("\n" + items)
        

#************

def new_user_enrollment(rest_name):
    '''
    WHAT: Obtaining the information from the new user
    WHY: We need this information in order to update 
         "costa_restaurants.txt"
    RESOURCES: accessing list elements / assertion
    '''       
    new_user_info = [rest_name, " ", " ", " ", " ", " ", " "]
    
    print("\nIt looks like you are a new user")
    print("You must provide the minimum restaurant information \
          to our system.")
    print("Please answer the following questions:\n")
    
    #*********************
    print("Do you serve Vegetarian food?", end="")
    response = input("Enter a response (y/n): ")
    
    assert response == "y" or response == "n", "Invalid response, your response must be 'y' or 'n'"
    
    if response == "y":
        # Vegetarian option at index = 3
        new_user_info[3] = " yes"
        
    else:
        new_user_info[3] = " no"
        
    #*********************
    
    print("\nDo you serve Vegan food?", end="")
    response = input("Enter a response (y/n): ")
    
    assert response == "y" or response == "n", "Invalid response, your response must be 'y' or 'n'"
    
    if response == "y":
        # Vegan option at index = 4
        new_user_info[4] = " yes"
        
    else:
        new_user_info[4] = " no"
        
    #*********************
    
    print("\nDo you serve Gluten-free food?", end="")
    response = input("Enter a response (y/n): ")
    
    assert response == "y" or response == "n", "Invalid response, your response must be 'y' or 'n'"
    
    if response == "y":
        # Gluten-free option at index = 5
        new_user_info[5] = " yes"
        
    else:
        new_user_info[5] = " no"
        
    #*********************
    
    print("\nPlease provide the following Optional information", end="")
    zip_code = input("Please enter your restaurant's zip code: \n")
    # Zip code at index = 2
    new_user_info[2] = " " + zip_code
    
    
    print("\nThank you for providing that information.\n")
    
    return new_user_info
    
#************

def add_to_restaurant_dataset(user_list):
    '''
    WHAT: Updating the "costa_restaurants.txt" dataset
    WHY: for new user need to append their new user information
    RESOURCES: ",".join()
    '''      
    with open("costa_restaurants.txt", "a") as file:
        # join converts a list into a string
        # why? because we are writing a String to a file 
        list_as_string = ",".join(user_list)
        
        file.write(list_as_string)
        
    print("\nYour restaurant information has been added to our dataset!")
    

#************
# MAIN PROGRAM SECTION
#************


rest_names = []

with open("costa_restaurants.txt", "r") as file:
    
    # skipping header
    lines = file.readlines()[1:]
    
    for line in lines:
        
        # first strip() then split()
        # Using split() making sure to
        # include "," 
        
#        print(line.strip().split(","))
        
        line_as_list = line.strip().split(",")
        
#        print(line_as_list[0])
        
        rest_name = line_as_list[0]
        
        rest_names.append(rest_name)
        
        
#print(rest_names)
# classic loop

#rest_names_lower = []
#
#for i in rest_names:
#    rest_names_lower.append(i.lower())
#
#print(rest_names_lower)      

  
# list comprehension
        
rest_names_lower = [i.lower() for i in rest_names]

#print(rest_names_lower) 

        

restaurant_name = input("What's the name of the restaurant?\n")

# if restaurant name provided is included in the list
# of restaurante names (rest_names)
if restaurant_name.lower() in rest_names_lower:
    
    print("You are already added as restaurant to our restaurant dataset.")
    
    menu_file_name = input("Please enter the menu filename including the extension, for example: villa.pdf\n")
    
    assert menu_file_name.endswith(".pdf"), "Invalid extension, you are either not including the file extension or it's not a pdf file (.pdf), menus must be in .pdf format"
    
    if check_if_file_available(menu_file_name):
        
        add_to_menu_index(restaurant_name, menu_file_name)
        
        # Reading the file: costa_restaurants.txt
        costa_listings = []
        with open("costa_restaurants.txt", "r") as file:
            # skip header
            lines = file.readlines()[1:]
            for line in lines:
                costa_listings.append(line)
                
                
        # Reading the file: menu_index.txt
        index_listings = []
        with open("menu_index.txt", "r") as file:
            # skip header
            lines = file.readlines()[1:]
            for line in lines:
                index_listings.append(line)
                
        with open("costa_restaurants.txt", "w") as file:
            
            header = 'name, address, zip code, vegetarian, vegan, gluten-free, menu'
            
            # header being written
            file.write(header + '\n')
            
            # Using a set()
            unique_listings = set()
            
            # Nested Loop = Loop inside a loop
            for i in costa_listings:
                # using strip to make sure all
                # extra newline characters are removed
                # prior to split()
                i_as_list = i.strip().split(",")
                
                for j in index_listings:
                    j_as_list = j.strip().split(",")
                    
                    if i_as_list[0].lower() == j_as_list[0].lower():
                        i_as_list[-1] = j_as_list[1]
#                        print(i_as_list)
                        unique_listings.add(",".join(i_as_list))
                        
                    else:
                        unique_listings.add(",".join(i_as_list))
            
            # Converting a set into a list 
            # for writing to a file
            for x in list(unique_listings):
                file.write(x + "\n")
                        
else:
    
    new_user_list = new_user_enrollment(restaurant_name)
#    print(new_user_list)
                        
    menu_file_name = input("Please enter the menu filename including the extension, for example: villa.pdf\n")        
    
    assert menu_file_name.endswith(".pdf"), "Invalid extension, you are either not including the file extension or it's not a pdf file (.pdf), menus must be in .pdf format"
    
    if check_if_file_available(menu_file_name):
        
        add_to_menu_index(restaurant_name, menu_file_name)
        
        new_user_list[-1] = " " + menu_file_name
        
        add_to_restaurant_dataset(new_user_list)
        
    
    
