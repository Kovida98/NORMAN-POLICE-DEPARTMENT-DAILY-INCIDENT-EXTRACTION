import sqlite3

import project0
import pytest

def test_populateDB():
    url = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-06_daily_incident_summary.pdf")
    database = 'normanpd.db'
    data = project0.fetchincidents(url)
    t_list = project0.extractincidents(data)
    sql = sqlite3.connect(database)
    cur = sql.cursor()
    for row in cur.execute('SELECT * FROM incidents'):
        assert len(row) == 5

