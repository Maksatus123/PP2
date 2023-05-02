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
            VALUES('Maksat', 'Mukan', '87715164488'),
            ('Askar', 'Oralkhan', '87078300272'),
            ('Dias', 'Jakupov', '87712841851'),
            ('Margulan', 'Azimenov', '87077146503')
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
    

    def get_phone_users(cursor):
        cursor.execute(
            """
            select * from get_phone_users()
            """
        )


    def insert_or_update_data(cursor):
        cursor.execute(
            """
            call insert_or_update_data('Miras', 'Aibyn', '87073532433');
            select * from phonebook
            """
        )
        print(cursor.fetchall())

    def insert_many_data(cursor):
        cursor.execute(
            """
                call insert_many_data(array[
                    array['Ansar', 'Amanzholov', '87078957653'],
                    array['Artyom', 'Avdeev', '87475437854'],
                    array['Tamerlan', 'Taskynbay', '87773215674']
                ]);
            """
        )
        print("[INFO] Data was inserted successfully")

    def querring_by_pagination(cursor):
        cursor.execute(
            """
            select * from querring_by_pagination(0, 10);
            """
        )
        print(cursor.fetchall())

    
    def deleting_data_by_phone_or_name(cursor):
        cursor.execute(
            """
            call deleting_data('name', 'Miras');
            """
        )
        print("[INFO] Data was deleted")

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
    # deleting_data_by_phone_or_name(cursor)
    # get_phone_users(cursor)
    # insert_or_update_data(cursor)
    # insert_many_data(cursor)
    # querring_by_pagination(cursor)
    # deleting_data_by_phone_or_name(cursor)

except Exception as _ex:
    print("[INFO] Error while working with postgresql", _ex)
finally:
    if connection:
        connection.close()
        cursor.close()
        print("[INFO] PostgresSQL connection close")

