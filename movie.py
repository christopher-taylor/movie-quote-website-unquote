"""Contains the movie class definition."""
import webbrowser


class Movie():
    """An object that represents a given movie that.

    Holds all the information about a movie that will be surfaced on the site.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, description, cover, trailer_url, rating):
        """Create a new instance of the Movie class."""
        self.title = title
        self.description = description
        self.poster_image_url = cover
        self.trailer_youtube_url = trailer_url
        if rating in Movie.VALID_RATINGS:
            self.rating = rating
        else:
            raise AssertionError("The provided rating is invalid.")

    def __str__(self):
        """Create a text representation of the movie."""
        string = 'Title: ' + self.title + '\r\nDescription: ' \
            + self.description + '\r\nCover: ' + self.poster_image_url + \
            '\r\nTrailer Link: ' + self.trailer_youtube_url
        return string

    def __repr__(self):
        """Allow the object to represent itself."""
        return {
            "title": self.title,
            "description": self.description,
            "cover": self.poster_image_url,
            "trailer": self.trailer_youtube_url
        }

    def show_trailer(self):
        """Open a browser and play the movies trailer."""
        webbrowser.open(self.trailer_youtube_url)
