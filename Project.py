"""
===========================================================
                 Project Part 1
              First Phase of the Project
              By Frelin C. Ogario-Johnson
===========================================================
"""
import random
import statistics
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz

movies = {
    "The Shawshank Redemption": 9.5,
    "Pulp Fiction": 8.8,
    "The Room": 3.6,
    "The Godfather": 9.2,
    "The Godfather: Part II": 9.0,
    "The Dark Knight": 9.0,
    "12 Angry Men": 8.9,
    "Everything Everywhere All At Once": 8.9,
    "Forrest Gump": 8.8,
    "Star Wars: Episode V": 8.7
}


def main():
    """ Displays the Menu of choices or commands

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    print(f"\033[36m Menu: \n 1. List movies \n 2. Add movie \n 3. Delete movie \n 4. Update movie \n"
          f" 5. Stats \n 6. Random movie \n 7. Search movie \n 8. Movies sorted by rating \n"
          f" 9. Creating Rating Histogram \033[0m")
    # User Input
    choice = int(input("Enter choice (1-9): "))

    if choice == 1:
        movie_list()
    elif choice == 2:
        add_movie()
    elif choice == 3:
        delete_movie()
    elif choice == 4:
        update_movie()
    elif choice == 5:
        movie_statistics()
    elif choice == 6:
        random_movie()
    elif choice == 7:
        search_movie()
    elif choice == 8:
        sorted_movie()
    elif choice == 9:
        movie_histogram()
    else:
        print("\033[31m" + "Error! Please choose from numbers 1 to 9." + "\033[0m")
        main()
    # To display the menu after executing a command
    enter = input("\033[33m" + "Please enter to continue " + "\033[0m")
    if enter == "":
        main()
    else:
        print("\033[31m" + "Error! Please press Enter key to continue" + "\033[0m")
        main()


def movie_list():
    """ Displays the dictionary of movies[key] and its rating(value)

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    print(f"{len(movies)} movies in total")
    [print(f"{key}: {value}") for key, value in movies.items()]
    return movies


def add_movie():
    """ Adds a movie title[key] and its rating(value)

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    movie_name = input("Enter new movie name: ")
    # Validating an update not an additional movie
    if movie_name in movies.keys():
        print(f"{movie_name} is already in the movie app. Do you want to update {movie_name}? ")
        user_input = input("Press 'Y' for Yes and 'N' for No: ")
        if user_input == "Y":
            movie_rating = float(input("Enter new movie rating (0-10): "))
            if movie_rating <= 10:
                movies[movie_name] = movie_rating
                print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
            else:
                print(f"\033[31m {movie_rating} is invalid.\033[0m")
        elif user_input == "N":
            main()
    # Adding a new movie title and rating
    elif movie_name not in movies.keys():
        movie_rating = float(input("Enter new movie rating (0-10): "))
        if movie_rating <= 10:
            movies[movie_name] = movie_rating
            print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
        else:
            print(f"\033[31m {movie_rating} is invalid.\033[0m")
    return movies


def delete_movie():
    """ Deletes a movie title[key] and its rating(value)

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    movie_name = input("Enter movie name to delete: ")
    if movie_name in movies:
        del movies[movie_name]
        print(f"The movie {movie_name} successfully deleted")
    else:
        print(f"\033[31m Movie {movie_name} doesn't exist. Choose from the following movies \033[0m")
        movie_list()
    return movies


def update_movie():
    """ Updates the rating(value) of a movie[key]

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    movie_name = input("Enter movie name: ")
    if movie_name in movies:
        movie_rating = float(input("Enter new rating: "))
        movies[movie_name] = movie_rating
        if movie_rating <= 10:
            movies[movie_name] = movie_rating
            print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
        else:
            print(f"\033[31m {movie_rating} is invalid.\033[0m")
    else:
        print(f"\033[31m Movie {movie_name} doesn't exist. Choose from the following movies \033[0m")
        movie_list()
    return movies


def movie_statistics():
    """ Displays the average, mean, median, maximum rating and the minimum rating of the movies.

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    rating = 0
    # Find the average of the movie rating.
    for value in movies.values():
        rating += value
    average = rating / len(movies)
    print(f"Average rating: {average}")

    # Find the median of the movie rating
    ratings = list(movies.values())
    sorted_ratings = sorted(ratings)
    median_ratings = statistics.median(sorted_ratings)
    print(f"Median rating: {median_ratings}")

    # Find the best movies
    max_title = max(movies, key=movies.get)
    max_rating = movies[max_title]
    print(f"Best movie: {max_title}: {max_rating} ")

    # Find the worst movies
    min_title = min(movies, key=movies.get)
    min_rating = movies[min_title]
    print(f"Worst movie: {min_title}: {min_rating}")
    return movies


def random_movie():
    """ Randomly choose a movie title[key]

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    key, value = random.choice(list(movies.items()))
    print(f"Your movie tonight: {key}, it's rated {value}")
    return movies


def search_movie_distance(movie_name):
    """ Search for a matching movie title

     Args:
        movie_name(str): Input user for searching term

    """
    global movies
    close_movie_match = []
    for movie in movies.keys():
        ratio = fuzz.token_set_ratio(movie_name.lower(), movie.lower())
        if ratio >= 55:
            close_movie_match.append((movie, movies[movie]))
    if close_movie_match:
        movie_match = dict(sorted(close_movie_match, key=lambda x: x[1], reverse=True))
        print(f"The movie {movie_name} does not exist. Did you mean: ")
        for movie in movie_match.keys():
            print(f"{movie}")
        validation = input(f"Press 'Y' for Yes and 'N' for No: ")
        if validation == "Y":
            for movie, rating in movie_match.items():
                print(f"{movie}, {rating}")
        elif validation == "N":
            print(f"Sorry, the movie '{movie_name}' doesn't exist")


def search_movie():
    """ Search a movie title[key] and its possible matching string

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    movie_name = input("Enter a search term: ")
    for movie, rating in movies.items():
        lowercase_movies = movie.lower()
        lowercase_movie_name = movie_name.lower()
        if lowercase_movie_name in lowercase_movies:
            print(f"{movie}, {rating}")
    if not any(lowercase_movie_name in movie.lower() for movie in movies.keys()):
        search_movie_distance(movie_name)
    else:
        print("No results found.")
    return movies


def sorted_movie():
    """ Sorts the movie title[key] based on its rating(value) in a descending order

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict
    """
    global movies
    sorted_movies = dict(sorted(movies.items(), key=lambda x: x[1], reverse=True))
    [print(f"{key}: {value}") for key, value in sorted_movies.items()]
    return movies


def movie_histogram():
    """ Allows user to save the histogram of ratings in different file type specified

     No Args:
        dict: It is using the global dictionary movies
        key[str]: Titles of the movies
        value(float): Rating of the movies

    Returns:
        dict

    Raises:
        ValueError: If filetype is unsupported
    """
    plt.hist(movies, bins=15)
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Movie Title")
    plt.ylabel("Rating")
    plt.title("Movie Rating")
    filename = input("Choose a filename for your histogram: ")
    filetype = input("In which filetype do you want to save the histogram as? ")
    # Checking the supported format
    if filetype in "eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff":
        file_name = filename + "." + filetype
        plt.savefig(file_name)
        plt.show()
        return movies
    raise ValueError("Unsupported Format")


if __name__ == "__main__":
    main()