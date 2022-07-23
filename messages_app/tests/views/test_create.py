from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken
from users_app.serializers import UserDetailSerializer
from barters_app.models import SeedBarter
from rest_framework.test import force_authenticate
from messages_app import views
from rest_framework import status


class TestBarterCreate(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory(enforce_csrf_checks=True)

        self.sender = get_user_model().objects.create_user(
            email='sender@gardenbarter.com',
            password='pass3412'
        )

        self.recipient = get_user_model().objects.create_user(
            email='recipient@gardenbarter.com',
            password='pass3412'
        )

        self.access_token = str(
            RefreshToken.for_user(self.sender).access_token)

        self.seed_barter = SeedBarter.objects.create(
            creator=self.recipient,
            title='test barter title',
            description='test barter description',
            will_trade_for='item that will be traded',
            is_free=False,
            cross_street_1='123 Faux St.',
            cross_street_2='789 Impostor Rd',
            postal_code='99999',
            barter_type='seed',
            latitude='',
            longitude='',
            genus='leonarus',
            species='cardiaca',
            common_name='motherwort',
        )

        self.message_data = {
            "body": "Let's trade!"
        }

    def generate_request(self, data):
        '''return a Factory.post() request with the provided data'''
        return self.factory.post(
            reverse('messages_app:create'),
            data,
            format='json'
        )

    def test_message_create_success(self):
        request = self.generate_request(
            {
                'senderId': self.sender.id,
                'barterId': self.seed_barter.id,
                'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.recipient.inbox.conversations.count(), 1)
        
        conversation = self.recipient.inbox.conversations.first()
        self.assertEqual(conversation.messages.count(), 1)

        self.assertEqual(self.seed_barter.conversations.count(), 1)

    def test_message_create_fail(self):
        # missing senderId
        request = self.generate_request(
            {
                # 'senderId': self.sender.id,
                'barterId': self.seed_barter.id,
                'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], ['Missing senderId.'])

        # missing barterId
        request = self.generate_request(
            {
                'senderId': self.sender.id,
                # 'barterId': self.seed_barter.id,
                'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], ['Missing barterId.'])

        # missing barterType
        request = self.generate_request(
            {
                'senderId': self.sender.id,
                'barterId': self.seed_barter.id,
                # 'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], ['Missing barterType.'])

        # missing formData
        request = self.generate_request(
            {
                'senderId': self.sender.id,
                'barterId': self.seed_barter.id,
                'barterType': self.seed_barter.barter_type,
                # 'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], ['Missing formData object.'])

        # sender doesn't exist
        invalid_user_id = 999
        request = self.generate_request(
            {
                'senderId': invalid_user_id,
                'barterId': self.seed_barter.id,
                'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], [
                         f'User with id {invalid_user_id} not found.'])

        # barter doesn't exist
        invalid_barter_id = 999
        request = self.generate_request(
            {
                'senderId': self.sender.id,
                'barterId': invalid_barter_id,
                'barterType': self.seed_barter.barter_type,
                'formData': self.message_data
            }
        )
        force_authenticate(request, user=self.sender)

        response = views.create(request)

        self.assertIn('errors', response.data.keys())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['errors'], [
                         f"No barter of type '{self.seed_barter.barter_type}' with id {invalid_barter_id}"])