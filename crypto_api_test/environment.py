# environment.py
# def before_scenario(context, scenario):
#     pass
#
# def after_scenario(context, scenario):
#     pass

def before_scenario(context, scenario):
    context.websocket_endpoint = None
    context.instrument = None
    context.depth = None
    context.subscription_message = None
    context.websocket_client = None
    context.response = None
    context.updated_response = None

def after_scenario(context, scenario):
    if hasattr(context, 'websocket_client') and context.websocket_client:
        context.websocket_client.close()