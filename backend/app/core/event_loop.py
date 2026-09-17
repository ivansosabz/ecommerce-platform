import asyncio


def create_event_loop() -> asyncio.AbstractEventLoop:
    """SelectorEventLoop permite usar psycopg asíncrono también en Windows."""
    return asyncio.SelectorEventLoop()
