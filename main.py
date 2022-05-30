import psycopg2
from psycopg2 import sql

def create_tables(conn):
    cur = conn.cursor()

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS lines (line_id SERIAL PRIMARY KEY, name TEXT);"))
    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS stations (station_id TEXT PRIMARY KEY, name TEXT);"))
    conn.commit()

    cur.execute(sql.SQL("CREATE TABLE IF NOT EXISTS station_lines (line_id SERIAL REFERENCES lines(line_id), station_id TEXT REFERENCES stations(station_id));"))

    conn.commit()
    
conn = psycopg2.connect("dbname=tubedb user=james password=london")
create_tables(conn)