import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_api_root(client):
    res = client.get(reverse('api-root'))
    assert res.status_code == 200
