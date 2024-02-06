import csv
import sqlite3

class MedicalDatabase:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.column_names_list = []
        self.list_of_data_lists = []

    def delete(self):
        # Just normal delete function
        pass

    def insert(self):
        # Insert patient data. Two cases(optional btw we can just add entire row) one for inserting entire row and one
        # for updating/insert (maybe adding missing data to some patient)
        pass

    def interpret_data(self):
        # I do not remember why we have this
        pass

    def correct_data(self):
        # Correct missing value if any. I think we can make it initialized by click of the button.
        pass

    def load_data(self):
        with open(self.file_path, newline='') as csvfile:
            file = csv.reader(csvfile, delimiter=' ', quotechar='|')
            counter = 0
            for row in file:
                # Find all column names or data from string row[0] that contains them separated by commas
                data_from_row = row[0].split(',')

                # For first row of the file get the title of each column
                if counter == 0:
                    for columnName in data_from_row:
                        self.column_names_list.append(columnName)
                        # Adding new empty lists here cuz it only executes at the beginning of the reading
                        self.list_of_data_lists.append([])

                # For all other rows that contain data get data - add data to lists (representing columns of the dataset)
                # that are in the listOfDataLists, each of these has a columnCounter index, eg. HeartDiseaseOrAttack is on
                # index 0 (column no. 0), so add values to a list that is on this index
                else:
                    column_counter = 0
                    for data in data_from_row:
                        self.list_of_data_lists[column_counter].append(data)
                        column_counter = column_counter + 1

                counter = counter + 1

            for i in range(0, len(self.column_names_list)):
                print(self.column_names_list[i] + " : " + str(len(self.list_of_data_lists[i])))

    def save_data(self):
        # Saves data to file. Something should be in parameters
        pass


class MedicalDatabaseSQL:
    def __init__(self, db_name='your_database.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def create_table(self):
        if not self.conn:
            self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
                id INTEGER PRIMARY KEY,
                user_id INTEGER UNIQUE,
                full_name TEXT,
                email TEXT,
                FOREIGN KEY (user_id) REFERENCES logins (id)
            )
        ''')

