#! /bin/sh

# drop completely the db (with the triggers, sequences, etc.)
sudo -u postgres dropdb health
sudo -u postgres createdb health --no-password
echo "ALTER USER pgsqluser WITH ENCRYPTED PASSWORD 'pgsqlpwd';" | sudo -u postgres psql
echo "GRANT ALL PRIVILEGES ON DATABASE health TO pgsqluser;" | sudo -u postgres psql
