import statistics
import random
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
import sys


def exit_movie():
    """Exits the app"""
    print("Bye!")
    sys.exit()


class MovieManager:
    def __init__(self, my_movies):
        """Defines a class called MovieManager that contains methods to manage a collection of movies

        Args:
            my_movies(dict): Contains a dictionary of movies
        """
        self.movies = my_movies

    def movie_list(self):
        """ Displays the dictionary of movies[key] and its rating(value)

        Returns:
            None
        """
        print(f"{len(self.movies)} movies in total")
        [print(f"\033[34m{key}\n\033[0mRating: {value['rating']}\nYear: {value['year']}") for key, value in
         self.movies.items()]

    def add_movie(self):
        """ Adds a movie title[key] and its rating(value)

        Returns:
            None
        """
        movie_name = input("Enter new movie name: ")
        # Validating an update not an additional movie
        if movie_name in movies.keys():
            print(f"{movie_name} is already in the movie app. Do you want to update {movie_name}? ")
            user_input = input("Press 'Y' for Yes and 'N' for No: ")
            if user_input == "Y":
                movie_rating = float(input("Enter new movie rating (0-10): "))
                if movie_rating <= 10:
                    self.movies[movie_name] = movie_rating
                    print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
                else:
                    print(f"\033[31m {movie_rating} is invalid.\033[0m")
            elif user_input == "N":
                self.run_manager()
        # Adding a new movie title and rating
        elif movie_name not in self.movies.keys():
            movie_rating = float(input("Enter new movie rating (0-10): "))
            if movie_rating <= 10:
                movie_year = int(input("Enter year: "))
                self.movies[movie_name] = {"rating": movie_rating, "year": movie_year}
                print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
            else:
                print(f"\033[31m {movie_rating} is invalid.\033[0m")
        self.run_manager()

    def delete_movie(self):
        """ Deletes a movie title[key] and its rating(value)

        Returns:
            None
        """
        movie_name = input("Enter movie name to delete: ")
        if movie_name in self.movies:
            del self.movies[movie_name]
            print(f"The movie {movie_name} successfully deleted")
        else:
            print(f"\033[31m Movie {movie_name} doesn't exist. Choose from the following movies \033[0m")
            self.movie_list()

    def update_movie(self):
        """ Updates the rating(value) of a movie[key]

        Returns:
            None
        """
        movie_name = input("Enter movie name: ")
        if movie_name in self.movies:
            movie_rating = float(input("Enter new rating: "))
            if movie_rating <= 10:
                self.movies[movie_name]["rating"] = movie_rating
                print(f"\033[34m Movie {movie_name} successfully updated. \033[0m")
            else:
                print(f"\033[31m {movie_rating} is invalid.\033[0m")
        else:
            print(f"\033[31m Movie {movie_name} doesn't exist. Choose from the following movies \033[0m")
            self.movie_list()

    def movie_average(self):
        """Calculates the average rating of all movies in the dictionary

        Returns:
            average_rating(int): average rating of all the movies in the dictionary
        """
        total_rating = 0
        for movie in self.movies.values():
            total_rating += movie["rating"]
        average_rating = total_rating / len(self.movies)
        return average_rating

    def movie_median(self):
        """Identifies the median rating of all the movies in the dictionary

        Returns:
            median_rating(int): median rating of all the movies in the dictionary
        """
        ratings = [value["rating"] for value in self.movies.values()]
        median_rating = statistics.median(ratings)
        return median_rating

    def best_movie(self):
        """Identifies the highest rating of all the movies in the dictionary

        Returns:
            title(str): The title of the movie with the highest rating.
            rating(float): The rating of the movie with the highest rating.
        """
        ratings = [value["rating"] for key, value in self.movies.items()]
        max_rating = max(ratings)
        for title, rating in movies.items():
            if movies[title]["rating"] == max_rating:
                return title, rating["rating"]  

    def worst_movie(self):
        """Identifies the highest rating of all the movies in the dictionary

        Returns:
            title(str): The title of the movie with the lowest rating.
            rating(float): The rating of the movie with the lowest rating.
        """
        ratings = [value["rating"] for key, value in self.movies.items()]
        min_rating = min(ratings)
        for title, rating in self.movies.items():
            if movies[title]["rating"] == min_rating:
                return title, rating["rating"]

    def movie_statistics(self):
        """Serves as the structure for the statistics of the movies dictionary

        Returns:
            None
        """
        average = self.movie_average()
        median = self.movie_median()
        best, best_rating = self.best_movie()
        worst, worst_rating = self.worst_movie()
        print(f"Average: {average}")
        print(f"Median rating: {median}")
        print(f"Best movie: {best} ({best_rating})")
        print(f"Worst movie: {worst} ({worst_rating})")

    def random_movie(self):
        """ Randomly choose a movie title[key]

        Returns:
            None
        """
        key, value = random.choice(list(self.movies.items()))
        print(f"Your movie tonight: {key}, it's rated {value['rating']}")

    def search_movie(self):
        """ Search a movie title[key] and its possible matching string

        Returns:
            None
        """
        movie_name = input("Enter a search term: ")
        lowercase_movie_name = movie_name.lower()
        found_movies = []
        for movie, rating in self.movies.items():
            lowercase_movies = movie.lower()
            if lowercase_movie_name in lowercase_movies:
                found_movies.append((movie, rating['rating']))
        if found_movies:
            found_movies.sort(key=lambda x: x[1], reverse=True)
            for movie, rating in found_movies:
                print(f"{movie}, {rating}")
        else:
            print(f"The search term {movie_name} is not found")

    def search_movie_distance(self, movie_name):
        """ Search for a matching movie title

         Args:
            movie_name(str): Input user for searching term

        """
        close_movie_match = []
        for movie in self.movies.keys():
            ratio = fuzz.token_set_ratio(movie_name.lower(), movie.lower())
            if ratio >= 55:
                close_movie_match.append((movie, self.movies[movie]["rating"]))
        if close_movie_match:
            close_movie_match.sort(key=lambda x: x[1], reverse=True)
            print(f"The movie {movie_name} does not exist. Did you mean: ")
            for movie, rating in close_movie_match:
                print(f"{movie}, {rating}")
            validation = input(f"Press 'Y' for Yes and 'N' for No: ")
            if validation == "Y":
                for movie, rating in close_movie_match:
                    print(f"{movie}, {rating}")
            elif validation == "N":
                print(f"Sorry, the movie '{movie_name}' doesn't exist")
            else:
                print("Sorry wrong input")
        else:
            print(f"Sorry, the movie '{movie_name}' doesn't exist")

    def sorted_movie(self):
        """ Sorts the movie title[key] based on its rating(value) in descending order

         No Args:
            dict: It is using the dictionary movies
            key[str]: Titles of the movies
            value(float): Rating of the movies

        Returns:
            None
        """
        sorted_movies = dict(sorted(self.movies.items(), key=lambda x: x[1]['rating'], reverse=True))
        [print(f"{key}: {value['rating']}") for key, value in sorted_movies.items()]

    def movie_histogram(self):
        """ Allows user to save the histogram of ratings in different file type specified

        Returns:
            None

        Raises:
            ValueError: If filetype is unsupported
        """
        rating_list = []
        for key, value in self.movies.items():
            rating_list.append(value['rating'])
        plt.hist(rating_list, bins=5)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Rating")
        plt.ylabel("Count")
        plt.title("Movie Rating")
        filename = input("Choose a filename for your histogram: ")
        filetype = input("In which filetype do you want to save the histogram as? ")
        # Checking the supported format
        if filetype in "eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff":
            file_name = filename + "." + filetype
            plt.savefig(file_name)
            plt.show()
        raise ValueError("Unsupported Format")

    def run_manager(self):
        while True:
            print(f"\033[36m Menu:\n0. Exit\n1. List movies\n2. Add movie\n3. Delete movie\n4. Update movie\n"
                  f"5. Stats\n6. Random movie\n7. Search movie\n8. Movies sorted by rating\n"
                  f"9. Creating Rating Histogram\033[0m")
            # User Input
            choice = int(input("Enter choice (0-9): "))
            if choice == 0:
                exit_movie()
            elif choice == 1:
                self.movie_list()
            elif choice == 2:
                self.add_movie()
            elif choice == 3:
                self.delete_movie()
            elif choice == 4:
                self.update_movie()
            elif choice == 5:
                self.movie_statistics()
            elif choice == 6:
                self.random_movie()
            elif choice == 7:
                self.search_movie()
            elif choice == 8:
                self.sorted_movie()
            elif choice == 9:
                self.movie_histogram()
            else:
                print("\033[31m" + "Error! Please choose from numbers 1 to 9." + "\033[0m")
                self.run_manager()
            # To display the menu after executing a command
            enter = input("\033[33m" + "Please enter to continue " + "\033[0m")
            if enter == "":
                self.run_manager()
            else:
                print("\033[31m" + "Error! Please press Enter key to continue" + "\033[0m")
                self.run_manager()


if __name__ == "__main__":
    movies = {
        "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
        "Pulp Fiction": {"rating": 9.6, "year": 1994},
        "The Room": {"rating": 3.6, "year": 2003},
        "The Godfather": {"rating": 9.2, "year": 1972},
        "The Godfather: Part II": {"rating": 9.0, "year": 1974},
        "The Dark Knight": {"rating": 9.0, "year": 2008},
        "12 Angry Men": {"rating": 8.9, "year": 1957},
        "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
        "Forrest Gump": {"rating": 8.8, "year": 1994},
        "Star Wars: Episode V": {"rating": 8.7, "year": 1980}
    }

    manager = MovieManager(movies)

    manager.run_manager()
