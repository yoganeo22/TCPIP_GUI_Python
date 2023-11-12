import pytest
from client import ClientSide
from database import db

FILENAME = r"sqlfile.db"

class TestClient:
    def test_msgFormat(self):
        cs = ClientSide()
        send_length, msg = cs.msgFormat("Hello")
        assert send_length == b'5                                                               '
        assert msg == b'Hello'

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
