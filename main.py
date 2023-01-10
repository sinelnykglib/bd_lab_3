import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '23102002Papa'
database = 'Lab_BD'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(film_name), count(film_name) FROM dubs GROUP BY film_name
'''

query_2 = '''
SELECT film_name, run_time from movie order by run_time
'''

query_3 = '''
SELECT years, round(AVG(rate),2) from movie GROUP by years order by years
'''

conn = psycopg2.connect(user = username, password = password, dbname = database, host = host, port = port)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute(query_1)
    x = []
    y = []
    for row in cur:
        x.append(row[0]+"-[{}]".format(row[1]))
        y.append(row[1])
    plt.pie(y, labels=x)
    plt.title("Film - languages")
    plt.show()

    print('\n2.')
    x = []
    y = []
    cur.execute(query_2)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x,y)
    plt.title("film - runs time")
    plt.xlabel("movie")
    plt.ylabel("time")
    plt.show()

    print('\n3.')
    x = []
    y = []
    cur.execute(query_3)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y)
    plt.title("average film rating by years")
    plt.xlabel("years")
    plt.ylabel("ratings")
    plt.show()