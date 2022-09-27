Feature: Checking the connection and log out
    Scenario: The connection connects to the server
        Given the connection with the host "test.mosquitto.org", port 1883 and webport 80
        When the connection connects to the server
        And waiting for 2 seconds
        Then the connection must be connected

    Scenario: The connection connects to the wrong server 
        Given the connection with the host "test.mosquitto.ort", port 1883 and webport 80
        When the connection connects to the server
        And waiting for 5 seconds
        Then the connection must not be connected
