import json
from behave import given, when, then
from crypto_api_test.utils.websocket_client import WebSocketClient
# from crypto_api_test.utils.test_data import TEST_INSTRUMENT, TEST_DEPTH

@given('I have the WebSocket root endpoint "{endpoint}"')
def step_given_websocket_endpoint(context, endpoint):
    context.websocket_endpoint = endpoint

@given('I want to subscribe to the order book for instrument "{instrument}" with depth "{depth}"')
def step_given_subscribe_order_book(context, instrument, depth):
    context.instrument = instrument
    context.depth = depth
    context.subscription_message = {
        "id": 1,
        "method": "subscribe",
        "params": {
            "channel": f"book.{instrument}.{depth}"
        }
    }

@when('I connect to the WebSocket and send the subscription message')
def step_when_connect_and_subscribe(context):
    context.websocket_client = WebSocketClient(context.websocket_endpoint)
    context.websocket_client.connect()
    context.websocket_client.send(json.dumps(context.subscription_message))

@then('I should receive the order book data for "{instrument}" with depth "{depth}"')
def step_then_receive_order_book_data(context, instrument, depth):
    response = context.websocket_client.receive()
    assert response is not None, "No response received from WebSocket"
    data = json.loads(response)
    assert data.get("method") == "subscription", "Not a subscription response"
    assert data.get("params", {}).get("channel") == f"book.{instrument}.{depth}", "Incorrect channel in response"

@given('I am subscribed to the order book for instrument "{instrument}" with depth "{depth}"')
def step_given_already_subscribed(context, instrument, depth):
    context.instrument = instrument
    context.depth = depth
    # Assuming the connection and subscription already happened in a previous step

@when('the order book is updated')
def step_when_order_book_updated(context):
    # This step might involve waiting for an update or simulating an update
    # For simplicity, we assume the WebSocket client has a method to wait for updates
    context.updated_response = context.websocket_client.wait_for_update()

@then('I should receive the updated order book data')
def step_then_receive_updated_order_book_data(context):
    assert context.updated_response is not None, "No updated response received"
    data = json.loads(context.updated_response)
    assert data.get("method") == "update", "Not an update response"
    assert data.get("params", {}).get("channel") == f"book.{context.instrument}.{context.depth}", "Incorrect channel in update response"