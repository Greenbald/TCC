import pymonetdb
import os
import pandas as pd

monetConn = pymonetdb.connect(username="paulo", password=os.environ["DB_PASSWORD"],
                               hostname="localhost", database="demo")
monetCur = monetConn.cursor()

monetCur.arraysize = 4025

monetCur.execute('SELECT * FROM tweet_tokens')


df = pd.DataFrame(monetCur.fetchall())

meta_data = monetCur.description

#metadata = pd.DataFrame(columns=[i[0] for i in meta_data])

#fdf = pd.concat([metadata , df], axis=0)
df.columns = [i[0] for i in meta_data]

df.to_csv("data/tweets.csv", encoding="ascii")

monetCur.execute('SELECT * FROM user_tokens')

df = pd.DataFrame(monetCur.fetchall())

meta_data = monetCur.description

df.columns = [i[0] for i in meta_data]

df.to_csv("data/users.csv", encoding="ascii")

monetCur.close()
monetConn.close()