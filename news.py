#!/usr/bin/env python3
#

from flask import Flask, render_template
from newsdb import (get_top_three_articles,
                    get_most_popular_authors,
                    get_over_one_percent_error)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    # Main page of the reports.
    top_three_articles = get_top_three_articles()
    most_popular_authors = get_most_popular_authors()
    over_one_percent_error = get_over_one_percent_error()

    return render_template(
        "index.html",
        top_three_articles=top_three_articles,
        most_popular_authors=most_popular_authors,
        over_one_percent_error=over_one_percent_error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
