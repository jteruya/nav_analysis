import pandas as pd
import psycopg2

conn = psycopg2.connect("dbname='analytics' user='etl' host='10.223.192.6' password='s0.Much.Data'")

df = pd.read_sql_query('SELECT * from PUBLIC.Fact_Actions_Live WHERE Identifier = \'menuItem\' AND Created >= \'2016-01-01\'',con=conn)

df.to_csv('/Users/jonathanteruya/repo/nav_analysis/csv/text.csv')

conn.close()