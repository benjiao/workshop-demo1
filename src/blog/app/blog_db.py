class BlogDB:
    def __init__(self, conn):
        self.conn = conn

    def getUserByUsername(self, username):
        cursor = self.conn.cursor()

        query = "SELECT * FROM user WHERE username=%(username)s"
        params = {'username': username}

        cursor.execute(query, params)
        user = cursor.fetchone()
        self.conn.commit()

        return user
