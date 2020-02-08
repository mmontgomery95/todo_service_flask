import sqlite3

DB_PATH = './todo.db' # update this path accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(item):
    try:
        conn = sqlite3.connect(DB_PATH)

        # once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # keep the initial status as Not Started
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))

        # commit to save the change
        conn.commit()
        return{"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None