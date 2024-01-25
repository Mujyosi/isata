# database.py

from sqlalchemy.orm import sessionmaker
from models import Movie, Series, Episode, TopOne, engine

Session = sessionmaker(bind=engine)

def add_data_to_database():
    session = Session()

    # Example data for movies
    movies_data = {
        1: {
            "id": 1,
            "title": "They Shall Not Grow Old",
            "year": 2018,
            "image": "images/money heist.jpg",
            "details": "hekl fight kill them there is no time",
            "download_link": "/download/1"
        },
        # Add other movies here
    }

    # Example data for series
    series_data = {
        1: {
            "id": 1,
            "title": "Breaking Bad",
            "year": 2008,
            "image": "images/breaking_bad.jpg",
            "details": "Meth and high school chemistry",
            "download_link": "/download/1"
        },
        # Add other series here
    }

    # Example data for topones
    topones_data = {
        1: {
            "id": 1,
            "title": "TopOne Movie",
            "year": 2022,
            "image": "Image/avengers.jpg",
            "details": "An amazing top one movie",
            "download_link": "/download/topone"
        },
        # Add other topones here
    }

    # Add movies to the database
    for movie_id, movie_info in movies_data.items():
        session.add(Movie(id=movie_id, **movie_info))

    # Add series to the database
    for series_id, series_info in series_data.items():
        session.add(Series(id=series_id, **series_info))

    # Add topones to the database
    for topone_id, topone_info in topones_data.items():
        session.add(TopOne(id=topone_id, **topone_info))

    session.commit()
    session.close()

if __name__ == "__main__":
    add_data_to_database()
