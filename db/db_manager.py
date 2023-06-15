import aiomysql
from aiomysql.connection import IntegrityError
import logging


class DBManager:
    def __init__(self, **kwargs):
        self.host = kwargs.get('HOST')
        self.port = kwargs.get('PORT')
        self.user = kwargs.get('USER')
        self.password = kwargs.get('PASSWORD')
        self.db = kwargs.get('DB')
        self.conn = None
        self.cursor = None

    async def connect(self):
        self.conn = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        self.cursor = await self.conn.cursor()

    async def check_create_table(self):
        await self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dumps_user_data (
                id INT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                birthday TEXT,
                title TEXT,
                personal_id TEXT
            )
        ''')

    async def insert_data(self, data):
        try:
            data = [
                data.get('Id'),
                data.get('First Name'),
                data.get('Last Name'),
                data.get('Birthday'),
                data.get('Title'),
                data.get('Personal ID')
            ]
            await self.cursor.execute('''
                INSERT INTO dumps_user_data (id, first_name, last_name, birthday, title, personal_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', data)
        except IntegrityError as ex:
            logging.warning(f"Such record already exists {ex}")
        except Exception as ex:
            logging.warning(f"Error occurred: {ex.__class__.__name__}")

    async def commit(self):
        await self.conn.commit()

    async def close_connection(self):
        await self.cursor.close()
