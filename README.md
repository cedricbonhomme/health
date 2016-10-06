# health

Retrieve, store and plot your Fitbit data.

## Usage

### Register a new Fitbit app

Register a new app [here](https://dev.fitbit.com/apps) and
provide your oauth credentials in the file *conf.cfg*.  
In order to get intra-days values for the heart rate, you should create a
*Personal* app.  
The callback URL should be *http://127.0.0.1:8080/*.

To get your *access_token* and *refresh_token*:

```shell
$ python gather_keys_oauth2.py client_id client_secret
```

### Database configuration

#### Example with SQLite

Configure the connection in the file *conf.cfg*:

```ini
$ grep 'database_url' conf/conf.cfg
database_url = sqlite:///health.db
```

Then create and initialize the database:

```shell
$ ./fitbit-ctl.py db_initialize
reinitialize the database (yes/no) ? (default: no)  : yes
```

#### Example with PostgreSQL

Create a new PostgreSQL database (or MySQL) for this application and
configure the connection in the file *conf.cfg*:

```ini
$ grep 'database_url' conf/conf.cfg
database_url = postgres://pgsqluser:pgsqlpwd@127.0.0.1:5432/health
```

As you can see the line specifies:
* the kind of the database (here *postgres*);
* the database user name and password;
* the database address and port;
* the database name.

Then create and initialize the database:

```shell
$ ./create_db.sh
ALTER ROLE
GRANT
$ ./fitbit-ctl.py db_initialize
reinitialize the database (yes/no) ? (default: no)  : yes
```

### Retrieve the data

#### Heart

```bash
$ ./fitbit-ctl.py retrieve_heart 5
Retrieving the heart rate for September 14, 2016...
Retrieving the heart rate for September 13, 2016...
Retrieving the heart rate for September 12, 2016...
Retrieving the heart rate for September 11, 2016...
Retrieving the heart rate for September 10, 2016...

$ ./fitbit-ctl.py plot_heart 2016-09-12
Generation of the graph...
$ gwenview 2016-09-12_heart.png
```

#### Weight

```bash
$ ./fitbit-ctl.py retrieve_weight 2016-09-01 2016-09-31
Retrieving the weight...

$ ./fitbit-ctl.py plot_weight
Generation of the graph...
$ gwenview weight.png
```

#### Help command

```bash
$ ./fitbit-ctl.py -h
usage: fitbit-ctl.py <command> [<args>]

positional arguments:
  command     the command to run

optional arguments:
  -h, --help  show this help message and exit

available commands:
  db_initialize            Initialize the database from conf parameters.
  plot_heart               Plot the data about the heart.
  plot_weight              Plot the data about the weight.
  retrieve_heart           Retrieve the data about the heart.
  retrieve_weight          Retrieve the data about the weight.
```


## TODO

* retrieve more data (sleep, activities, etc.).

## Contact

[Cédric Bonhomme](https://www.cedricbonhomme.org)
