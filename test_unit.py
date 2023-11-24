import pytest
from client import ClientSide
from database import db
import socket

FILENAME = r"sqlfile.db"

class TestClient:
    def test_msgFormat(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs = ClientSide(client)
        send_length, msg = cs.msgFormat("Hello")
        assert send_length == b'5                                                               '
        assert msg == b'Hello'

    def test_sendFunc(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs = ClientSide(client)
        cs.connectFunc('192.168.50.81', 5050)
        received_message = cs.sendFunc("Hello")
        assert received_message == "Server sent - Msg received!"

class TestDatabase:
    def test_sqlQueryCommandReturnZero(self):
        query = '''DELETE FROM MessageLogs'''
        sqc = db.sqlQueryCommand(FILENAME, query)
        assert sqc == 0

    def test_sqlQueryCommandReturnId(self):
        query = '''DELETE FROM MessageLogs'''
        sqc = db.sqlQueryCommand(FILENAME, query)
        query = '''INSERT INTO MessageLogs (id, recv_message) VALUES (1, 'Hello-1'), (2, 'Hello-2'), (3, 'Hello-3')'''
        sqc = db.sqlQueryCommand(FILENAME, query)
        query = '''SELECT * FROM MessageLogs WHERE id = 2'''
        sqc = db.sqlQueryCommand(FILENAME, query)
        assert sqc[0] == 2
        assert sqc[1] == 'Hello-2'