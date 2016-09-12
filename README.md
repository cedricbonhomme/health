# health

Retrieve, store and plot your Fitbit data.

## Usage

### Register a new Fitbit app

Register a new app [here](https://dev.fitbit.com/apps) and
provide your oauth credentials in the file *conf.cfg*.

### Database configuration

Create a new database (SQLite, MySQL, PostgreSQL) for this application and
configure the connection to this new database in the file *conf.cfg* with:

* the kind of the database (for example *postgres*);
* the database user name and password;
* the database address and port;
* the database name.

For example:

```ini
database_url = postgres://pgsqluser:pgsqlpwd@127.0.0.1:5432/health
```

Then create and initialize the database:

```shell
$ ./create_db.sh
ALTER ROLE
GRANT
$ python3.5 cmd.py db_create
```

### Retrieve the data

```bash
$ python3.5 weight.py
Retrieve data about the weight...
Database insertion...
Generation of the graph...
$ gwenview weight.png

$ python3.5 heart.py
Retrieve data about the heart rate...
Database insertion...
Generation of the graph...
$ gwenview 2016-09-12-heart.png
```


## TODO

* retrieve more data (sleep, activities, etc.).

## Contact

[Cédric Bonhomme](https://www.cedricbonhomme.org)
