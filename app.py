# app.py
import logging
from statistics import median_grouped
from flask import Flask, redirect, url_for, render_template, request, send_file
from file import series_data, get_Episode, get_topones, get_movieolds, get_movieolddetails, get_recommendations

from database import add_data_to_database
from file import get_topones, get_movieolds
from flask_cors import CORS
from datetime import datetime
from file import movies
from file import series_data, get_Episode
from file import get_topones
from file import get_movieolds,get_movieolddetails
from file import get_recommendations, movies, series_data
import binascii
from flask import send_file,jsonify



app = Flask(__name__)
app.secret_key = 'mujyosi'
app.config['SESSION_COOKIE_SECURE'] = True  # Only send cookies over HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Reduce risk of XSS attacks
CORS(app)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

def initialize_app():
    add_data_to_database()  # Populate the database with initial data


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST Request here
        return render_template('index.html')
     # Assuming 'url_friendly_id' is the field in your movies dictionary
    
        
  # Get the latest movies (assuming they have a 'Timestamp' field indicating the upload time)
    latest_movies = sorted(movies.values(), key=lambda x: x.get('Timestamp', datetime.min), reverse=True)[:10]

    # Get the latest series (assuming they have a 'Timestamp' field indicating the upload time)
    latest_series = sorted(series_data.values(), key=lambda x: x.get('Timestamp', datetime.min), reverse=True)[:10]

    return render_template('index.html', latest_movies=latest_movies, latest_series=latest_series)



@app.route('/movie/<movie_id>', methods=['GET', 'POST'])
def moviesdetails(movie_id):
    app.logger.info(f"Received movie_id: {movie_id}")
    
    try:
        movie_id = int(movie_id)
    except ValueError:
        return render_template('error.html', message='Invalid movie ID')

    # Check if the movie_id exists in movies_data
    if movie_id in movies:
        movie = movies[movie_id]
        app.logger.info(f"Found movie: {movie}")

        # Convert details to hexadecimal
        hex_title = binascii.hexlify(movie['Title'].encode()).decode()
        hex_details = binascii.hexlify(movie['Details'].encode()).decode()

        # Get movie recommendations
        recommendations = get_recommendations(movie_id, movies)

        # Pass the movie_id and DownloadLink to the template
        return render_template('moviesdetails.html', movie=movie, recommendations=recommendations,
                               hex_title=hex_title, hex_details=hex_details, movie_id=movie_id)
    else:
        app.logger.info(f"Movie not found for movie_id: {movie_id}")
        # Handle case where movie_id is not found (e.g., show an error page)
        return render_template('error.html', message='Movie not found')


   



@app.route('/download/<movie_id>')
def download_movie(movie_id):
    # Check if the movie_id exists in movies_data
    if movie_id in movies:
        # For simplicity, redirect to a static download link
        return redirect(url_for('static', filename='sample_movie_file.mp4'))
    else:
        # Handle case where movie_id is not found (e.g., show an error page)
        return render_template('error.html', message='Movie not found')




@app.route('/series/')
def series_data_route():
    return render_template ('series.html',series=series_data, serie_id=None)

@app.route('/seriesdetails/<serie_id>', methods=['GET', 'POST'])
def seriesdetails(serie_id):
    if request.method == 'POST':
        # Handle the case where someone clicks without providing values
        return render_template('error.html', message='Invalid request')

    try:
        serie_id = int(serie_id)
    except ValueError:
        return render_template('error.html', message='Invalid series ID')
    

    if serie_id in series_data:
        serie = series_data[serie_id]
        recommendations = get_recommendations(serie_id, series_data)
        return render_template('seriesdetails.html', serie=serie, serie_id=serie_id, recommendations=recommendations)
    
    serie = series_data.get(serie_id)
    if serie:
        
        episodes = serie.get('Episodes', {})
        recommendations = get_recommendations(serie_id, series_data)
        return render_template('seriesdetails.html', serie=serie, episodes=episodes, serie_id=serie_id, recommendations=recommendations)
    else:
        return render_template('error.html', message='Series not found', serie_id=serie_id)

@app.route('/movies/')
def movies_data1 ():
    movieolds_data = get_movieolds()
    return render_template('movies.html', movieolds=movieolds_data)
@app.route('/movieolddetails/<int:movieold_id>')
def movieolddetails(movieold_id):
    movieold = get_movieolddetails(movieold_id)
     # Generate movie recommendations
    moviesolds = get_movieolds()
    recommendations = get_recommendations(movieold_id, moviesolds)
    
    if movieold is None:
        # Handle the case where the movieold_id is not found
        return render_template('error.html', message='Movie not found')

    return render_template('movieolddetails.html', movieold=movieold, recommendations=recommendations)

@app.route('/topones/')

def topones():
    topones_data = get_topones()  # Assuming get_topones() returns a dictionary
    return render_template('topones.html', topones=topones_data)

@app.route('/toponesdetails/<int:topone_id>', methods=['GET', 'POST'])
def toponesdetails(topone_id):
    if request.method == 'POST':
        # Handle the case where someone clicks without providing values
        return render_template('error.html', message='Invalid request')
    top_ones = get_topones()

    topone = top_ones.get(topone_id)

    if topone:
        return render_template('toponesdetails.html', topone=topone)
    else:
        return render_template('error.html', message='Movie not found', topone_id=topone_id)
# Add a new route to handle search queries and display results
@app.route('/search', methods=['GET'])
def search_results():
    query = request.args.get('query')

    # Call the correct function to get movie data
    movies_data = movies

    if movies_data:
        # Filter movies that match the search query
        matching_movies = {movie_id: movie for movie_id, movie in movies_data.items() if query.lower() in movie['Title'].lower()}
    else:
        matching_movies = {}

    # Filter series that match the search query
    matching_series = {}

    if series_data:
        # Filter series that match the search query
        matching_series = {series_id: series for series_id, series in series_data.items() if query.lower() in series['Title'].lower()}

    # Choose a specific serie_id based on your logic (e.g., first result)
    serie_id = next(iter(matching_series.keys()), None)

    # Choose a specific movie_id based on your logic (e.g., first result)
    movie_id = next(iter(matching_movies.keys()), None)

    # Pass 'serie_id' and 'movie_id' to the context
    return render_template('search_results.html', query=query, movies=matching_movies, series=matching_series, serie_id=serie_id, movie_id=movie_id)


if __name__=="__main__":
    app.run