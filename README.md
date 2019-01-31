# About the Project
This is a Log Analysis project for the Full Stack Web Development Nanodegree @Udacity (https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004)


## First Steps:

Download the file newsdata.zip here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

Unzip it and move it to your root directory. Then
load the data on `newsdata.sql` by running
`psql -d news -f newsdata.sql`

## Queries - DB API

Queries can be found on `newsdb.py`

## Views
This project uses the following views:

**total_requests**:

` CREATE VIEW total_requests as
  SELECT CAST(time as DATE) as day, count(status) as total_requests
  FROM log
  GROUP BY day
  ORDER BY day;
`
\
\
**error_requests**:

` CREATE VIEW error_requests as
  SELECT CAST(time as DATE) as day, count(status) as error_log
  FROM log
  WHERE status not like '200%'
  GROUP BY day
  ORDER BY day;
`

## File Structure
```bash
.
├── README.md
├── news.py
├── newsdb.py
├── requirements.txt
├── static
│   ├── github.png
│   └── icon.svg
└── templates
    └── index.html
```
## Running the Project

Activate your virtual environment. Then to make sure you have all
required dependencies installed, run `pip install -r requirements.txt`

Once that is setup, on your console run `python news.py`. That will run the
Log Analysis web page on your `localhost`on PORT `8000`.
