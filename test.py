import asyncio
import websockets
import json
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16.enums import Action

class ChargePoint(cp):
    async def send_boot_notification(self):
        payload = {
            "chargePointVendor": "Tesla",
            "chargePointModel": "Model X",
            "chargePointSerialNumber": "123456",
            "chargeBoxSerialNumber": "654321",
            "firmwareVersion": "v1.0.0",
            "iccid": "89012345678901234567",
            "imsi": "310260000000000",
            "meterType": "Type A",
            "meterSerialNumber": "000123456"
        }
        response = await self.call(Action.BootNotification, payload)
        print(f"BootNotification response: {response}")

async def connect_to_server():
    uri = "ws://localhost:9000"  # Replace with your server URI
    async with websockets.connect(uri) as websocket:
        charge_point_id = "CP_1"  # Replace with your ChargePoint ID
        charge_point = ChargePoint(charge_point_id, websocket)
        await charge_point.start()
        await charge_point.send_boot_notification()

if __name__ == "__main__":
    asyncio.run(connect_to_server())
