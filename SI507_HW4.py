# SI 507 - Homework 4
# Note the changed name (Lab -> Homework)

# Instructions all provided in this file.
# IMPORTANT: Please read ALL of the instructions for each part before starting on it.

# Submit this edited code file (only) to HW 4 on Gradescope via Canvas to see test results!

## Your import statements for use in the program (both things installed wih pip & things that come default with Python) should go here!
import pandas as pd
import numpy as np
from enum import Enum, unique
from itertools import permutations
import random

#####################

## [PART 1]
# Provided is a dataset: movies_dataset_group.csv
# Your first goal is to write code to "clean" this dataset a little bit and produce a cleaned version of the dataset in a file called movies_clean.csv.

# NOTE that there are MANY ways to clean up a dataset programmatically. Many common ways will use a module to do so -- pandas is a common one.
# If you take SI 618, you will use/are using the Pandas module in that course! You are welcome to use that here. (Just make sure you indicate in imports and requirements everything you need.)
# However, you do not NEED to use Pandas to do this. Think carefully about what it is you need to achieve for these specific goals, and then try some things out.
# You MAY (but do NOT have to) use any of the following modules, but NOT others, for this particular lab:
# pandas, xlrd, scipy, numpy
# HINT: The CSV module (built into Python) is probably going to be very useful , and using list and/or dictionary methods may also be useful!

# The following things should be true of movies_clean.csv:

# - Every missing cell should no longer be blank -- instead, anything missing should contain the string "NA" TODO
## NOTE: "Not Rated" IS information about rating, and should remain; don't get rid of that information. TODO

# - TODO Dates should be considered missing (and become "NA" values) if they are not in the format DD-Month-YY (e.g. 23-Apr-98). Any date in the format D-Month-YY (e.g. 3-Apr-94) should have a 0 at the front.
### ***NOTE - it is possible for a starting 0 to exist and not show up in certain display options/software -- so if it's not showing up and you're SURE it's there, test by opening the .CSV in a text editor or the command prompt first!

# You may achieve these goals and create movies_clean.csv in any way you like, as long as it's done with Python code.

# Tests for this part are testing movies_clean.csv, which *should have been generated by the program* -- do NOT submit that file, only submit your program file.

def clean_data():
    csv_df = pd.read_csv("movies_dataset_group.csv")

    # apply to all elements, regardless of column
    cleaned_csv_df = csv_df.fillna("NA")
    cleaned_csv_df['Release Date']

    # TODO: validate datetime
    i = 0
    for index, release_date in enumerate(cleaned_csv_df['Release Date']):
        tokens = release_date.strip().split('-')
        if len(tokens[0]) == 1:
            cleaned_csv_df.loc[index, 'Release Date'] = '-'.join(
                [f"0{tokens[0]}"]+tokens[1:]
            )
            # print(index, release_date, type(release_date), '=>', cleaned_csv_df.loc[index, 'Release Date'])
        i += 1

    cleaned_csv_df.to_csv("movies_clean.csv")
    return cleaned_csv_df

cleaned_csv_df = clean_data()

## [PART 2]

# TODO If you take all the movie ratings available in the dataset (G, PG, PG-13, R, NC-17 .. do not count Not Rated movies here) -- what is the *median* rating of the rated movies? Save the result in a variable median_rating (whose value should be a string representing a rating, e.g. "G" or "PG-13" or "R" or whatever it is).

# TODO To do this, you should convert the ratings to numbers,  starting at 1 for G rating and counting up (1,2,3,4,5), where 5 represents NC-17.
# HINT: Creating a dictionary may be useful in this process!
# If you find that the median result is a decimal in between two of these integers, round to the closest one to find your answer. (And if you do not know what a median is, check this out: https://en.wikipedia.org/wiki/Median )


# You may use one of the modules listed in part 1 to help you with this, but you do not necessarily need to.

# Use code to compute this (by opening the data file and manipulating the data in some way) and to assign the median_rating variable correctly, which we will test.


@unique
class MpaaRating(Enum):
    G = 1
    PG = 2
    PG_13 = 3
    R = 4
    NC_17 = 5

    def to_string(self):
        return self.name.replace('_', '-')
    
