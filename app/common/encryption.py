from datetime import date, datetime, time

import cryptography
from cryptography.fernet import Fernet
import cryptography.fernet
from sqlalchemy import Column

from app.common.exceptions import Forbidden


class EncryptionManager:
    """
    Common encryption manager for datatypes
    """

    def __init__(self, key: str):
        self.cipher = Fernet(key.encode())

    def encrypt_str(self, data: str):
        """
        Encrypt string
        """
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt_str(self, data: str | Column[str]):
        """
        Decrypt string
        """
        try:
            return self.cipher.decrypt(data.encode()).decode()
        except cryptography.fernet.InvalidToken:
            raise Forbidden()

    def encrypt_boolean(self, data: bool):
        """
        Encrypt boolean
        """
        bool_str = str(data)  # Convert boolean to string ("True" or "False")
        return self.encrypt_str(bool_str)

    def decrypt_boolean(self, data: str | Column[str]):
        """
        Decrypt boolean
        """
        try:
            bool_str = self.decrypt_str(data)  # Decrypt to string
        except cryptography.fernet.InvalidToken:
            raise Forbidden()

        return bool_str == "True"  # Convert string back to boolean

    def encrypt_datetime(self, dt: datetime):
        """
        Encrypt datetime
        """
        dt_str = dt.isoformat()  # Convert datetime to ISO 8601 string format
        return self.encrypt_str(dt_str)

    def decrypt_datetime(self, data: str | Column[str]):
        """
        Decrypt datetime
        """
        try:
            dt_str = self.decrypt_str(data)  # Decrypt to ISO 8601 string
        except cryptography.fernet.InvalidToken:
            raise Forbidden()

        return datetime.fromisoformat(dt_str)  # Convert string back to datetime

    def encrypt_date(self, dt: date) -> str:
        """
        Encrypt date
        """
        dt_str = dt.isoformat()  # Convert date to ISO 8601 string format
        return self.encrypt_str(dt_str)

    def decrypt_date(self, data: str | Column[str]):
        """
        Decrypt date
        """
        try:
            dt_str = self.decrypt_str(data)  # Decrypt to ISO 8601 string
        except cryptography.fernet.InvalidToken:
            raise Forbidden()

        return date.fromisoformat(dt_str)  # Convert string back to date

    def encrypt_time(self, tm: time):
        """
        Encrypt time
        """
        tm_str = tm.isoformat()  # Convert time to ISO 8601 string format
        return self.encrypt_str(tm_str)

    def decrypt_time(self, data: str | Column[str]):
        """
        Decrypt time
        """
        try:
            tm_str = self.decrypt_str(data)  # Decrypt to ISO 8601 string
        except cryptography.fernet.InvalidToken:
            raise Forbidden()

        return time.fromisoformat(tm_str)  # Convert string back to time
