# file.py
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from datetime import datetime
import random
def get_recommendations(current_id, data,num_recommendations=5):
    recommended_ids = [id for id in data if id !=current_id]
    random.shuffle(recommended_ids)
    recommended_ids = recommended_ids[:num_recommendations]

    recommendations =[(id, data[id]['image']) for id in recommended_ids]
    return recommendations


movies = {
        1: {'id':1,'Title': 'avengers', 'Year': 2022, 'image': 'money heist.jpg', 'Details': 'Description for Movie 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        2: {'id':2,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        3: {'id':3,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        4: {'id':4,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        5: {'id':5,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        6: {'id':6,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        7: {'id':7,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        8: {'id':8,'Title': 'avengers', 'Year': 2021, 'image': 'money heist.jpg', 'Details': 'Description for Movie 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        # Add more movies as needed
    }
   
# Example Series Data
series_data = {
    101: {'id': 101, 'Title': 'Series 1', 'Year': 2020, 'image': 'avengers.jpg', 'Details': 'Description for Series 1', 'DownloadLink': 'series1.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    102: {'id': 102, 'Title': 'Series 2', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    103: {'id': 103, 'Title': 'Series 3', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    104: {'id': 104, 'Title': 'Series 4', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    105: {'id': 105, 'Title': 'Series 5', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    106: {'id': 106, 'Title': 'Series 5', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    106: {'id': 106, 'Title': 'Series 5', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    107: {'id': 107, 'Title': 'Series 5', 'Year': 2019, 'image': 'avengers.jpg', 'Details': 'Description for Series 2', 'DownloadLink': 'series2.zip',
          'Episodes': {1: {'Title': 'Episode 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
                       2: {'Title': 'Episode 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'}},
          'Timestamp': datetime(2020, 1, 1, 12, 0, 0)},
    
    # Add more series as needed
}

def get_series_data(series_id=None):
    if series_id is not None:
        return series_data.get(series_id)
    else:
        return series_data
def get_Episode(series_id, episode_id):
    series = series_data.get(str(series_id))
    if series:
        return series.get('Episodes', {}).get(episode_id, None)
    return None
# Example Top Ones Data
def get_topones():
    topones = {
        1001: {'Title': 'Top One 1', 'image': 'avengers.jpg', 'Details': 'Description for Top One 1','DownloadLink':'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        1002: {'Title': 'Top One 2', 'image': 'avengers.jpg', 'Details': 'Description for Top One 2','DownloadLink':'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
        # Add more top ones as needed
    }
    return topones

# Example Movie Olds Data
moviesolds = {
    201: {'id':1,'Title': 'Movie Old 1', 'comments': [], 'Year': 2000, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 1', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    202: {'id':2,'Title': 'Movie Old 2', 'comments': [], 'Year': 1995, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    203: {'id':3,'Title': 'Movie Old 3', 'comments': [], 'Year': 1995, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    204: {'id':4,'Title': 'Movie Old 4', 'comments': [],'Year': 1995, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    205: {'id':5,'Title': 'Movie Old 5', 'comments': [],'Year': 1995, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    206: {'id':6,'Title': 'Movie Old 6', 'comments': [] ,'Year': 1995, 'image': 'avengers.jpg', 'Details': 'Description for Movie Old 2', 'DownloadLink': 'https://www.mediafire.com/file/v4ugzpn5ai0cxm8/Love_at_first_kiss.mp4/file'},
    
    # Add more movie olds as needed
}

def get_movieolds():
    return moviesolds

def get_movieolddetails(movieold_id):
    moviesolds = get_movieolds()  # Assuming you have a function get_movieolds to retrieve the movies dictionary
    movieold = moviesolds.get(movieold_id)
    return movieold



# ... (your other imports and functions)

