import pandas as pd
import numpy as np
import ast


# This script takes in the raw IMDB csv's and outputs a cleaned csv with new features/columns added.
# The script uses relative file paths so be sure to set your working directory correctly

# Load Data 
movies_raw = pd.read_csv('tmdb_5000_movies.csv')
credits_raw = pd.read_csv('tmdb_5000_credits.csv')

movies = movies_raw.copy()
credit = credits_raw.copy() 

# Clean Data 
# Remove no relase date
# Remove "Rumoured" (5) and "Post Production" (3) movies by filtering to "Released"
movies = movies[(movies.status == 'Released') & 
                (movies.release_date.notna())]


######################### Movies #####################################
# Change string lists of dictionaries to actual lists of dictionaries
movies['spoken_languages'] = movies['spoken_languages'].apply(ast.literal_eval)
movies['genres'] = movies['genres'].apply(ast.literal_eval)
movies['keywords'] = movies['keywords'].apply(ast.literal_eval)
movies['production_companies'] = movies['production_companies'].apply(ast.literal_eval)
movies['production_countries'] = movies['production_countries'].apply(ast.literal_eval)


# Create Columns
# Extract release month and year as columns. Also the day of week  
movies['release_year'] = pd.DatetimeIndex(movies['release_date']).year
movies['release_month'] = pd.DatetimeIndex(movies['release_date']).month
movies['day_of_week_release'] = pd.DatetimeIndex(movies['release_date']).dayofweek

# Create column for "if has homepage"
movies['has_homepage'] = movies['homepage'].apply(lambda x: 0 if pd.isna(x) else 1)

# Create columns for the number of spoken languages, production companies, genres
movies['num_spoken_languages'] = movies['spoken_languages'].apply(lambda x: len(x))
movies['num_production_companies'] = movies['production_companies'].apply(lambda x: len(x))
movies['num_genres'] = movies['genres'].apply(lambda x: len(x))

#  Create a set of unique genre names
unique_genres = set()

for row in movies['genres']:
    for genre_dict in row:
        unique_genres.add(genre_dict['name'])

# Iterate through unique genre names and create columns 
for genre_name in unique_genres:
    genre_name = genre_name.replace(" ", "_")
    movies[f'genre_{genre_name}'] = 0

# Populate the columns with 1s or 0s based on the presence of each genre
for index, row in movies.iterrows():
    for genre_dict in row['genres']:
        genre_name = genre_dict['name']
        genre_name = genre_name.replace(" ", "_")
        movies.at[index, f'genre_{genre_name}'] = 1
        
# Create a column for if that movie has a homepage
        
# Find number of unique production_companies out of curiosity (5015)        
unique_production = set()

for row in movies['production_companies']:
    for production_dict in row:
        unique_production.add(production_dict['name'])        
 
        
# Find number of unique keywords out of curiosity   (9806)     
unique_keywords = set()

for row in movies['keywords']:
    for keyword_dict in row:
        unique_keywords.add(keyword_dict['name'])


# Create a column that has the keywords in a list 

keywords_list = []

for row in movies['keywords']:
    out = []
    for keyword_dict in row:
        out.append(keyword_dict['name'])
    
    keywords_list.append(out)
    
movies['keywords_list'] = keywords_list


# Create a column that has the production companies in a list 

companies_list = []

for row in movies['production_companies']:
    out = []
    for production_dict in row:
        out.append(production_dict['name'])
    
    companies_list.append(out)
    
movies['production_companies_list'] = companies_list


# Create a column that has the production countries in a list 

countries_list = []

for row in movies['production_countries']:
    out = []
    for countries_dict in row:
        out.append(countries_dict['name'])
    
    countries_list.append(out)
    
movies['production_countries_list'] = countries_list

# Remove unnecessary columns
movies = movies.drop(columns = ['genres','keywords','production_companies','production_countries','spoken_languages'])

movies = movies.rename(columns={'id':'movie_id'})

movies.to_csv('cleaned_movies.csv', index=False)

## Notes about movies
# 1031 have 0 as the budget value 
# 1419 have 0 revenue 

######################### Credits #####################################

# Change string lists of dictionaries to actual lists of dictionaries
credit['cast'] = credit['cast'].apply(ast.literal_eval)
credit['crew'] = credit['crew'].apply(ast.literal_eval)

# Create column with size of cast 
credit['cast_size'] = credit['cast'].apply(len)

# Filter to only the top 5 cast members
credit['cast_members'] = credit['cast'].apply(lambda x: x[:5])     
    

# Find number of unique cast members out of curiosity (9390)     
unique_cast = set()

for row in credit['cast_members']:
    for members_dict in row:
        unique_cast.add(members_dict['name'])
        

# Create a column that has the top 5 cast in a list 
cast_list = []

for row in credit['cast_members']:
    out = []
    for cast_dict in row:
        out.append(cast_dict['name'])
    
    cast_list.append(out)
    
credit['cast_member_list'] = cast_list


# Create cast_1, cast_2, cast_3 etc. columns 
for i in range(5):
    credit[f'cast_{i+1}'] = credit['cast_member_list'].apply(lambda x: x[i] if len(x) > i else None)


# Remove unnecessary columns
credit = credit.drop(columns = ['crew','cast','cast_members','title'])

credit.to_csv('cleaned_credits.csv', index=False)

## Notes about credits
# 86 Movies in the credits_raw csv have a record but no cast data behind it 


######################### Movies & Credits #####################################

# Join movies and credits on movie_id

movies_credits = pd.merge(movies, credit, on = 'movie_id', how = 'left')

movies_credits.to_csv('cleaned_movie_and_credits.csv', index=False)


######################### Display Stats #####################################

selected_columns = ['budget','popularity','revenue','runtime','vote_average','vote_count','cast_size']

summary = movies_credits[selected_columns].describe()

print(summary)