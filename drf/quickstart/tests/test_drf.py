import pytest
from rest_framework.reverse import reverse


@pytest.fixture
def resp(client):
    return client.get(reverse('rest_framework:login'))


def test(resp):
    assert resp.status_code == 200
