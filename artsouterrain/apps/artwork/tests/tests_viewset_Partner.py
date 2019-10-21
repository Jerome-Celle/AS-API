import json

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from artsouterrain.apps.artwork.models import PartnerType, Partner


class PartnerTexts(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

        self.partner_type = PartnerType.objects.create(
            key='TYPE_1',
            name='Type 1'
        )

        self.partner_type_2 = PartnerType.objects.create(
            key='TYPE_2',
            name='Type 2'
        )

        self.partner = Partner.objects.create(
            name='Partner 1',
            link='http://partner1.com',
            description='partner 1 description',
            partner_type=self.partner_type
        )
        self.partner_2 = Partner.objects.create(
            name='Partner 2',
            link='http://partner2.com',
            description='partner 2 description',
            partner_type=self.partner_type)
        self.partner_3 = Partner.objects.create(
            name='Partner 3',
            link='http://partner3.com',
            description='partner 3 description',
            partner_type=self.partner_type_2)

    def test_list_partner(self):

        response = self.client.get(
            reverse('partner-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 3)

    def test_get_partner(self):
        response = self.client.get(
            reverse('partner-detail', kwargs={'pk': self.partner.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['name'], self.partner.name)
        self.assertEqual(response_data['link'], self.partner.link)
        self.assertEqual(response_data['description'],
                         self.partner.description)
        self.assertEqual(response_data['partner_type']['key'],
                         self.partner.partner_type.key)

    def test_list_filter_by_type_key(self):
        response = self.client.get(
            reverse('partner-list'),
            {'partner_type__key': self.partner_type.key}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 2)

    def test_list_filter_by_type_id(self):
        response = self.client.get(
            reverse('partner-list'),
            {'partner_type': self.partner_type.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            response.content,
        )

        response_data = json.loads(response.content)

        self.assertEqual(response_data['count'], 2)

    def test_update_partner(self):
        response = self.client.patch(
            reverse('partner-detail', kwargs={'pk': self.partner.id}),
            {
                'partner_type': 'fake',
                'name': 'fake'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )

    def test_delete_partner(self):
        response = self.client.delete(
            reverse('partner-detail', kwargs={'pk': self.partner.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )

    def test_update_partner_type(self):

        response = self.client.patch(
            reverse('partnertype-detail', kwargs={'pk': self.partner_type.id}),
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

    def test_delete_partner_type(self):
        response = self.client.delete(
            reverse('partnertype-detail', kwargs={'pk': self.partner_type.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_501_NOT_IMPLEMENTED,
            response.content,
        )
