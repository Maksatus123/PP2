import psycopg2
import csv

try:
    #create table
    def create_table(cursor):
        cursor.execute(
        """
            CREATE TABLE PhoneBook(
                id serial PRIMARY KEY,
                first_name varchar(50),
                last_name varchar(50),
                phone_number varchar(13)
            );
        """
        )
        print("[INFO] Table was created")


    def insert_data(cursor):
        cursor.execute(
            """
            INSERT INTO PhoneBook(first_name, last_name, phone_number)
            VALUES('Maksat', 'Mukan', '87715164488')
            """
        )
        print("[INFO] Data was inserted successfully")


    def insert_data_from_csv(cursor):
        #getting data from csv file
        data_set = []
        with open ('phonebook2.csv') as phone_book_file:
            spamreader = csv.reader(phone_book_file)
            for row in spamreader:
                data_set.append(row)

        data_set_splitted = []
        for i in data_set:
            for j in i:
                data_set_splitted.append(j.split(";"))
        
        #inserting data from csv file
        for i in data_set_splitted:
            cursor.execute(
                f"""
                INSERT INTO PhoneBook(first_name, last_name, phone_number)
                VALUES('{i[0]}', '{i[1]}', '{i[2]}');
                """
            )
        print("[INFO] Data was inserted successfully")


    def update_data(cursor):
        #update data
        cursor.execute(
            """
                UPDATE PhoneBook
                SET phone_number = '87783459164'
                WHERE first_name = 'Maksat'
            """
            )
        print("[INFO] Data was updated successfully")
    

    def data_query(cursor):
        #Querying data from the tables 
        cursor.execute(
            """
            SELECT * from PhoneBook WHERE first_name = 'Maksat' or last_name = 'Jakupov'
            """
        )
        print(cursor.fetchone())
    

    def delete_data(cursor):
        #deleting data
        cursor.execute(
            """
            DELETE FROM PhoneBook
            WHERE first_name = 'Margulan'
            """
        )
        print("[INFO] Data was deleted")


    def drop_table(cursor):
        cursor.execute(
        """
        DROP TABLE Phonebook
        """
        )
        print("[INFO] Table was deleted")
    #connection to database
    connection = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "admin",
        database = "pp2"
    )
    connection.autocommit = True

    cursor = connection.cursor()

    # create_table(cursor)
    # insert_data(cursor)
    # insert_data_from_csv(cursor)
    # update_data(cursor)
    # delete_data(cursor)
    # drop_table(cursor)

except Exception as _ex:
    print("[INFO] Error while working with postgresql", _ex)
finally:
    if connection:
        connection.close()
        cursor.close()
        print("[INFO] PostgresSQL connection close")

