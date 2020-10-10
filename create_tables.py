import logging

from database_connection import get_cassandra_connection
from sql_queries import sparkify_keyspace_create, sparkify_keyspace_drop, create_table_queries

logging.basicConfig(level=logging.INFO)


def initialize_database(session):
    """
    Drops keyspace if exists
    Create keyspace & tables
    :param session: cassandra session object
    :param cluster: Cassandra cluster object
    :return:
    """
    # Drop Keyspace
    session.execute(sparkify_keyspace_drop)
    # Create Keyspace
    session.execute(sparkify_keyspace_create)
    # set keyspace
    # session.set_keyspace('sparkify')

    # Create tables
    for table in create_table_queries:
        session.execute(table)


if __name__ == "__main__":
    session, cluster = get_cassandra_connection()
    initialize_database(session)
