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

# Created By Phoebe
def getting_album():
    choices = [1, 2, 3, 4, 5, 6]
    getting_albums = True
    while getting_albums:
        try:
            choice = int(input("\nPlease chose your option\n"
                           "1: add album\n"
                           "2: delete album\n"
                           "3: edit album\n"
                           "4: rate album\n"
                           "5: print albums\n"
                           "6: recomend albums\n"))
            if choice in choices:
                print("you have chosen {}.\n".format(choice))
                getting_albums = False
        except ValueError:
            print("enter a valid number")
        return choice

def add_album(dictionary):
    pass

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

    menu_option = getting_album()
