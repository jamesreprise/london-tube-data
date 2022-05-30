import psycopg2
from psycopg2 import sql

conn = psycopg2.connect("dbname=tubedb user=james password=london")
cur = conn.cursor()


print("""
Query for all the lines for a given station using 'station:'.
e.g. 'station:victoria'

Query for all the stations for a given line using 'line:'.
e.g. 'line:victoria'

Use CTRL+C to exit.
""")

while True:
    print('> ', end='')
    query = input()
    query = query.split(":")
    if len(query) == 2:
        query_type = query[0]
        query_data = query[1]
        if query_type == "station":
            pass
        elif query_type == "line":
            pass
        else:
            print("Your query wasn't of the formation 'station:name' or 'line:name'. Please try again.")
    else:
        print("Your query wasn't of the formation 'station:name' or 'line:name'. Please try again.")

def station_query(station_name):

    pass

def line_query(line_name):
    pass