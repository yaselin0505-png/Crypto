# cases.feature
# crypto/crypto_api_test/features/cases.feature

Feature: get the Candlestick Data
  @normaltest
  Scenario: get the valid data
    Given I have a valid api
    When send the valid request for candlestick
    Then response is 200
    And the response should be included valid data

  @normaltest
  Scenario: get the invalid data
    Given I have a valid api
    When send an invalid request
    Then response is not 200