# importing the required modules
import mysql.connector
import sys
import time
import maskpass         # doesn't work in Python IDLE 

# getting the mysql password 
password = maskpass.askpass(prompt="\nEnter password for root user : ")

# connecting to MySql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # passwd=input("\nEnter password for root user : ")
    passwd=password  
)

# making the cursor object
cursor = mydb.cursor()

# creating the database
cursor.execute("CREATE DATABASE IF NOT EXISTS project")
cursor.execute("USE project")

# creating the table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS students"
    "(adm_no INT(4) PRIMARY KEY UNIQUE NOT NULL, "
    "class INT(4) NOT NULL, "
    "roll_no INT(4) NOT NULL, "
    "student_name VARCHAR(30) NOT NULL, "
    "math_marks DOUBLE(4,1) NOT NULL, "
    "phy_marks DOUBLE(4,1) NOT NULL, "
    "chem_marks DOUBLE(4,1) NOT NULL, "
    "eng_marks DOUBLE(4,1) NOT NULL, "
    "comp_marks DOUBLE(4,1) NOT NULL, "
    "total DOUBLE(4,1), "
    "CGPA DOUBLE(4,1))")

print("\n---------- Creating database and inserting the dummy data -----------")
time.sleep(3)

sql = "INSERT INTO students (adm_no, class, roll_no, student_name, math_marks, phy_marks, " \
      "chem_marks, eng_marks, comp_marks, total, CGPA) " \
      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

