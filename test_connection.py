import sys
import os

# This makes sure Python can find the util folder
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from util.db_conn_util import DBConnUtil

# Use the connection method and test
conn = DBConnUtil.get_connection("util/db.properties")
if conn:
    print("✅ Connection successful!")
    conn.close()
else:
    print("❌ Connection failed.")
