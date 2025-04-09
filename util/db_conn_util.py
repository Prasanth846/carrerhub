import mysql.connector
from exception.database_conn_exception import DatabaseConnException
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(prop_file_name: str):
        try:
            conn_str = DBPropertyUtil.get_connection_string(prop_file_name)

            conn_params = {}
            for item in conn_str.split(';'):
                if '=' in item:
                    key, value = item.split('=', 1)
                    conn_params[key.strip()] = value.strip()

            conn = mysql.connector.connect(
                host=conn_params.get('host'),
                user=conn_params.get('user'),
                password=conn_params.get('password'),
                database=conn_params.get('database')
            )
            return conn

        except mysql.connector.Error as err:
            raise DatabaseConnException(f"❌ Database connection error: {err}")
        except Exception as e:
            raise DatabaseConnException(f"❌ Unexpected error: {e}")
