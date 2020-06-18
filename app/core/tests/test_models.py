from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@gmail.com', password='testpass'):
    '''Create Sample User'''
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        ''' test creating a new user with an email is successful'''
        email = 'test@gmail.com'
        password = 'abc123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test if email for new user is normalized'''
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='abc123'
            )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test if no email is passed then there'll be an error'''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='abc123'
                )

    def test_create_superuser_is_successful(self):
        '''Tests to see if superuser is created successfully'''

        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='abc123'
            )
        self.assertEqual(user.email, 'test@gmail.com')
        self.assertTrue(user.check_password('abc123'))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser_invalid_email(self):
        '''Tests to see if an invalid email raises an error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                email=None,
                password='abc123'
                )

    def test_create_superuser_extra_fields(self):
        '''Tests to see if extra fields are saved when creating superuser'''
        user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='abc123',
            name='thaddeus'
            )
        self.assertEqual(user.name, 'thaddeus')

    def test_tag_str(self):
        '''Test the tag string representation'''
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        '''Test the ingredient string representation'''
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
