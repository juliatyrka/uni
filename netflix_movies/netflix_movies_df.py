# netflix_data.csv description:
# columns: show_id, type, title, director, cast, country, date_added, release_year, duration, description, genre

import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv('netflix_data.csv')

#Filter the data for movies released in the 1990s
realeased_1990 = netflix_df[netflix_df['release_year'] == 1990]

#The most frequent duration in 1990s, plot
dur = realeased_1990['duration']
plt.hist(dur)
plt.xticks([0,40,80,100,120,140,180])
plt.show()

#Mean
duration_mean = int(dur.mean())
print(f'Duration mean: {duration_mean}')

#Count the number of short action movies in 1990s
genre_1990 = realeased_1990['genre']
plt.hist(genre_1990)
plt.show()
print(genre_1990)

#Filter the DataFrame for movies released in the 1990s, of type 'Movie', genre 'Action', and duration < 90 minutes
short_movie = netflix_df[(netflix_df['genre'] == 'Action') & (netflix_df['release_year'] >= 1990) &
                         (netflix_df['release_year'] < 2000) & (netflix_df['type'] == 'Movie') & (netflix_df['duration'] < 90)]

short_movie_count = len(short_movie)
print(f"Short movies count: {short_movie_count}")
