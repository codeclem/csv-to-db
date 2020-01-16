# csv-to-db

A python script to import csv files to an sqlite3 database, with support for column types.

## Usage
This script expects the first line of the csv file to describe the columns and types. Most csv files will already contain the column names. To specify the types, add `=[type]` to each column. For example:
```
id,name,birthday
1,John Doe,1985-10-26
```
should become
```
id=integer,name=text,birthday=date
1,John Doe,1985-10-26
```

If the file is particularly large and unwieldy to open in a text editor, you can use sed or some other magic:

`sed -i "1s/.*/id=integer,name=text,birthday=date/" birthdays.csv`

Then run the script and pass to it the csv file, the name of the sqlite file to write to, and the table name to be created/inserted into, in that order:

`./import.py birthdays.csv database.sqlite3 people`

Empty fields are stored as `null`. Any malformed rows will be skipped and a notice printed.

## Todo
Command line flags, support for other databases, and other niceties.
