import websocket
import json
import threading
import time
 # thisis a class
class WebSocketClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.ws = None
        self.connected = False
        self.response = None
        self.update_response = None
        self.stop_waiting = False

    def connect(self):
        self.ws = websocket.WebSocketApp(
            self.endpoint,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.thread = threading.Thread(target=self.ws.run_forever)
        self.thread.start()
        # Wait for connection to be established
        time.sleep(2)  # Adjust as necessary
        self.connected = True

    def on_open(self, ws):
        print("WebSocket connection opened")

    def on_message(self, ws, message):
        print(f"Received message: {message}")
        self.response = message
        data = json.loads(message)
        if data.get("method") == "update":
            self.update_response = message

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")
        self.connected = False

    def send(self, message):
        if self.ws:
            self.ws.send(message)
            print(f"Sent message: {message}")

    def receive(self):
        # Simple implementation to return the last received message
        # In a real scenario, you might want to handle multiple messages or specific types
        return self.response

    def wait_for_update(self):
        # Wait for an update message
        start_time = time.time()
        while not self.update_response and (time.time() - start_time) < 10:  # Timeout after 10 seconds
            time.sleep(0.1)
        update_response = self.update_response
        self.update_response = None  # Reset for future updates
        return update_response

    def close(self):
        if self.ws:
            self.ws.close()
        self.thread.join()