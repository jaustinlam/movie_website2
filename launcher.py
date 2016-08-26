import media
import fresh_tomatoes

godfather = media.Movie("The Godfather",
  "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
  "https://www.youtube.com/watch?v=sY1S34973zA")

bourne_identity = media.Movie("The Bourne Identity",
  "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
  "https://www.youtube.com/watch?v=PGKK5wACwrU")

casino = media.Movie("Casino",
  "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",
  "https://www.youtube.com/watch?v=EGNx3ilNB80")

forrest_gump = media.Movie("Forrest Gump",
  "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
  "https://www.youtube.com/watch?v=8eCIRKJdV4k")

he_got_game = media.Movie("He Got Game",
  "https://upload.wikimedia.org/wikipedia/en/thumb/4/4e/He_got_game_poster.jpg/220px-He_got_game_poster.jpg",
  "https://www.youtube.com/watch?v=yIhthvNiPR4")

fast_and_furious = media.Movie("The Fast and Furious",
"https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Fast_and_the_furious_poster.jpg/220px-Fast_and_the_furious_poster.jpg",
"https://www.youtube.com/watch?v=kJdNBEHTGPg")

maria_full_of_grace = media.Movie("Maria Full of Grace",
"https://upload.wikimedia.org/wikipedia/en/thumb/b/b4/Maria_Full_of_Grace_movie.jpg/220px-Maria_Full_of_Grace_movie.jpg",
"https://www.youtube.com/watch?v=afhNync9A6A")

spirited_away = media.Movie("Spirited Away",
"https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Spirited_Away_poster.JPG/220px-Spirited_Away_poster.JPG",
"https://www.youtube.com/watch?v=ByXuk9QqQkk")

movies = [godfather, bourne_identity, casino, forrest_gump, he_got_game, fast_and_furious, maria_full_of_grace, spirited_away]

fresh_tomatoes.open_movies_page(movies)
