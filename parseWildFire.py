import sqlite3

sqlite_file = 'FPA_FOD_20170508.sqlite'    # name of the sqlite database file
table_name = 'Fires'   # name of the table to be queried
id_column = 'FOD_ID'
some_id = 123456
column_2 = 'FIRE_NAME'
column_3 = 'STATE'
column_4 = 'FIRE_YEAR'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT FOD_ID, FIRE_NAME, STATE, FIRE_YEAR FROM {tn} WHERE {cn}="IL"  and {cn2} = "2015"'.\
        format(tn=table_name, cn=column_3, cn2 = column_4))
all_rows = c.fetchall()
counter = 0
for row in all_rows:
    print(row)
    print("\n")
    counter += 1
    if (counter == 6):
        break

conn.commit()
conn.close()

        
