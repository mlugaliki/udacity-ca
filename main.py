import csv
import glob
import os
from database_connection import get_cassandra_connection
from sql_queries import insert_queries


def save_in_cassandra(table):
    """
    Save music streaming data in cassandra
    :return:
    """
    session, cluster = get_cassandra_connection()

    # We have provided part of the code to set up the CSV file. Please complete the Apache Cassandra code below#
    file = 'event_datafile_new.csv'

    with open(file, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            query = "INSERT INTO popular_music(artist,firstName,gender,itemInSession,lastName,length,level," \
                    "location,sessionId,song,userId)"
            query = query + "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            session.execute(table, (line[0], line[1], line[2], int(line[3]), line[4], float(line[5]), line[6],
                                    line[7], int(line[8]), line[9], int(line[10])))


def process_csv():
    """
    Get csv in a dir and processes them to extract required info
    Create a csv file with the required information
    :return:
    """
    filepath = os.getcwd() + '/event_data'
    for root, dirs, files in os.walk(filepath):
        # for file_name in files:
        #  print(file_name)
        file_path_list = glob.glob(os.path.join(root, '*'))

    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []
    for f in file_path_list:
        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader)
            # extracting each data row one by one and append it
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line)

                # uncomment the code below if you would like to get total number of rows
    # print(len(file_path_list))
    # uncomment the code below if you would like to check to see what the list of event data rows will look like
    # print(full_data_rows_list)

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    data_file = 'event_datafile_new.csv'
    os.remove(data_file)  # Remove file if it exists
    with open(data_file, 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', 'level', 'location',
                         'sessionId', 'song', 'userId'])
        for row in full_data_rows_list:
            if row[0] == '':
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding='utf8') as f:
        print(sum(1 for line in f))

    for query in insert_queries:
        save_in_cassandra(query)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_csv()
