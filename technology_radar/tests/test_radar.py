import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_api_radar_list(client):
    res = client.get(reverse('api-radar-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_api_radar_detail(client):
    res = client.get(reverse('api-radar-detail', kwargs={'pk': 1}))
    assert res.status_code == 404


@pytest.mark.django_db
def test_api_blip_list(client):
    res = client.get(reverse('api-blip-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_api_blip_detail(client):
    res = client.get(reverse('api-blip-detail', kwargs={'pk': 1}))
    assert res.status_code == 404
