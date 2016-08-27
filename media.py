import webbrowser

class Movie():

    """Movie class creates attributes for movies"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """Intializes the Movie class"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the browser and displays trailer website"""
        webbrowser.open(self.trailer_youtube_url)



  
