
from behave import given, when, then
from crypto_api_test.utils.api_client import APIClient
# import json
# crypto_api_test/features/steps/candlestick_steps.py

@given('I have a valid api')
def step_given_valid_api_root(context):
    context.api = APIClient()

@when('send the valid request for candlestick')
def step_when_request_btc_usdt_1m(context):
    try:
        context.response = context.api.get_candlestick(instrument_name="BTC_USDT", timeframe="1m")
    except Exception as e:
        context.exception = e

@then('response is 200')
def step_then_response_status_200(context):
    if hasattr(context, 'exception'):
        raise context.exception
    assert context.response['code'] == 0  # 根据 Crypto.com API，成功时返回 code: 0

@then('the response should be included valid data')
def step_then_response_contains_valid_data(context):
    if hasattr(context, 'exception'):
        raise context.exception
    assert 'data' in context.response
    data = context.response['data']
    assert isinstance(data, list)
    if data:
        assert len(data[0]) >= 6  # 假设每个蜡烛是一个包含至少6个值的列表

@when('send an invalid request')
def step_when_request_invalid_instrument(context):
    try:
        context.response = context.api.get_candlestick(instrument_name="INVALID_PAIR", timeframe="1m")
    except Exception as e:
        context.exception = e

@then('response is not 200')
def step_then_response_status_not_200(context):
    if hasattr(context, 'exception'):
        # 比如请求失败，抛出了异常，可以认为测试通过（因为确实没成功）
        return
    assert context.response['code'] != 0  # 失败时 code 不为 0