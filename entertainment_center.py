import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
#print(toy_story.storyline)
avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=-9ceBgWV8io')
#print(avatar.storyline)
#avatar.show_trailer()
tropic_thunder = media.Movie('Tropic Thunder',
                     'Through a series of freak occurrences, a group of actors shooting a big-budget war movie are forced to become the soldiers they are portraying',
                     'https://images-na.ssl-images-amazon.com/images/I/51AQVt%2BAIVL.jpg',
                     'https://www.youtube.com/watch?v=T-6YhRZowgc')
#print(tropic_thunder.storyline)
#tropic_thunder.show_trailer()

movies = [toy_story, avatar, tropic_thunder]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__name__)
print(media.Movie.__module__)
