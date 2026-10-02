import asyncio
import websockets

PORT = 8765  # Port the server listens on

connected_clients = set()  # All currently connected browsers


async def handle_client(websocket):
    """Called automatically each time a new browser connects."""

    connected_clients.add(websocket)
    print(f"[NEW] Client connected. Total: {len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"[MSG] {message}")

            # Send the message to every OTHER connected browser
            others = connected_clients - {websocket}

            if others:
                await asyncio.gather(
                    *[client.send(message) for client in others]
                )

    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        connected_clients.discard(websocket)
        print(
            f"[LEFT] Client disconnected. "
            f"Total: {len(connected_clients)}"
        )


async def main():
    print("===============================")
    print(" IoT Learning Hub - WebSocket Server")
    print(f" Listening on port {PORT}")
    print(" Open chat.html in any browser to connect")
    print("===============================")

    async with websockets.serve(
        handle_client,
        "0.0.0.0",
        PORT
    ):
        await asyncio.Future()  # Run forever


asyncio.run(main())
