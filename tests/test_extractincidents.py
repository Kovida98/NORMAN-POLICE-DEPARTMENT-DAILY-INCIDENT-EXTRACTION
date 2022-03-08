import project0
import pytest

def test_extractincidents():
    url=("https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-06_daily_incident_summary.pdf")
    data = project0.fetchincidents(url)
    tuple_list = project0.extractincidents(data)
    assert tuple_list is not None

    assert type(tuple_list) == type([])

    for i in tuple_list:
        assert len(i) == 5

