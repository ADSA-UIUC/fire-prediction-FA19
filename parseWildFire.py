import sqlite3

sqlite_file = 'FPA_FOD_20170508.sqlite'    # name of the sqlite database file
table_name = 'Fires'   # name of the table to be queried
id_column = 'FOD_ID'
some_id = 123456
column_2 = 'FIRE_SIZE'
column_3 = 'STATE'
column_4 = 'FIRE_YEAR'

x = []
y = []

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
 
years = 1992
yearsStr = str(years)

# get years
for z in range(24):
    c.execute('SELECT FIRE_YEAR FROM {tn} WHERE {cn}="IL"  and {cn2} = "{y}"'.\
            format(tn=table_name, cn=column_3, cn2 = column_4, y = yearsStr))
    all_rows = c.fetchall()
    counter = 0
    for row in all_rows:
        print(row[0])
        x.append(row[0])
        #print("\n")
        counter += 1
        if (counter == 20):
            break
    years += 1
    yearsStr = str(years)


years = 1992
yearsStr = str(years)


# get fire sizes
for z in range(24):
    c.execute('SELECT FIRE_SIZE FROM {tn} WHERE {cn}="IL"  and {cn2} = "{y}"'.\
            format(tn=table_name, cn=column_3, cn2 = column_4, y = yearsStr))
    all_rows = c.fetchall()
    counter = 0
    for row in all_rows:
        print(row[0])
        y.append(row[0])
        #print("\n")
        counter += 1
       
        if (counter == 20):
            break

    years += 1
    yearsStr = str(years)

conn.commit()
conn.close()

from bokeh.plotting import figure, output_file, show


# output to static HTML file
output_file("firesizesillinois.html")

# create a new plot with a title and axis labels
p = figure(title="Fire Sizes of First 20 Fires Per Year in Illinois", x_axis_label='Year', y_axis_label='Fire Size')

# add a line renderer with legend and line thickness
p.line(x, y, legend="Fire Size.", line_width=2)

# show the results
show(p)
        
