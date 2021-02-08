import pandas as pd
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='', db='tai_projekt')
# create cursor
cursor = connection.cursor()

# iterate through table pages
for value in range(1, 6):
    # url to site with data, last number indicates page
    url = "https://stooq.pl/t/?i=513&v=0&l={}".format(value)
    # find table with name 'fth1'
    df = pd.read_html(url, attrs={'id': 'fth1'})[0]

    # Insert DataFrame records one by one
    for i, row in df.iterrows():
        sql = ("INSERT INTO stocks(symbol, name, price) VALUES('{}','{}',{}) ON DUPLICATE KEY UPDATE price = {}"
               .format(row['Symbol'], row['Nazwa'], row['Kurs'], row['Kurs']))
        # print(sql)
        cursor.execute(sql)

        connection.commit()

connection.close()
print("Done")
