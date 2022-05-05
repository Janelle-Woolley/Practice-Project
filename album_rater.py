##
# album_rater.py
# allow user to rate albums
#
# Author: Janelle Woolley, Phoebe
# 08/04/22 Version_1

# TO DO:
# function for editing album
# function recomending an album
# call functions

# DOING:
# function for rating album
# function for printing album

# DONE:
# Main routine
# create nested dictionary
# Menu function
# function for adding album
# function for deleting album


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
                print("You have chosen {}.\n".format(choice))
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

            dictionary.update({key: {"Title": album,
                                     "Artist": artist,
                                     "Genre": genre,
                                     "Rating": rating}})
            adding_albums = False


# Created By Phoebe, I edited code to fit
def delete_album(dictionary):
    deleting_albums = True
    while deleting_albums:
        delete = input("\nPlease select the album number you would "
                       "like to delete, or press 'q' to quit: ")
        
        if delete == "q":
                deleting_albums = False
        else:
            print("You have chose to delete album {}.".format(delete))
            del dictionary[delete]
            key = len(dictionary) - 1
            dictionary.update()
            deleting_albums = False


def rate_album(dictionary):
    album_rating_change = input("\nPlease select the key number "
                                "for the album you would like to "
                                "change the rating for"
                                "\nOR press 'q' to quit: "))
    
    album_info = dictionary[album_rating_change]
    album = album_info["Title"]
    artist = album_info["Artist"]
    genre = album_info["Genre"]
    rating = album_info["Rating"]
    key = album_rating_change

    getting_rating = True
    while getting_rating:
        try:
            new_rating = int(input("Please give the album a rating out of 5: "))

            if new_rating < 0 or new_rating > 5:
                print("Please rate the album from 0 to 5")

            elif new_rating == rating:
                print("The album already has this rating "
                      "please change it")

            elif new_rating != rating and new_rating >= 0 and new_rating <= 5:
                dictionary.update({key: {"Title": album,
                                     "Artist": artist,
                                     "Genre": genre,
                                     "Rating": new_rating}})
                getting_rating = False

            else:
                print("Please enter a number between 0 and 5")
                
        except ValueError:
            print("Please enter a whole number")        


def print_albums(dictionary):
    for key in dictionary.keys():
        album = key["Title"]
        artist = key["Artist"]
        genre = key["Genre"]
        rating = key["Rating"]

        print("{}\t{}\t{}\t{}\t{}".format(key, album, artist, genre, rating))

def prints(dictionary):
    print(dictionary)

if __name__ == "__main__":
    albums = {1: {"Title": "Sour",
                  "Artist": "Olivia Rodrigo",
                  "Genre": "Pop", "Rating": 5},
              2: {"Title": "Promises",
                  "Artist": "Sam Shepherd",
                  "Genre": "Jazz", "Rating": 2},
              3: {"Title": "Sound Ancestors",
                  "Artist": "Madlib",
                  "Genre": "Hip-Hop", "Rating": 0},
              4: {"Title": "Valentine",
                  "Artist": "Snail Mail",
                  "Genre": "Alternative", "Rating": 4},
              5: {"Title": "Daddy's Home",
                  "Artist": "St. Vincent",
                  "Genre": "Pop", "Rating": 2}}

    # loop so meun will keep coming up after completing an option
    code_running = True
    while code_running:
        menu_option = menu()
        if menu_option == 0:
            code_running = False
        elif menu_option == 1:
            add_album(albums)
            print_albums(albums)
        elif menu_option == 2:
            print_albums(albums)
            delete_album(albums)
            print_albums(albums)
        elif menu_option == 4:
            prints(albums)
            rate_album(albums)
        elif menu_option == 5:
            print_albums(albums)
        else:
            print("Please enter a valid option")
