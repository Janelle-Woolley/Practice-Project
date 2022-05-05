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
# Testing

# DONE:
# Main routine
# create nested dictionary
# Menu function
# function for adding album
# function for deleting album
# function for rating album
# function for printing album


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
    album = input("Please enter the title of the album: ")
    artist = input("Please enter the artist: ")
    genre = input("Please enter the genre: ")
    rating = input("Please give it a rating: ")
    # converts dictionary in a list so it can access the last value and add 1 to it
    # this creates a new album key
    key = list(dictionary.keys())[-1] +1

    dictionary.update({key: {"Title": album.title(),
                             "Artist": artist.title(),
                             "Genre": genre.title(),
                             "Rating": rating}})


# Created By Phoebe
# I removed parts of it becuase the get_album_key function already did it
def delete_album(dictionary, key):
    """
    Asks user for album key
    Deletes coresponding album
    """
    print("You have chose to delete album {}.".format(key))
    del dictionary[key]


def get_album_key(dictionary):
    """
    Ask user for album key then returns it
    """
    MIN_DICT_SIZE = 0
    getting_key = True
    while getting_key:
        try:
            album_rating_change = int(input("\nPlease select the key number "
                                            "for the album you would like to select: "))

        except ValueError:
            print("Please enter a whole number")

        if album_rating_change > len(dictionary) or album_rating_change < MIN_DICT_SIZE:
            print("Please enter an album key")

        elif album_rating_change <= len(dictionary):
            return album_rating_change
            

        else:
            print("Please enter an album key")


def change_rating(dictionary, key):
    """
    Asks user for a new rating for album selected
    Updates dictionary accordingly
    """
    HIGHEST_RATING = 5
    LOWEST_RATING = 0

    # seting variables for the album info so they can be used when updating the dictionary 
    album_info = dictionary[key]
    album = album_info["Title"]
    artist = album_info["Artist"]
    genre = album_info["Genre"]
    rating = album_info["Rating"]

    getting_rating = True
    while getting_rating:
        try:
            new_rating = int(input("Please give the album a rating out of 5: "))

        except ValueError:
            print("Please enter a whole number")
        
        if new_rating < LOWEST_RATING or new_rating > HIGHEST_RATING:
            print("Please rate the album out of 5")

        elif new_rating == rating:
            print("The album already has this rating "
                  "please change it")

        elif new_rating != rating and new_rating >= LOWEST_RATING and new_rating <= HIGHEST_RATING:
            dictionary.update({key: {"Title": album,
                                     "Artist": artist,
                                     "Genre": genre,
                                     "Rating": new_rating}})
            getting_rating = False

        else:
            print("Please enter a number between 0 and 5")


def print_albums(dictionary):
    """
    Prints albums out formated
    """
    for key in dictionary.keys():
        album_info = dictionary[key]
        album = album_info["Title"]
        artist = album_info["Artist"]
        genre = album_info["Genre"]
        rating = album_info["Rating"]

        print("{}\t{}\t\t{}\t{}\t{}".format(key, album, artist, genre, rating))


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
            key = get_album_key(albums)
            delete_album(albums, key)
        elif menu_option == 3:
            print_albums(albums)
            key = get_album_key(albums)
            edit_album(albums, key)
        elif menu_option == 4:
            print_albums(albums)
            key = get_album_key(albums)
            change_rating(albums, key)
        elif menu_option == 5:
            print_albums(albums)
        else:
            print("Please enter a valid option")
