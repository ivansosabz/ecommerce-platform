import asyncio

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

from app.core.config import Settings
from app.core.event_loop import create_event_loop
from app.models import Base


def run_migrations(connection):
    context.configure(
        connection=connection, target_metadata=Base.metadata, compare_type=True
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_online():
    engine = create_async_engine(Settings().database_url, poolclass=NullPool)
    try:
        async with engine.connect() as connection:
            await connection.run_sync(run_migrations)
    finally:
        await engine.dispose()


if context.is_offline_mode():
    context.configure(
        url=Settings().database_url,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    asyncio.run(run_online(), loop_factory=create_event_loop)
