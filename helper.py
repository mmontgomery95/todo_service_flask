import sqlite3

DB_PATH = "./todo.db"  # update this path accordingly
NOTSTARTED = "Not Started"
INPROGRESS = "In Progress"
COMPLETED = "Completed"


def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        # once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # keep the initial status as Not Started
        c.execute("insert into items(item, status) values(?,?)", (item, NOTSTARTED))

        # commit to save the change
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print("Error: ", e)
        return None


def get_all_items():
    # returns number of items and names of items returned by query
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items")
        rows = c.fetchall()  # returns all records; use c.fetchone() for a single item
        return {"count": len(rows), "items": rows}
    except Exception as e:
        print("Error: ", e)
        return None


def get_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from items where item=?", (item))
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print("Error: ", e)
        return None


def update_status(item, status):
    # check if the passed status is a valid value
    clean_status = status.lower().strip()
    if clean_status == "not started":
        status = NOTSTARTED
    elif clean_status == "in progress":
        status = INPROGRESS
    elif clean_status == "completed":
        status = COMPLETED
    else:
        print("Invalid Status: '%s'" % status)
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("update items set status=? where item=?", (status, item))
        conn.commit()
        return {item: status}
    except Exception as e:
        print("Error: ", e)
        return None


def delete_item(item):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("delete from items where item=?", (item,))
        conn.commit()
        return {"item": item}
    except Exception as e:
        print("Error: ", e)
        return None
