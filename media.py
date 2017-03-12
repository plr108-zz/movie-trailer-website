import webbrowser


class Movie():
    """ Movie class: contains information about a specific movie """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ The movie's title """
        self.title = title
        """ URL to an image of the movie's poster """
        self.poster_image_url = poster_image_url
        """ URL to YouTube video of the movie's trailer """
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ Show the movie's trailer in the web browser. """
        webbrowser.open(self.trailer_youtube_url)
