import psycopg2
import json
import uuid
from psycopg2 import sql

def create_tables(conn):
    cur = conn.cursor()

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS lines (line_id TEXT PRIMARY KEY, name TEXT);"))
    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS stations (station_id TEXT PRIMARY KEY, name TEXT, longitude TEXT, latitude TEXT);"))
    conn.commit()

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS station_lines (line_id TEXT REFERENCES lines(line_id), station_id TEXT REFERENCES stations(station_id));"))

    conn.commit()

def load_dataset(path, conn):
    data = json.load(open(path, 'r'))
    cur = conn.cursor()
    for station in data['stations']:
        # A station has a 'name', 'id', 'longitude', 'latitude'.
        station_id = station['id']
        name = station['name']
        # We aren't doing math on the longitude or latitude, so we don't need to store these as floats.
        lon = str(station['longitude'])
        lat = str(station['latitude'])
        cur.execute(sql.SQL("INSERT INTO stations(station_id, name, longitude, latitude) VALUES (%s, %s, %s, %s);"), [station_id, name, lon, lat])
        conn.commit()
    
    for line in data['lines']:
        # A line has a 'name' and 'stations', which is a list of station_id as strings.
        name = line['name']
        stations = line['stations']
        # We make a line UUID to create a primary key for a line.
        line_id = str(uuid.uuid4())
        cur.execute(sql.SQL("INSERT INTO lines(line_id, name) VALUES (%s, %s);"), [line_id, name])
        conn.commit()
        for station_id in stations:
            cur.execute(sql.SQL("INSERT INTO station_lines(line_id, station_id) VALUES (%s, %s);"), [line_id, station_id])
            conn.commit()
    
conn = psycopg2.connect("dbname=tubedb user=james password=london")
create_tables(conn)
load_dataset("train-network.json", conn)