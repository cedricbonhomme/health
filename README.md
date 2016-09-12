# health

Retrieve, store and plot your Fitbit data.

## Usage

* register a new app [here](https://dev.fitbit.com/apps);
* provide your oauth credentials in the file **conf.cfg**;
* configure the database connection in the file **conf.cfg**.

```shell
$ cp conf.cfg-sample conf.cfg

$ ./create_db.sh
ALTER ROLE
GRANT
$ python3.5 cmd.py db_create

$ python3.5 weight.py
Retrieve data about the weight...
Database insertion...
Generation of the graph...
$ gwenview weight.png &

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
