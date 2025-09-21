Feature: Automate WebSocket API 'book.{instrument_name}.{depth}'
  @normaltest2
  Scenario: Subscribe to the order book for a specific instrument and depth
    Given I have the WebSocket root endpoint "wss://stream.crypto.com/v2/market"
    And I want to subscribe to the order book for instrument "BTC_USDT" with depth "5"
    When I connect to the WebSocket and send the subscription message
    Then I should receive the order book data for "BTC_USDT" with depth "5"
  @normaltest2
  Scenario: Receive real-time updates for the subscribed order book
    Given I am subscribed to the order book for instrument "BTC_USDT" with depth "5"
    When the order book is updated
    Then I should receive the updated order book data