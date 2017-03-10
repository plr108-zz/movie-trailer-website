import fresh_tomatoes
import media
import random

tropic_thunder = media.Movie('Tropic Thunder',
                             'Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying',
                             'https://images-na.ssl-images-amazon.com/images/I/51AQVt%2BAIVL.jpg',
                             'https://www.youtube.com/watch?v=T-6YhRZowgc')

spotless = media.Movie('Eternal Sunshine of the Spotless Mind',
                       'When their relationship turns sour, a couple undergoes a procedure to have each other erased from their memories. But it is only through the process of loss that they discover what they had to begin with.',
                       'https://pics.filmaffinity.com/Eternal_Sunshine_of_the_Spotless_Mind-487862604-large.jpg',
                       'https://www.youtube.com/watch?v=GBEke6JixyE')

iron_man = media.Movie('Iron Man',
                       'After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.',
                       'http://www.impawards.com/2008/posters/iron_man_ver3.jpg',
                       'https://www.youtube.com/watch?v=7H0yo-lDuk0')

the_matrix = media.Movie('The Matrix',
                         'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                         'http://www.impawards.com/1999/posters/matrix_ver1.jpg',
                         'https://www.youtube.com/watch?v=vKQi3bBA1y8')

wedding_singer = media.Movie('The Wedding Singer',
                             'Robbie, a singer, and Julia, a waitress, are both engaged, but to the wrong people. Fortune intervenes to help them discover each other.',
                             'http://assets.flicks.co.nz/images/movies/poster/ca/ca172e964907a97d5ebd876bfdd4adbd_500x735.jpg',
                             'https://www.youtube.com/watch?v=_bhU3NsCIDs')

pulp_fiction = media.Movie('Pulp Fiction',
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           'https://www.movieposter.com/posters/archive/main/16/A70-8455',
                           'https://www.youtube.com/watch?v=tGpTpVyI_OQ')
movies = [tropic_thunder,spotless,iron_man,the_matrix,wedding_singer,pulp_fiction]
# randomize the order of movies
random.shuffle(movies)
fresh_tomatoes.open_movies_page(movies)
