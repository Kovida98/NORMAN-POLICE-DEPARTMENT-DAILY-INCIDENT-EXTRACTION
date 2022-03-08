import project0
#from project0 import __init__.project0.fetchincidents(None)
import pytest

def test_fetch_incidents():
    url1 = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-06_daily_incident_summary.pdf")
    data = project0.fetchincidents(url1)
    assert data is not None
