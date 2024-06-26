from mmovie_app.movie_specification.movie import Movie
from mmovie_app.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []  # contains all the movies (objects)
        self.users_collection = []  # contains all the users (objects)

    def register_user(self, username: str, age: int):

        for u in self.users_collection:
            if u.username == username:
                raise Exception("User already exists!")

        user = User(username, age)

        if user not in self.users_collection:
            self.users_collection.append(user)
            return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie in self.movies_collection or movie in user.movies_owned:
                    raise Exception("Movie already added to the collection!")
                if movie.owner != user:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")
                user.movies_owned.append(movie)
                self.movies_collection.append(movie)
                return f"{username} successfully added {movie.title} movie."

        raise Exception("This user does not exist!")

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        for user in self.users_collection:
            if user.username == username:
                if movie.owner != user:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")
                for key, value in kwargs.items():
                    setattr(movie, key, value)
                return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        for user in self.users_collection:
            if user.username == username:
                if movie.owner != user:
                    raise Exception(f"{username} is not the owner of the movie {movie.title}!")

                if movie in user.movies_owned:  # tova go pisah az i e novo
                    user.movies_owned.remove(movie)
                    self.movies_collection.remove(movie)
                    return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie.owner == user:
                    raise Exception(f"{username} is the owner of the movie {movie.title}!")
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
                user.movies_liked.append(movie)
                movie.likes += 1
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie not in user.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")

                if movie in user.movies_liked:  # oshte edna proverka ot men
                    user.movies_liked.remove(movie)
                    movie.likes -= 1
                    return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:  # ??
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return "\n".join(movie.details() for movie in sorted_movies)

    def __str__(self):
        result = "All users: "
        if not self.users_collection:
            result += "No users."
        all_usernames = []
        for user in self.users_collection:
            all_usernames.append(user.username)
        result += f"{', '.join(all_usernames)}\nAll movies: "
        if not self.movies_collection:
            result += "No movies."
        all_titles = []
        for movie in self.movies_collection:
            all_titles.append(movie.title)
        result += f"{', '.join(all_titles)}"

        return result
