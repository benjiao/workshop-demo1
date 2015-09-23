class UserDB:
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

    def getUsers(self):
        cursor = self.conn.cursor()

        query = "SELECT * FROM user"

        cursor.execute(query)
        users = cursor.fetchall()
        self.conn.commit()

        return users

    def createUser(self, username, name, password):
        cursor = self.conn.cursor()

        query = """ INSERT INTO user SET
            username=%(username)s,
            name=%(name)s,
            password=%(password)s
        """

        params = {
            "username": username,
            "name": name,
            "password": password
        }

        try:
            cursor.execute(query, params)
            self.conn.commit()
            return True

        except:
            self.conn.rollback()
            cursor.close()
            return False
