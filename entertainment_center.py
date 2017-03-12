import fresh_tomatoes
import media

tropic_thunder = media.Movie(
    'Tropic Thunder',
    'https://images-na.ssl-images-amazon.com/images/I/51AQVt%2BAIVL.jpg',
    'https://www.youtube.com/watch?v=T-6YhRZowgc')

iron_man = media.Movie(
    'Iron Man',
    'http://www.impawards.com/2008/posters/iron_man_ver3.jpg',
    'https://www.youtube.com/watch?v=7H0yo-lDuk0')

the_matrix = media.Movie(
    'The Matrix',
    'http://www.impawards.com/1999/posters/matrix_ver1.jpg',
    'https://www.youtube.com/watch?v=vKQi3bBA1y8')

wedding_singer = media.Movie(
    'The Wedding Singer',
    'http://assets.flicks.co.nz/images/movies/poster/ca/' +
    'ca172e964907a97d5ebd876bfdd4adbd_500x735.jpg',
    'https://www.youtube.com/watch?v=_bhU3NsCIDs')

pulp_fiction = media.Movie(
    'Pulp Fiction',
    'https://www.movieposter.com/posters/archive/main/16/A70-8455',
    'https://www.youtube.com/watch?v=tGpTpVyI_OQ')

eternal_sunshine = media.Movie(
    'Eternal Sunshine of the Spotless Mind',
    'https://pics.filmaffinity.com/' +
    'Eternal_Sunshine_of_the_Spotless_Mind-487862604-large.jpg',
    'https://www.youtube.com/watch?v=GBEke6JixyE')

movies = [
    tropic_thunder, wedding_singer, iron_man,
    the_matrix, pulp_fiction, eternal_sunshine]
# show the movies on the movies web page
fresh_tomatoes.open_movies_page(movies)
