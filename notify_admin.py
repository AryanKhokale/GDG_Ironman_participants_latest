import httpx

REALTIME_URL = "http://127.0.0.1:9000/broadcast"

async def notify_admin(event_data: dict):

    async with httpx.AsyncClient() as client:

        await client.post(
            REALTIME_URL,
            json=event_data,
            timeout=5
        )