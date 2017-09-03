"""Main file for the movie trailer website."""
from movie import Movie
import fresh_tomatoes


fresh_tomatoes.open_movies_page(movies=[
    Movie(
        "Misery",
        "A novellist is rescued from a car accident by a fan.",
        r"https://upload.wikimedia.org/wikipedia/en/b/b4/Miseryposter.jpg",
        r"https://www.youtube.com/watch?v=ptpaEntid74",
        "R"
    ),
    Movie(
        "The Wailing",
        "A stranger arrives in a little village and soon after a mysterious" +
        "sickness starts spreading. A policeman is drawn into the incident" +
        " and is forced to solve the mystery in order to save his daughter.",
        r"https://upload.wikimedia.org/wikipedia/en/e/eb/The_Wailing_" +
        "%28film%29.png",
        r"https://www.youtube.com/watch?v=43uAputjI4k",
        "R"
    ),
    Movie(
        "The Audition",
        "A widower takes an offer to screen girls at a special audition, " +
        "arranged for him by a friend to find him a new wife. The one he " +
        "fancies is not who she appears to be after all.",
        r"http://www.gstatic.com/tv/thumb/movieposters/29706/p29706_p_v8_aa" +
        ".jpg",
        r"https://www.youtube.com/watch?v=OC3jCY4h0H0",
        "R"
    ),
    Movie(
        "It Follows",
        "A young woman is followed by an unknown supernatural force after a" +
        " sexual encounter.",
        r"http://t1.gstatic.com/images?q=tbn:ANd9GcSm4UbnFzQQ7zvlGqklBVuQOp" +
        "EpoIDo5IifFHh8GRwKv5pCiauC",
        r"https://www.youtube.com/watch?v=Ymoh5SIqgtw",
        "R"
    ),
    Movie(
        "The Thing",
        "A research facility in Antarctica comes across an alien force that " +
        "can become anything it touches with 100% accuracy. The members must" +
        " now find out who's human and who's not before it's too late.",
        r"http://t1.gstatic.com/images?q=tbn:ANd9GcS8_TRLy8QuX-FGMlNnlM56gkp" +
        "nk8wTzLGH4pYOufwK4ajSqFvv",
        r"https://www.youtube.com/watch?v=p35JDJLa9ec",
        "R"
    ),
    Movie(
        "Pontypool",
        "A radio host interprets the possible outbreak of a deadly virus " +
        "which infects the small Ontario town he is stationed in.",
        r"http://www.gstatic.com/tv/thumb/dvdboxart/195169/p195169_d_v8_aa" +
        ".jpg",
        r"https://www.youtube.com/watch?v=Ehq2a8lum_4",
        "R"
    )
])
