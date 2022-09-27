from abc import ABC, abstractmethod
from paho.mqtt.client import Client
from time import sleep


class IConnection(ABC):
    pass


class Connection(IConnection):
    def __init__(self, host, port, webport, logger=None):
        self._connected = False
        self.client = Client()
        self.client.on_connect = self._on_connect
        self._host = host 
        self._port = port 
        self._webport = webport
        self._logger = logger

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            self._connected = True
            if self._logger is not None:
                self._logger.info(f"Connect to the {self._host}:{self._port} successfully")
        else:
            self._connected = False

    @property
    def connected(self):
        return self._connected

    def connect(self) -> None:
        try:
            self.client.connect(self._host, self._port)
            self.client.loop_start()
        except:
            if self._logger is not None:
                self._logger.error(f"Connect to the {self._host}:{self._port} fail")