val = [(507, 11, 1, 'Oma Lawler', 78.2, 71.7, 54.7, 78.9, 74.0, 357.5, 8.9),
       (508, 12, 1, 'Jerome Gipson', 67.5, 68.9, 50.7, 71.2, 76.4, 334.7, 8.4),
       (509, 11, 2, 'Tamica Goins', 55.8, 66.3, 67.3, 71.7, 78.2, 339.3, 8.5),
       (510, 12, 2, 'Calvin Looney', 56.6, 55.3, 60.1, 70.5, 80.0, 322.5, 8.1),
       (511, 11, 3, 'Adan Pulido', 63.4, 75.2, 54.3, 79.5, 79.2, 351.6, 8.8),
       (512, 10, 1, 'Logan Flannery', 50.1, 66.9, 74.8, 70.5, 80.0, 342.3, 8.6),
       (513, 12, 3, 'Abram Swank', 76.8, 76.1, 67.8, 56.0, 75.8, 352.5, 8.8),
       (514, 12, 4, 'Selina Pfeiffer', 52.6, 66.9, 54.9, 73.4, 78.7, 326.5, 8.2),
       (515, 11, 4, 'Bradford Broderick', 69.3, 50.4, 70.2, 69.4, 74.5, 333.8, 8.3),
       (537, 11, 5, 'Adolph Francisco', 60.9, 67.1, 70.5, 66.6, 78.2, 343.3, 8.6),
       (538, 11, 6, 'Delcie Abney', 56.3, 64.3, 79.1, 63.0, 76.0, 338.7, 8.5),
       (539, 10, 2, 'Newton Graves', 70.3, 70.6, 71.8, 72.0, 74.6, 359.3, 9.0),
       (540, 11, 7, 'Alejandro Espinal', 52.6, 77.3, 52.6, 67.5, 72.2, 322.2, 8.1),
       (541, 11, 8, 'Calvin Abrams', 73.9, 68.0, 61.8, 60.4, 76.5, 340.6, 8.5),
       (542, 10, 3, 'Ronnie Roby', 78.6, 68.5, 53.8, 79.8, 75.9, 356.6, 8.9),
       (543, 12, 5, 'Owen Alston', 58.9, 74.3, 66.8, 56.9, 74.4, 331.3, 8.3),
       (544, 12, 6, 'Elaina Gruber', 53.0, 71.5, 66.8, 71.2, 76.9, 339.4, 8.5),
       (545, 12, 7, 'Hosea Spears', 56.6, 68.4, 77.9, 62.8, 74.3, 340.0, 8.5),
       (567, 12, 8, 'Stanford Sullivan', 57.2, 63.8, 69.9, 76.3, 78.2, 345.4, 8.6),
       (568, 10, 4, 'Adam Geer', 61.6, 53.2, 51.5, 71.7, 77.9, 315.9, 7.9),
       (569, 11, 9, 'Elli Robertson', 53.9, 72.9, 71.4, 66.8, 78.5, 343.5, 8.6),
       (570, 12, 9, 'Carley Valdez', 52.3, 79.0, 70.7, 77.7, 77.2, 356.9, 8.9),
       (571, 11, 10, 'Burt Hughes', 50.1, 80.0, 70.3, 58.9, 79.8, 339.1, 8.5),
       (572, 12, 10, 'Milton Gay', 75.2, 74.2, 59.8, 56.8, 74.8, 340.8, 8.5),
       (573, 12, 11, 'Bradford Alfaro', 78.5, 67.1, 70.0, 55.0, 74.5, 345.1, 8.6),
       (597, 11, 11, 'Denisha Mcginnis', 60.2, 53.3, 54.9, 61.3, 73.3, 303.0, 7.6),
       (598, 10, 5, 'Adah Jameson', 60.3, 65.5, 72.0, 69.4, 77.3, 344.5, 8.6),
       (599, 11, 12, 'Justin Bieber', 80.0, 80.0, 80.0, 80.0, 80.0, 400.0, 10.0),
       (600, 11, 13, 'Curtis Hutson', 60.3, 76.8, 50.2, 51.9, 76.7, 315.9, 7.9),
       (601, 12, 12, 'Zayn Malik', 77.7, 60.7, 78.6, 74.4, 74.8, 366.2, 9.2),
       (602, 11, 14, 'Alice Gonzales', 58.2, 52.9, 58.1, 66.7, 73.8, 309.7, 7.7),
       (603, 10, 6, 'Darrick Olmstead', 51.8, 54.5, 76.2, 64.8, 79.8, 327.1, 8.2),
       (604, 11, 15, 'Benito Agee', 68.3, 66.4, 63.2, 53.4, 77.6, 328.9, 8.2),
       (628, 12, 13, 'Marcos Abraham', 74.5, 60.0, 73.5, 57.4, 73.0, 338.4, 8.5),
       (629, 12, 14, 'Adam Maddox', 64.6, 58.7, 63.5, 61.6, 75.2, 323.6, 8.1),
       (630, 10, 7, 'Kasey Furr', 71.5, 51.7, 53.4, 51.2, 76.8, 304.6, 7.6),
       (631, 10, 8, 'Jarod Bourgeois', 79.6, 56.3, 52.5, 80.0, 75.7, 344.1, 8.6),
       (632, 11, 16, 'Bud Grubbs', 80.0, 78.1, 58.3, 51.8, 75.2, 343.4, 8.6),
       (633, 10, 9, 'Aimee Stamm', 75.8, 71.7, 73.0, 74.0, 72.7, 367.2, 9.2),
       (634, 11, 17, 'Myrtis Thornhill', 66.7, 67.7, 59.5, 69.6, 76.4, 339.9, 8.5),
       (635, 12, 15, 'Alexa Saucedo', 77.7, 69.7, 79.6, 53.5, 74.4, 354.9, 8.9),
       (636, 11, 18, 'Armando Alvarez', 69.6, 72.4, 67.5, 69.2, 72.1, 350.8, 8.8),
       (637, 12, 16, 'Alan Judd', 77.2, 68.5, 51.1, 61.1, 72.7, 330.6, 8.3),
       (638, 11, 19, 'Janis Gonsalves', 57.4, 55.8, 59.2, 51.2, 72.3, 295.9, 7.4),
       (658, 10, 10, 'Vanita Kelleher', 73.5, 77.8, 69.4, 76.6, 72.3, 369.6, 9.2),
       (659, 11, 20, 'Burton Bunnell', 62.4, 64.9, 73.6, 67.2, 80.0, 348.1, 8.7),
       (660, 10, 11, 'Akari Watanabe', 76.8, 74.5, 69.2, 76.2, 74.6, 371.3, 9.3),
       (661, 11, 21, 'Melia Gates', 51.5, 64.8, 77.0, 62.0, 78.3, 333.6, 8.3),
       (662, 12, 17, 'Oliva Coble', 66.9, 74.3, 52.4, 60.9, 78.7, 333.2, 8.3),
       (663, 11, 22, 'Shonda Leake', 57.1, 69.3, 50.6, 68.3, 74.3, 319.6, 8.0),
       (664, 11, 23, 'Derrick Ruiz', 53.2, 57.1, 75.9, 53.4, 75.5, 315.1, 7.9),
       (665, 11, 24, 'Abram Fenton', 59.6, 77.6, 53.5, 66.7, 78.7, 336.1, 8.4),
       (666, 12, 18, 'Ariana grande', 80.0, 80.0, 80.0, 80.0, 80.0, 400.0, 10.0),
       (667, 10, 12, 'Sonya Tinsley', 72.6, 62.3, 51.0, 70.6, 72.7, 329.2, 8.2),
       (668, 11, 25, 'Chris Brown', 78.3, 58.9, 79.3, 65.5, 76.5, 358.5, 9.0),
       (683, 12, 19, 'Johnathan Magana', 60.3, 56.8, 65.2, 72.2, 74.0, 328.5, 8.2),
       (684, 12, 20, 'Sanjuanita Conners', 76.5, 64.5, 63.7, 52.9, 75.0, 332.6, 8.3),
       (705, 11, 26, 'Felix Alba', 59.0, 60.5, 75.0, 73.6, 79.5, 347.6, 8.7),
       (706, 11, 27, 'Nathan Salisbury', 73.2, 71.1, 58.1, 74.4, 74.8, 351.6, 8.8),
       (707, 10, 13, 'Ariel Hermann', 63.6, 52.3, 68.6, 75.5, 80.0, 340.0, 8.5),
       (708, 11, 28, 'Marc Pickering', 54.6, 71.7, 75.9, 55.9, 77.6, 335.7, 8.4),
       (709, 11, 29, 'Malcolm Coward', 59.6, 53.4, 51.5, 70.0, 78.5, 313.0, 7.8),
       (710, 11, 30, 'Deedee Strange', 55.8, 53.6, 64.7, 77.3, 76.1, 327.5, 8.2),
       (711, 11, 31, 'Jeanna Maxwell', 59.6, 61.6, 75.5, 76.9, 78.5, 352.1, 8.8),
       (712, 10, 14, 'Glynis Redman', 76.8, 64.7, 68.7, 75.9, 77.1, 363.2, 9.1),
       (713, 12, 21, 'Debbra Packer', 54.2, 65.7, 79.8, 72.4, 80.0, 352.1, 8.8),
       (714, 12, 22, 'Graham Alger', 64.1, 51.5, 79.3, 70.1, 73.0, 338.0, 8.4),
       (715, 10, 15, 'Abdul Freed', 76.8, 76.6, 72.2, 60.1, 72.9, 358.6, 9.0),
       (736, 11, 32, 'Eusebia Noland', 63.5, 51.5, 59.0, 74.4, 74.7, 323.1, 8.1),
       (737, 11, 33, 'Freeman Selby', 51.7, 59.1, 70.3, 72.5, 72.8, 326.4, 8.2),
       (738, 12, 23, 'Gertie Abel', 64.4, 62.9, 63.9, 56.4, 74.5, 322.1, 8.1),
       (739, 11, 34, 'Corey Musgrove', 69.8, 60.3, 66.6, 68.7, 80.0, 345.4, 8.6),
       (740, 10, 16, 'Eren Yeager', 80.0, 80.0, 80.0, 80.0, 80.0, 400.0, 10.0),
       (741, 12, 24, 'Hobert Adam', 71.6, 57.9, 71.1, 55.4, 72.5, 328.5, 8.2),
       (742, 12, 25, 'Carlton Beaudoin', 63.3, 78.0, 76.2, 73.7, 73.2, 364.4, 9.1),
       (743, 12, 26, 'Machelle Andersen', 75.6, 52.2, 79.2, 68.9, 79.3, 355.2, 8.9),
       (751, 10, 17, 'Letha Bolt', 66.6, 72.5, 62.9, 60.8, 78.8, 341.6, 8.5),
       (752, 11, 35, 'Laura Barger', 61.5, 57.5, 57.8, 76.6, 77.4, 330.8, 8.3),
       (753, 11, 36, 'Shawn Mendes', 76.3, 75.4, 58.7, 80.0, 80.0, 370.4, 9.3),
       (754, 10, 18, 'Alida Jobe', 67.0, 74.7, 73.5, 55.4, 75.0, 345.6, 8.6),
       (755, 10, 19, 'Reba Gregg', 67.1, 60.0, 78.5, 79.0, 80.0, 364.6, 9.1),
       (756, 12, 27, 'Lizzie Krueger', 67.0, 80.0, 53.2, 80.0, 74.0, 354.2, 8.9),
       (757, 12, 28, 'Hubert Waldrop', 64.9, 52.8, 77.0, 56.1, 80.0, 330.8, 8.3),
       (758, 10, 20, 'Mervin Lyon', 69.8, 60.4, 63.2, 60.3, 78.4, 332.1, 8.3),
       (759, 12, 29, 'Drake', 80.0, 80.0, 65.7, 70.2, 80.0, 375.9, 9.4),
       (760, 10, 21, 'Lesia Hatch', 64.2, 58.3, 73.9, 60.2, 73.5, 330.1, 8.3),
       (761, 10, 22, 'Marin Kitagawa', 69.8, 77.1, 73.7, 71.1, 79.3, 371.0, 9.3),
       (762, 11, 37, 'Ora Dorris', 51.6, 52.4, 69.3, 57.1, 74.0, 304.4, 7.6),
       (780, 12, 30, 'Miyoko Mckinney', 59.0, 59.6, 54.4, 73.1, 78.4, 324.5, 8.1),
       (781, 10, 23, 'Winnifred Brantley', 56.3, 64.9, 66.5, 67.2, 75.6, 330.5, 8.3),
       (782, 11, 38, 'Josephine Norwood', 69.8, 68.1, 70.2, 52.6, 80.0, 340.7, 8.5),
       (783, 10, 24, 'Cordelia Key', 50.1, 78.6, 56.9, 57.5, 73.0, 316.1, 7.9),
       (784, 11, 39, 'Bertram Herzog', 78.6, 77.8, 50.4, 70.4, 76.0, 353.2, 8.8),
       (785, 12, 31, 'Celestine Hong', 51.8, 72.9, 80.0, 76.7, 73.2, 354.6, 8.9),
       (786, 10, 25, 'Abel Christian', 58.9, 55.3, 56.5, 75.0, 72.5, 318.2, 8.0),
       (787, 12, 32, 'Halley Bostic', 54.8, 68.2, 61.2, 73.7, 78.1, 336.0, 8.4),
       (788, 12, 33, 'Drew Burt', 71.1, 63.9, 50.0, 80.0, 72.6, 337.6, 8.4),
       (789, 10, 26, 'Kizzy Hightower', 73.4, 60.5, 51.2, 80.0, 73.3, 338.4, 8.5),
       (790, 11, 40, 'Abel Paulson', 52.1, 50.2, 54.1, 62.3, 76.3, 295.0, 7.4),
       (791, 11, 41, 'Abbie Gurley', 52.2, 73.3, 66.1, 62.5, 73.6, 327.7, 8.2)]

# inserting all the values
try:
    cursor.executemany(sql, val)
    if cursor.rowcount == 100:
        print("\n----------- Data inserted successfully -----------\n")
        time.sleep(3)
except mysql.connector.errors.IntegrityError as e:
    code = e.errno
    if code == 1062:
        print("\n-------------- Error -  Values already exist. First, delete the old data and then try again. ------------\n")
        time.sleep(3)

# commiting the changes
mydb.commit()

# closing the connection
mydb.close()

# exiting the programme
sys.exit()
