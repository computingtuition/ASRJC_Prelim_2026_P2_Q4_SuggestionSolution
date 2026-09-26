import sqlite3

def create_tables():
    db = sqlite3.connect('SHENZHENGO.db')

    # clear db if tables exist
    db.execute('''DROP TABLE IF EXISTS Student''') # must be removed before Room as it references Room
    db.execute('''DROP TABLE IF EXISTS Room''')

    # create the tables
    db.execute('''
    CREATE TABLE `Room` (
            `Room_ID`	INTEGER,
            `Room_Type`	TEXT,
            PRIMARY KEY(`Room_ID`)
    );
    ''')

    db.execute('''
    CREATE TABLE `Student` (
            `Student_ID`	INTEGER,
            `Student_Name`	TEXT,
            `Student_Class`	TEXT,
            `Student_Gender`	TEXT,
            `Student_Leader`	INTEGER,
            `Room_ID`	INTEGER,
            PRIMARY KEY(`Student_ID`),
            FOREIGN KEY(`Room_ID`) REFERENCES `Room`(`Room_ID`)
    );
    ''')

    # open the files

    ### ROOMS ###
    file = open('ROOMS.txt', 'r')

    # skip the header line
    file.readline()

    for line in file:
        line = line.strip() # remove \n at the end
        Room_ID, Room_Type = line.split(',')

        db.execute('''
        INSERT INTO Room(Room_ID, Room_Type)
        VALUES(?, ?)
        ''', (Room_ID, Room_Type))
        db.commit()

    file.close()

    ### STUDENTS ###
    file = open('STUDENTS.txt', 'r')

    # skip the header line
    file.readline()

    for line in file:
        line = line.strip() # remove \n at the end
        Student_ID,Student_Name,Student_Class,Student_Gender,Student_Leader,Room_ID = line.split(',')

        # need to convert to integer
        if Student_Leader == 'TRUE':
            Student_Leader = 1
        else:
            Student_Leader = 0

        db.execute('''
        INSERT INTO Student(Student_ID,Student_Name,Student_Class,Student_Gender,Student_Leader,Room_ID)
        VALUES(?, ?, ?, ?, ?, ?)
        ''', (Student_ID,Student_Name,Student_Class,Student_Gender,Student_Leader,Room_ID))
        db.commit()
        
    file.close()

    db.close()
