import asyncio
from datetime import datetime
import serial

import aioconsole
import websockets

from common.structures import Message

#95.163.236.35
WS_URL = 'ws://95.163.236.35:8000/room'


async def connect(url):
    while True:
        try:
            return await websockets.connect(url)
        except ConnectionRefusedError:
            print("Reconnecting...")


async def listen_room(ws):
    while True:
        raw_data = await ws.recv()
        message = Message.from_json(raw_data)
        await aioconsole.aprint(message.to_dict())


async def listen_input(ws, user):
    while True:
        text = await read_arduino()

        message = Message(
            text=text,
            time=datetime.now(),
            user=user,
        ).to_json(ensure_ascii=False)

        await ws.send(message)


async def read_arduino():
    port = serial.Seril("/dev/ttyACM0", 9600)
    while True:
        data = port.readline().decode("utf-8").strip()
        if data:
            return data.encode("utf-8")


async def main():
    name = input('Введите имя: ')
    room_name = input('Введите комнату: ')

    websocket = await connect(f'{WS_URL}/{room_name}?name={name}')

    await asyncio.gather(
        listen_room(websocket),
        listen_input(websocket, name),
    )


if __name__ == '__main__':
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    asyncio.run(main())
