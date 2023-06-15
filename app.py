from files_manager.files_manager import FilesManager
from db.db_manager import DBManager
from settings import DBCreds
import os


class App:
    PATH = os.path.join(os.getcwd(), 'files_manager')

    async def load_files(self):
        db_manager = DBManager(**DBCreds)
        files_manager = FilesManager()
        await db_manager.connect()
        await db_manager.check_create_table()

        files = files_manager.get_files()

        for file in files:
            file_data = files_manager.get_file_data(file)
            await db_manager.insert_data(file_data)

        await db_manager.commit()
        await db_manager.close_connection()
