from imdbpie import Imdb
import pprint
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')


imdb = Imdb()

endgame = imdb.get_title_user_reviews("tt4154796")
avatar = imdb.get_title_user_reviews("tt0499549")
titanic = imdb.get_title_user_reviews("tt0120338")
starwars = imdb.get_title_user_reviews("tt2488496")
infinity = imdb.get_title_user_reviews("tt4154756")
jurassic = imdb.get_title_user_reviews("tt0369610")
lionking = imdb.get_title_user_reviews("tt6105098")
avengers = imdb.get_title_user_reviews("tt0848228")
furious = imdb.get_title_user_reviews("tt2820852")
frozen = imdb.get_title_user_reviews("tt4520988")
movies = [endgame,avatar, titanic, starwars, infinity, jurassic ,lionking, avengers,furious, frozen]
movies_string = ["endgame", "avatar", "titanic", "starwars", "infinity", "jurassic" , "lionking" , "avengers", "furious", "frozen"]
# pprint.pprint(avengers)
# print(avengers_reviews['reviews'][1]['author']['displayName'])
# print(endgame['reviews'][1]['reviewText'])
# print(len(avengers_reviews))

def new_list(review):
    """Takes review directly from IMDB and adds it to its own list"""
    all = []
    for line in review['reviews'][1]['reviewText'].split():
        line = line.lower()
        all.append(line)
    return all

def histogram(reviews):
    """returns dictionary of how many times each word in a review appears"""
    d = dict()
    for line in reviews:
        if line not in d:
            d[line] = 1
        else:
            d[line] = d[line]+1
    return d

def main():
    """Runs the above 2 functions for every movie in the list of movie names and performs sentiment analysis on the review"""
    i = 0
    for movie in movies:
        review = movie
        new_hist = histogram(new_list(review))
        sort_histogram = sorted(new_hist.items(),key=lambda x: x[1], reverse = True)
        print(movies_string[i])
        pprint.pprint(sort_histogram)
        score = SentimentIntensityAnalyzer().polarity_scores(review['reviews'][1]['reviewText'])
        print(score)
        i = i+ 1


if __name__ == "__main__":
    main()


