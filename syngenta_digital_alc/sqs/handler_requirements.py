from syngenta_digital_alc.sqs.event_client import EventClient


def handler_requirements(**kwargs):
    def decorator_func(func):
        def wrapper(event, context):
            client = EventClient(event)
            func(client)
        return wrapper
    return decorator_func
