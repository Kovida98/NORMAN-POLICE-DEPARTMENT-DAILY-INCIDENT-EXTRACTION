import project0
import pytest

def test_status():
    url = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-06_daily_incident_summary.pdf")
    data = project0.fetchincidents(url)
    t_list = project0.extractincidents(data)
    cur=project0.createdb()
    cursor = project0.populatedb(cur,t_list)
    l=project0.status(cursor)
    for i in l:
        assert len(i) == 2
