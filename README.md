# About the Project
This is a Log Analysis project for the Full Stack Web Development Nanodegree @Udacity (https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004)


## Setting up your environment:

1. This project makes use of a linux-based virtual machine. To install it, go to Virtual Box's website: https://www.virtualbox.org/wiki/Downloads

2. We use Vagrant to manage our virtual machine and sync our local repo with VM's repo. Please install vagrant: https://www.vagrantup.com/downloads.html

3. Run `vagrant up` followed by `vagrant ssh`.

4. Run `cd /vagrant`. Then clone the current repo by running
`git clone git@github.com:dani-santos-code/log_analysis.git`

5. Run `pip install -r requirements.txt` to load necessary dependencies.

6. Finally, download the file `newsdata.zip` here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

7. Unzip it and move it to your root directory(`news`).

8. On the root directory, load the data on `newsdata.sql` by running `psql -d news -f newsdata.sql`

## Running Queries - DB API

Make sure you're on the root directory.

* To run queries type `python newsdb.py`

* You should see something like this:
![image](https://drive.google.com/uc?export=view&id=17cPO-qDfgG6OdVoLBY7wa_ENoKPP_d9O)

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

## Original File Structure
```bash
.
├── README.md
├── newsdb.py
├── requirements.txt
└── Vagrantfile
```

## After adding the .sql file:

```bash
.
├── README.md
├── newsdb.py
├── newsdata.sql
└── requirements.txt
```
