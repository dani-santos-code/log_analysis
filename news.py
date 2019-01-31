#!/usr/bin/env python3
#

from newsdb import (get_top_three_articles,
                    get_most_popular_authors,
                    get_over_one_percent_error)

def main():
    # Main page of the reports.
    top_three_articles = get_top_three_articles()
    most_popular_authors = get_most_popular_authors()
    over_one_percent_error = get_over_one_percent_error()

    print(top_three_articles)
    print('-' * 10)
    print(most_popular_authors)
    print('-' * 10)
    print(over_one_percent_error)
