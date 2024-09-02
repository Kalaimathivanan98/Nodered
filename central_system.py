import asyncio
import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action
import json

class ChargePoint(cp):
    @on(Action.BootNotification)
    async def on_boot_notification(self, charging_station, reason, **kwargs):
        # Handle the BootNotification and store relevant data
        data = {
            "charging_station": charging_station,
            "reason": reason
        }
        print("Received BootNotification:", data)
        return {
            "currentTime": "2024-08-28T12:00:00Z",
            "interval": 10,
            "status": "Accepted"
        }

async def on_connect(websocket, path):
    charge_point_id = path.strip("/")
    charge_point = ChargePoint(charge_point_id, websocket)
    await charge_point.start()

async def main():
    server = await websockets.serve(on_connect, "localhost", 9000)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
