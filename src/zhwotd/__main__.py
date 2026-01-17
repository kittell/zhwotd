from zhwotd.db.init_db import init_db
from zhwotd.app import Application

def main():
    # Startup tasks
    init_db()

    # Go
    app = Application()
    app.run()
    return

if __name__ == '__main__':
    main()