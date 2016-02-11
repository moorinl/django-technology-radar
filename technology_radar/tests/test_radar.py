import pytest

from django.core.urlresolvers import reverse


@pytest.mark.django_db
def test_radar_list(client):
    res = client.get(reverse('radar-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_radar_detail(client):
    res = client.get(reverse('radar-detail', kwargs={'pk': 1}))
    assert res.status_code == 404


@pytest.mark.django_db
def test_blip_list(client):
    res = client.get(reverse('blip-list'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_blip_detail(client):
    res = client.get(reverse('blip-detail', kwargs={'pk': 1}))
    assert res.status_code == 404
