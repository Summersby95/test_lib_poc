"""MongoDB Client Module."""
import os
from pymongo import MongoClient
from pymongo.collection import Collection
from models import Token


class MongoWrapper:
    """Mongo Client Wrapper."""

    def __init__(self) -> None:
        """Initialization method for MongoClient class."""
        mongo_uri = os.getenv("MONGO_URI")
        db_name = os.getenv("MONGO_DB")

        client = MongoClient(mongo_uri)
        self.db = client[db_name]

        self.token_coll: Collection = self.db.tokens
        self.test_coll: Collection = self.db.tests

    def find_token(self, token: Token) -> None:
        """Searches token collection for a specified token.

        Args:
            token (str): Token to find.
        """
        return self.token_coll.find_one(Token.model_dump())
    
    def insert_token(self, token: Token) -> None:
        """Insert token into Token collection.

        Args:
            token (Token): Token object to insert.
        """
        return self.token_coll.insert_one(token)
