import os
import time
import sys

import psycopg2


def main():
    dsn = os.environ["DATABASE_URL"]

    for i in range(30):
        try:
            conn = psycopg2.connect(dsn)
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS init_log ("
                "id SERIAL PRIMARY KEY, ts TIMESTAMPTZ DEFAULT now())"
            )
            cur.execute("INSERT INTO init_log DEFAULT VALUES;")
            cur.close()
            conn.close()
            print("init ok")
            return 0
        except Exception as e:
            print("init attempt failed, retrying...", e)
            time.sleep(1)

    print("init failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
