import pandas as pd
import numpy as np
import ast

# Load Data 
# credits = pd.read_csv('./data/cleaned_credits.csv')
# movies = pd.read_csv('./data/cleaned_movies.csv')

# actors = credits[["movie_id", "cast_member_list"]]
# movie_scores = movies[["movie_id", "vote_average"]]

# actors["cast_member_list"] = actors["cast_member_list"].apply(ast.literal_eval)
# actors_expanded = actors.explode("cast_member_list")

# actor_scores = actors_expanded.merge(movie_scores, on="movie_id")

# actor_avg_scores = (
#     actor_scores[['cast_member_list', 'vote_average']]
#     .groupby('cast_member_list')
#     .agg({'vote_average': 'mean', 'cast_member_list': 'count'})
#     .rename(columns={'vote_average':'actor_vote_average','cast_member_list':'movie_count'})
#     .reset_index()
# )

# print(actor_avg_scores[actor_avg_scores.movie_count > 1].sort_values(by='vote_average', ascending=False))

# actor_avg_scores.to_csv('./data/actor_features.csv', index=False)
actor_avg_scores = pd.read_csv("./data/actor_features.csv").rename(columns={'cast_member_list': 'actor', 'vote_average':'actor_vote_average','movie_count':'actor_movie_count'})
movies_and_credits = pd.read_csv('./data/cleaned_movies_NEW.csv')

cast_1_merge = (
    movies_and_credits.merge(actor_avg_scores, how='left', left_on='cast_1', right_on='actor')
                        .rename(columns={'actor_vote_average':'cast_1_vote_average','actor_movie_count':'cast_1_movie_count'})
                        # .drop('cast_member_list_x', axis=1)
                        # .drop('cast_member_list_y', axis=1)
                        .drop('actor', axis=1)
)

cast_2_merge = (
    cast_1_merge.merge(actor_avg_scores, how='left', left_on='cast_2', right_on='actor')
                .rename(columns={'actor_vote_average':'cast_2_vote_average','actor_movie_count':'cast_2_movie_count'})
                # .drop('vote_average_x', axis=1)
                # .drop('cast_member_list_y', axis=1)
)
cast_3_merge = (
    cast_2_merge.merge(actor_avg_scores, how='left', left_on='cast_3', right_on='actor')
                .rename(columns={'actor_vote_average':'cast_3_vote_average','actor_movie_count':'cast_3_movie_count'})
                # .drop('cast_member_list_x', axis=1)
                # .drop('cast_member_list_y', axis=1)
                # .drop('vote_average_x', axis=1)
)
cast_4_merge = (
    cast_3_merge.merge(actor_avg_scores, how='left', left_on='cast_4', right_on='actor')
                .rename(columns={'actor_vote_average':'cast_4_vote_average','actor_movie_count':'cast_4_movie_count'})
                # .drop('cast_member_list_x', axis=1)
                # .drop('cast_member_list_y', axis=1)
                # .drop('vote_average_x', axis=1)
                .drop('actor_x', axis=1)
                .drop('actor_y', axis=1)
                .drop('actor', axis=1)
)

cast_5_merge = (
    cast_4_merge.merge(actor_avg_scores, how='left', left_on='cast_5', right_on='actor')
                .rename(columns={'actor_vote_average':'cast_5_vote_average','actor_movie_count':'cast_5_movie_count'})
                # .drop('cast_member_list_x', axis=1)
                # .drop('cast_member_list_y', axis=1)
                # .drop('vote_average_x', axis=1)
                .drop('actor', axis=1)
)

cast_5_merge.to_csv('./data/cleaned_movies_NEW.csv', index=False)
