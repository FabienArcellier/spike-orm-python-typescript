import logging
import os

from retrying import retry
import psycopg2
import psycopg2.extras


def configure_auto_logging():
  level_info = logging.INFO
  logging.basicConfig(format="%(asctime)s %(levelname)s - %(message)s [%(filename)s:%(lineno)s]" ,level=level_info)


@retry(stop_max_attempt_number=12, wait_fixed=10000)
def wait_datastore():
    logger = logging.getLogger('ci_tests')
    host = os.getenv('DATASTORE_HOST', 'localhost')
    user = 'postgres'
    password = '1234' # as this script is dedicated for CI that run in local. The credential is not a secret
    database = 'sportsdb'

    logger.info(f'new attempt to check availability of datastore on {host}:5432')
    query_string=f"dbname='{database}' user='{user}' host='{host}' password='{password}'"
    try:
        psycopg2.connect(query_string)
    except Exception as exception:
        logger.error(str(exception))
        raise

    logger.info(f'datastore is up and running on {host}:5432')

def main():
    configure_auto_logging()
    wait_datastore()


if __name__ == "__main__":
    main()

