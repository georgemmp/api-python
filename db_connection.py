import sqlite3

connection = sqlite3.connect('hoteis_db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS hotel (hotel_id int PRIMARY KEY,\
                nome varchar(250), estrelas double, diaria double, cidade varchar(250))"
                
create_hotel =  "INSERT INTO hotel VALUES (1, 'Alpha Hotel', 4.3, 300, 'Belo Horizonte')"
                
cursor.execute(create_table)
cursor.execute(create_hotel)

connection.commit()
connection.close()