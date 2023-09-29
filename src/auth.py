"""Authentication Module."""
from models import Token
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from clients.mongo import MongoClient
import logging

LOG = logging.getLogger(__name__)

TOKEN_SCHEMA = APIKeyHeader(name="Token")


def validate_token(token: str = Security(TOKEN_SCHEMA)) -> None:
    """Validates a API request token.

    Args:
        token (str, optional): Token to validate. Defaults to Security(TOKEN_SCHEMA).

    Raises:
        HTTPException: 403, if token is not valid.
    """
    client = MongoClient()
    token = Token(token=token)

    LOG.debug("Validating token.")
    if not client.find_token(token):
        LOG.warning("Invalid Token.")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Token."
        )