def transform_data(df):
    # map PG... to numbers
    mpaa_rating_categorical = pd.Categorical(
        df['MPAA Rating'],
        categories=[ mapp_rate.to_string() for mapp_rate in MpaaRating ],
        ordered=False
    )

    # sanitize data
    mpaa_rating_series = pd.Series(mpaa_rating_categorical).dropna()

    # numerify
    mpaa_rating_numeric = mpaa_rating_series.replace(
        [ mapp_rate.to_string() for mapp_rate in MpaaRating ],
        [ mapp_rate.value for mapp_rate in MpaaRating ]
    )

    # calculate median of ratings
    mpaa_median = mpaa_rating_numeric.median()
    return MpaaRating(int(round(mpaa_median))).to_string()

median_rating = transform_data(cleaned_csv_df)

## [PART 3]
# We want to play a "game" (sort of) about making up new movies. Use the itertools library and the clean movies_clean.csv data you've created to have your program repeatedly create 10 new movie titles and ratings, print them out neatly (see below for an example), and save a string with all of them (like below) in a variable called sample_fake_movies.

# NOTE that this part of the lab may NOT be graded entirely by tests (it may be sat least partially graded by humans). So you should make sure you test it yourself to see that it does what it should.

# We're grading on whether you achieved the objectives listed below for the results of running this program.

# Requirements:
# - The 10 fake movie titles & ratings this game prints out should differ in some way each time you run the program -- e.g. randomness (via the random library, perhaps?) should be introduced somewhere.
# - Each of your new movie titles should be no more than six words long OR no more than 45 characters long. (Pick either one of those two constraints.)
# - The resulting string saved in sample_fake_movies should have at least 10 lines, and each line should have 1 movie title and rating in it -- no blank lines. See the EXAMPLE below for formatting guidelines/example.
# - This "game" should be something that happens on running this program -- it should NOT be something that depends on any user input. (A file with user input won't run in Gradescope!)
# - Combination of information must be more creative than existing movie titles with new ratings. Think along the lines of mixing up words in movie titles somehow. (It's OK if they don't make sense to us humans!)
# At least one tool/function from the itertools library must be used.
# It is okay to use more than one itertools function in different ways, or to create more than 10 movies on each run, but each time, at least 10 new movies + ratings must be created and printed.

# For example, here's one of millions of possible/reasonable outputs in the below string. The value of your sample_fake_movies variable should be something like this:          

"""
Say Seabiscuit - G
The Real Romeo - R
Rescue American The - PG-13
Damned Queen of the - PG
Perrier's Peter - R
Getaway I Pink You The Once - PG
Eleven Twelve Thirteen - PG-13
Wild Novocaine - PG
My With the of Why Narc Into - Not Rated
My My My The - G
"""

print("\n\nNEW FAKE MOVIE TITLES CREATED BELOW...\n\n")
# Write your code to enact all of this below

def get_creative_titles(movie_title_df):
    # print("Sampling csv...")
    sampled_movie_titles = movie_title_df[
        (movie_title_df['Title'].str.len() <= 45) & (movie_title_df['Title'].str.contains(' '))
    ].sample(10)

    # print("Generating 10 creative movies...")
    # pairs = []
    large_string = ''
    for movie_title in sampled_movie_titles['Title']:
        tokens = list(map(lambda t: t.capitalize(), movie_title.strip().lower().split()))
        perms = permutations(tokens)
        all_possible_titles = [ ' '.join(token_comp) for token_comp in perms ]
        random.shuffle(all_possible_titles)

        creative_title = all_possible_titles[0] if all_possible_titles[0] != movie_title else all_possible_titles[1]
        # if all_possible_titles[0].lower() != movie_title.lower():
        #     creative_title = all_possible_titles[0]
        # else:
        #     continue
        
        mpaa_rating = random.choice(list(MpaaRating)).to_string()
        # pairs.append((creative_title, mpaa_rating))
        large_string += f"{creative_title} - {mpaa_rating}\n"
    
    print(large_string)

    return large_string
  
sample_fake_movies = get_creative_titles(cleaned_csv_df[['Title', 'MPAA Rating']])