from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from movies.models import get_postgres_uri

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()