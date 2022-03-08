import project0
import pytest

def test_fetch_incidents():
    url1 = ("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-06_daily_incident_summary.pdf")
    data = project0.fetchincidents(url1)
    assert data is not None
