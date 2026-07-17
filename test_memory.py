import asyncio

from app.services.memory_manager import memory_manager


async def main():

    await memory_manager.process_message(
        user_id=123,
        message="سلام اسم من علی است و دانشگاه من گیلان است"
    )


asyncio.run(main())