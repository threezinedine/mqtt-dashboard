from behave import given, when, then
from src.cores import Connection
from time import sleep


@given("the connection with the host \"{host}\", port {port} and webport {webport}")
def given_the_connection_with_test_params(context, host, port, webport):
    context.connection = Connection(host, int(port), int(webport))

@when("the connection connects to the server")
def when_the_connection_connects_to_the_server(context):
    context.connection.connect()

@when("waiting for {sleep_time} seconds")
def when_sleep_for_seconds(context, sleep_time):
    sleep(int(sleep_time))

@then("the connection must be connected")
def then_the_connection_must_be_connected(context):
    assert context.connection.connected

@then("the connection must not be connected")
def then_the_connection_must_not_be_connected(context):
    assert not context.connection.connected
