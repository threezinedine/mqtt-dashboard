import unittest
from src.cores import Connection
from time import sleep
from unittest.mock import Mock
from src.cores.loggings import ILogger


class ConnectionTest(unittest.TestCase):
    correct_host = "test.mosquitto.org"
    wrong_host = "test.mosquitto.ort"
    port = 1883
    webport = 80

    def setUp(self):
        self.logger = Mock(spec=ILogger)

    def test_when_the_connection_connects_to_the_test_server_then_the_connection_must_be_connected(self):
        connection = Connection(self.correct_host, self.port, self.webport)
        connection.connect()
        sleep(1)

        assert connection.connected

    def test_when_the_connection_connects_to_the_wrong_test_server_then_the_connection_must_not_be_connected(self):
        connection = Connection(self.wrong_host, self.port, self.webport) 
        connection.connect()
        sleep(1)

        assert not connection.connected

    def test_when_the_connection_connects_to_the_test_server_then_the_logger_must_be_info(self):
        connection = Connection(self.correct_host, self.port, self.webport, self.logger)
        connection.connect()
        sleep(1)

        self.logger.info.assert_called_once_with(f"Connect to the {self.correct_host}:{self.port} successfully")

    def test_when_the_connection_connects_to_the_test_server_then_the_logger_must_be_error(self):
        connection = Connection(self.wrong_host, self.port, self.webport, self.logger)
        connection.connect()
        sleep(1)

        self.logger.error.assert_called_once_with(f"Connect to the {self.wrong_host}:{self.port} fail")
