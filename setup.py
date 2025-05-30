import os
import shutil
from sql_db import SQL_DB

config = """
SERVER_DOMAIN=""
SERVER_HOST=localhost
SERVER_PORT=5000

REQ_LIMIT_PER_DAY=50

CUSTOM_DB=false
CUSTOM_URL_BLACKLIST_DB=false
DB_PATH=""
URL_BLACKLIST_PATH=""
"""

banner = r""" 
  _        _   _                      _____   _                      _     _    _   _____    _      
 | |      (_) | |                    / ____| | |                    | |   | |  | | |  __ \  | |     
 | |       _  | |__    _ __    ___  | (___   | |__     ___    _ __  | |_  | |  | | | |__) | | |     
 | |      | | | '_ \  | '__|  / _ \  \___ \  | '_ \   / _ \  | '__| | __| | |  | | |  _  /  | |     
 | |____  | | | |_) | | |    |  __/  ____) | | | | | | (_) | | |    | |_  | |__| | | | \ \  | |____ 
 |______| |_| |_.__/  |_|     \___| |_____/  |_| |_|  \___/  |_|     \__|  \____/  |_|  \_\ |______|

~ Junaid(www.abujuni.dev)                                                                                                    
"""
print(banner)
print("")

if os.path.exists("./config.env"):
    print("Config File  -   ✅")
else:
    print("Config File  -   ❌")
    print(" - Creating New config File...")
    with open("./config.env", "w") as f:
        f.write(config)
        print(" - OK!")

print("Setting up DB...")
print("LOGS", "##" * 5)

print("[INFO]   SQL DB Init!")
db = SQL_DB()

if os.path.exists("db/urls.db") == True:
    print("[INFO]   Existing DB found!")
    print("[INFO]   Checking Connection to Current DB...")
    connection = db.connect_db("./urls.db")
    print("[OK]   Connection : OK")
    db.close_db(connection)
else:
    print("[ERROR]  DB not found.")
    print("[INFO]  Creating New DB...")
    connection = db.init_db("./urls.db")

    table = """
    CREATE TABLE  LibreShortUrlsDB(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        name TEXT NOT NULL UNIQUE
    )
    """
    db.create_table(connection, table)
    db.close_db(connection)

    shutil.move("urls.db", "./db/urls.db")
    print("[OK]   DB Created!")

print("SETUP COMPLETED!")