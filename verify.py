from database_connection import get_cassandra_connection
from sql_queries import select_queries


def verify_saved_data():
    session, cluster = get_cassandra_connection()
    for query in select_queries:
        print("\n\n------------------------------")
        print(query)
        print("------------------------------")
        rows = session.execute(query)
        for row in rows:
            print(row)


if __name__ == '__main__':
    verify_saved_data()
