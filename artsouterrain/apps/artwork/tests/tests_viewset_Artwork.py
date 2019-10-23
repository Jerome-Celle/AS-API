import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from artsouterrain.apps.artwork.models import ArtworkType, Place, Artist, \
    Artwork


class ArtworkTests(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.artwork_type = ArtworkType.objects.create(
            name='Type 1'
        )

        self.artwork_type_2 = ArtworkType.objects.create(
            name='Type 2'
        )

        self.place = Place.objects.create(
            name='place 1'
        )

        self.place_2 = Place.objects.create(
            name='place 2'
        )

        self.artist = Artist.objects.create(
            first_name='artist 1'
        )

        self.artist_2 = Artist.objects.create(
            first_name='artist 2'
        )

        self.artwork = Artwork.objects.create(
            name='art 1',
            artist=self.artist,
            place=self.place,
            artwork_type=self.artwork_type
        )

        self.artwork_2 = Artwork.objects.create(
            name='art 1',
            artist=self.artist,
            place=self.place_2,
            artwork_type=self.artwork_type
        )

        self.artwork_3 = Artwork.objects.create(
            name='art 1',
            artist=self.artist,
            place=self.place_2,
            artwork_type=self.artwork_type_2
        )

        self.artwork_4 = Artwork.objects.create(
            name='art 1',
            artist=self.artist_2,
            place=self.place,
            artwork_type=self.artwork_type
        )

        self.artwork_5 = Artwork.objects.create(
            name='art 1',
            artist=self.artist_2,
            place=self.place_2,
            artwork_type=self.artwork_type
        )

        self.artwork_6 = Artwork.objects.create(
            name='art 1',
            artist=self.artist_2,
            place=self.place_2,
            artwork_type=self.artwork_type_2
        )

        self.artwork_7 = Artwork.objects.create(
            name='art 1',
            artist=self.artist_2,
            place=self.place,
            artwork_type=self.artwork_type_2
        )

        self.artwork_8 = Artwork.objects.create(
            name='art 1',
            artist=self.artist,
            place=self.place,
            artwork_type=self.artwork_type_2
        )

    def test_list_artwork(self):

        response = self.client.get(
            reverse('artwork-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 8)

    def test_get_artwork(self):
        response = self.client.get(
            reverse('artwork-detail', kwargs={'pk': self.artwork.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['name'], self.artwork.name)

    def test_list_filter_by_artist(self):
        response = self.client.get(
            reverse('artwork-list'),
            {'artist': self.artist.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 4)

    def test_list_filter_by_place(self):
        response = self.client.get(
            reverse('artwork-list'),
            {'place': self.place.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 4)

    def test_list_filter_by_artwork_type(self):
        response = self.client.get(
            reverse('artwork-list'),
            {'artwork_type': self.artwork_type.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 4)

    def test_update_artwork(self):
        response = self.client.patch(
            reverse('artwork-detail', kwargs={'pk': self.artwork.id}),
            {
                'artwork_type': 'fake',
                'name': 'fake'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )

    def test_delete_artwork(self):
        response = self.client.delete(
            reverse('artwork-detail', kwargs={'pk': self.artwork.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )

    def test_update_artwork_type(self):

        response = self.client.patch(
            reverse('artworktype-detail', kwargs={'pk': self.artwork_type.id}),
            {
                'key': 'fake',
                'name': 'fake'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )

    def test_delete_artwork_type(self):
        response = self.client.delete(
            reverse('artworktype-detail', kwargs={'pk': self.artwork_type.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )
