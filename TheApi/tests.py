
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory, force_authenticate, APIClient
from TheApi.views import CreateRatingFilm
from authenticate.models import User
from authenticate.views import CreateFavorisFilmView


class CreateFilmRatingTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(CreateFilmRatingTestCase, cls).setUpClass()
        # create a User model object in temporary database.
        user = User(email='tom', password='tom')
        user.save()
        # get employee user.
        CreateFilmRatingTestCase.user = User.objects.get(email='tom')
        print(user)

    def test_is_not_authorized(self):
        response = self.client.post(reverse('create_film_rating'))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_is_authorized(self):
        factory = APIRequestFactory()
        view = CreateRatingFilm.as_view()

        # Make an authenticated request to the view...
        request = factory.post(reverse('create_film_rating'))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertNotEqual(response, 401)


class CreateFavorisFilmTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(CreateFavorisFilmTestCase, cls).setUpClass()
        # create a User model object in temporary database.
        user = User(email='tom', password='tom')
        user.save()
        # get employee user.
        CreateFavorisFilmTestCase.user = User.objects.get(email='tom')
        print(user)

    def test_is_not_authorized(self):
        response = self.client.post(reverse('create_favoris_film'))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_is_authorized(self):
        factory = APIRequestFactory()
        view = CreateFavorisFilmView.as_view()

        # Make an authenticated request to the view...
        request = factory.post(reverse('create_favoris_film'))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertNotEqual(response, 401)


class CreateFavorisSerieTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(CreateFavorisSerieTestCase, cls).setUpClass()
        # create a User model object in temporary database.
        user = User(email='tom', password='tom')
        user.save()
        # get employee user.
        CreateFavorisSerieTestCase.user = User.objects.get(email='tom')
        print(user)

    def test_is_not_authorized(self):
        response = self.client.post(reverse('create_favoris_serie'))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_is_authorized(self):
        factory = APIRequestFactory()
        view = CreateFavorisFilmView.as_view()

        # Make an authenticated request to the view...
        request = factory.post(reverse('create_favoris_serie'))
        force_authenticate(request, user=self.user)
        response = view(request)
        self.assertNotEqual(response, 401)