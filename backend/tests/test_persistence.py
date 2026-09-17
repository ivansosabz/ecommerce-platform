import importlib
import re
from pathlib import Path

from sqlalchemy import CheckConstraint, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import configure_mappers
from sqlalchemy.schema import CreateTable


def test_models_preserve_approved_mvp_schema():
    models = importlib.import_module("app.models")
    dbml = (Path(__file__).parents[2] / "docs/database/ecommerce.dbml").read_text(
        encoding="utf-8"
    )
    tables = re.findall(r"Table (\w+) \{(.*?)\n\}", dbml, re.DOTALL)
    expected = {
        name: body
        for name, body in tables
        if name not in {"facturas", "detalles_factura"}
    }
    assert set(models.Base.metadata.tables) == set(expected)
    configure_mappers()
    for name, body in expected.items():
        table = models.Base.metadata.tables[name]
        columns = re.findall(
            r"^  (\w+) ([\w(),]+)(?: \[([^\n]+)\])?$", body, re.MULTILINE
        )
        assert set(table.columns.keys()) == {column for column, _, _ in columns}
        for column, _, options in columns:
            assert table.c[column].nullable == ("not null" not in options)
            assert table.c[column].primary_key == ("pk" in options.split(", "))
            if "unique" in options:
                assert any(
                    isinstance(c, UniqueConstraint)
                    and list(c.columns.keys()) == [column]
                    for c in table.constraints
                )
            if "default:" in options:
                assert table.c[column].server_default is not None
        for check, check_name in re.findall(r"`([^`]+)` \[name: '([^']+)'\]", body):
            assert any(
                isinstance(c, CheckConstraint)
                and c.name == check_name
                and str(c.sqltext) == check
                for c in table.constraints
            )
        for index_name in re.findall(r"name: '(ix_[^']+)'", body):
            assert index_name in {i.name for i in table.indexes}
        for unique_name in re.findall(r"name: '(uq_[^']+)'", body):
            assert unique_name in {c.name for c in table.constraints}
        assert str(CreateTable(table).compile(dialect=postgresql.dialect()))
    refs = re.findall(
        r"Ref (\w+): (\w+)\.(\w+) > (\w+)\.(\w+) \[delete: ([^\]]+)\]", dbml
    )
    refs.append(
        ("fk_carritos_usuario", "carritos", "usuario_id", "usuarios", "id", "cascade")
    )
    for constraint_name, source, column, target, target_column, action in refs:
        if source not in expected:
            continue
        constraint = next(
            c
            for c in models.Base.metadata.tables[source].constraints
            if isinstance(c, ForeignKeyConstraint) and c.name == constraint_name
        )
        assert constraint.ondelete == action.upper()
        assert list(constraint.columns.keys()) == [column]
        assert constraint.elements[0].target_fullname == f"{target}.{target_column}"


def test_session_dependency_does_not_require_connection():
    from app.core.config import Settings
    from app.db.session import Database

    async def exercise():
        database = Database(
            Settings(database_url="postgresql+psycopg://test:test@localhost/test")
        )
        async with database.session() as session:
            assert session.is_active
        await database.dispose()

    import asyncio

    asyncio.run(exercise())
