# About the Project
This is a Log Analysis project for the Full Stack Web Development Nanodegree @Udacity (https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004)


## Setting up your environment:

1. This project makes use of a linux-based virtual machine. To install it, go to Virtual Box's website: https://www.virtualbox.org/wiki/Downloads

2. We use Vagrant to manage our virtual machine and sync our local repo with VM's repo. Please install vagrant: https://www.vagrantup.com/downloads.html

3. Clone the current repo by running
`git clone git@github.com:dani-santos-code/log_analysis.git`

4. Run `vagrant up` followed by `vagrant ssh`.

5. Run `cd /vagrant`.

5. Run `pip install -r requirements.txt` to load necessary dependencies. *In case of errors, run `sudo pip install -r requirements.txt`*

6. Finally, download the file `newsdata.zip` here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

7. Unzip it and move it to your root directory.

8. Load the data on `newsdata.sql` by running `psql -d news -f newsdata.sql`

9. Run `psql news` to access the `news` database.

## Creating Views

Now run the following to create 2 views ('total_requests' and 'error_requests'):

` CREATE VIEW total_requests as
  SELECT CAST(time as DATE) as day, count(status) as total_requests
  FROM log
  GROUP BY day
  ORDER BY day;
`
\
\
` CREATE VIEW error_requests as
  SELECT CAST(time as DATE) as day, count(status) as error_log
  FROM log
  WHERE status not like '200%'
  GROUP BY day
  ORDER BY day;
`

* After creating the views, don't forget to exit the `psql` console by running `\q`

## Running the Script

* To run queries, type `python newsdb.py`

* You should see something like this:
![image](https://drive.google.com/uc?export=view&id=17cPO-qDfgG6OdVoLBY7wa_ENoKPP_d9O)


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
├── Vagrantfile
└── requirements.txt
```
