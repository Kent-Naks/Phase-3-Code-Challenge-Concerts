from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import models from the project
from models import Base  # Ensures Alembic has access to model metadata

# Alembic Config object
config = context.config

# Set up Python logging based on the .ini file configuration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for 'autogenerate' support
target_metadata = Base.metadata
