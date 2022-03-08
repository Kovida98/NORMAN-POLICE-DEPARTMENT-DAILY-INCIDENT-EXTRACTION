import project0
import pytest

def test_createDB():
    DB_name='normanpd.db'
    cursor = project0.createdb()
    x=cursor.execute('SELECT count(*) from incidents')
    for row in x:
        assert row[0] >=0
