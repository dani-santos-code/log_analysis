import psycopg2

DBNAME = "news"


def get_top_three_articles():
    """Return top three articles from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT articles.title, COUNT(log.path) FROM articles
            JOIN log ON articles.slug = SUBSTRING(log.path, 10)
            GROUP BY title
            ORDER BY count
            DESC LIMIT 3
            """
    c.execute(query)
    top_three_articles = c.fetchall()
    db.close()
    return top_three_articles


def get_most_popular_authors():
    """Return most popular authors from the 'database', most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT name, SUM(count) as total_views
            FROM(SELECT a.title, a.name, COUNT(log.path)
                    FROM(SELECT a.title, authors.name, a.slug
                         FROM articles as a
                         JOIN authors on a.author=authors.id) a
                    JOIN log on a.slug = substring(log.path, 10)
                    GROUP BY title, name order by count) authlog
            GROUP BY name
            ORDER BY total_views DESC;
            """
    c.execute(query)
    most_popular_authors = c.fetchall()
    db.close()
    return most_popular_authors


def get_over_one_percent_error():
    """Return day(s) when errors were over 1 %."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """SELECT TO_CHAR(t.day :: DATE, 'Mon dd, yyyy') as day,
            t.total_requests, cast(e.error_log * 100.00/t.total_requests as
            DECIMAL(10,2)) as error_percentage
            FROM error_requests as e, total_requests as t
            WHERE e.day = t.day
            AND e.error_log > t.total_requests/100.00;
            """
    c.execute(query)
    over_one_percent_error = c.fetchall()
    db.close()
    return over_one_percent_error
