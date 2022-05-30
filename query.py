import psycopg2
from psycopg2 import sql

def station_query(station_name):
    cur.execute(sql.SQL("""
    SELECT name FROM lines WHERE line_id IN (SELECT line_id FROM station_lines WHERE station_id IN (SELECT station_id FROM stations WHERE name = %s));
    """), [station_name])
    return list(map(lambda x: x[0], cur.fetchall()))



def line_query(line_name):
    cur.execute(sql.SQL("""
    SELECT name FROM stations WHERE station_id IN (SELECT station_id FROM station_lines WHERE line_id IN (SELECT line_id FROM lines WHERE name = %s));
    """), [line_name])
    return list(map(lambda x: x[0], cur.fetchall()))

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
            print(station_query(query_data))
        elif query_type == "line":
            print(line_query(query_data))
        else:
            print("Your query wasn't of the formation 'station:name' or 'line:name'. Please try again.")
    else:
        print("Your query wasn't of the formation 'station:name' or 'line:name'. Please try again.")