import pymongo
import os

from .errors import FileAlreadyExistsForCurrentUserError
from dotenv import load_dotenv
load_dotenv()


class MusicData:
    def __init__(self) -> None:
        """
        Connect to MongoDB
        """
        client = pymongo.MongoClient(os.getenv("MONGO_URI"))
        self.db = client[os.getenv("MONGO_DB")][os.getenv("DATA_COLLECTION")]

    def insert_data(self, name: str, email: str, filename: str) -> None:
        """Insert file name and data into db

        Args:
            name: User Name
            email: User Email ID
            filename: Name of File

        Returns:
            None
        """
        if self.db.find_one({"Email": email, "Filename": filename}):
            raise FileAlreadyExistsForCurrentUserError(
                "File Already Exists With This Name For Current User")

        data = {"Name": name, "Email": email, "Filename": filename}
        self.db.insert_one(data)

    def delete_data(self, email: str, filename: str) -> None:
        """Delete file and related data from db

        Args:
            email: User Email ID
            filename: Name of File

        Returns:
            None
        """
        pass
