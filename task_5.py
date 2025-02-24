"""Task 5

Given a dictionary where movie names are keys and their respective ratings (out of 10) are values, determine:

movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

# Expected Output:
# Highest Rated Movie: The Dark Knight (9.0)
# Top 3 Movies: [('The Dark Knight', 9.0), ('Parasite', 8.9), ('Inception', 8.8)]
# Average Rating: 8.74"""

movie_ratings = {
    "Inception": 8.8,
    "Interstellar": 8.6,
    "Parasite": 8.9,
    "The Dark Knight": 9.0,
    "Avengers: Endgame": 8.4
}

# The highest-rated movie.
def highest_rated_movie(movie_ratings):
    max_rated=max(movie_ratings,key=movie_ratings.get)
    print(f"\n 1) The highest rated movie is {max_rated} with {max(movie_ratings.values())}")

# The top 3 movies sorted by rating.
def top3_movies(movie_ratings):
    sorted_ratings=sorted(movie_ratings.items(),key=lambda  x:x[1],reverse=True)
    top3=slice(3)
    final_top3=sorted_ratings[top3]
    print("\n 2) The top 3 movies sorted by rating are:", final_top3)

# The average movie rating
def avg_movie_ratings(movie_ratings):
    total_ratings=sum(movie_ratings.values())
    no_of_movies=len(movie_ratings)
    avg_of_movies=total_ratings/no_of_movies
    print(f"\n 3) The average movie rating is: {avg_of_movies}")

highest_rated_movie(movie_ratings)
top3_movies(movie_ratings)
avg_movie_ratings(movie_ratings)




