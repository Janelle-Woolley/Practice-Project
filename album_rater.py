##
# album_rater.py
# allow user to rate albums
#
# Author: Janelle Woolley, Phoebe and Syuni
# 08/04/22 Version_1

## TO DO:
# function for deleting album
# function for editing album
# function for rating album
# function for printing album
# function recomending an album
# call functions

## DOING:
# function for adding album

## DONE:
# Main routine
# create nested dictionary
# Menu function

# Created By Phoebe, I edited variable names
def menu():
    """
    Ask user to select an option
    Returns selected option
    """
    choices = [1, 2, 3, 4, 5, 6]
    getting_option = True
    while getting_option:
        try:
            choice = int(input("\nPlease chose your option\n"
                               "1: add album\n"
                               "2: delete album\n"
                               "3: edit album\n"
                               "4: rate album\n"
                               "5: print albums\n"
                               "6: recomend albums\n"
                               "0: exit\n"))
            if choice in choices:
                print("you have chosen {}.\n".format(choice))
                getting_option = False

        except ValueError:
            print("enter a valid number")

        return choice


def add_album(dictionary):
    """
    Asks for user inputs and adds them to dictionary
    """
    adding_albums = True
    while adding_albums:
        album = input("Please enter the title of the album\n"
                      "(or type 'q' to quit)\n"
                      ": ")
        if album == "q":
            adding_albums = False
        else:
           artist = input("Please enter the artist: ")
           genre = input("Please enter the genre: ")
           rating = input("Please give it a rating: ")
           key = len(dictionary) + 1

           dictionary.update({key:{album, artist, genre, rating}})
           adding_albums = False


def print_albums(dictionary):
    print(dictionary)

if __name__ == "__main__":
    albums = {1:{"Title":"Sour",
                 "Artist":"Olivia Rodrigo",
                 "Genre":"Pop", "Rating":5},
              2:{"Title":"Promises",
                 "Artist":"Sam Shepherd",
                 "Genre":"Jazz", "Rating":2},
              3:{"Title":"Sound Ancestors",
                 "Artist":"Madlib",
                 "Genre":"Hip-Hop", "Rating":0},
              4:{"Title":"Valentine",
                 "Artist":"Snail Mail",
                 "Genre":"Alternative", "Rating":4},
              5:{"Title":"Daddy's Home",
                 "Artist":"St. Vincent",
                 "Genre":"Pop", "Rating":2}}
    
    # loop so meun will keep coming up after completing an option
    code_running = True
    while code_running:
        menu_option = menu()
        if menu_option == 0:
            code_running = False
        elif menu_option == 1:
            add_album(albums)
            print_albums(albums)
        
