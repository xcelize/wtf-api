from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, force_authenticate
from authenticate.models import User


class CreateFilmRatingTestCase(APITestCase):
    def test_is_not_authorized(self):
        response = self.client.post(reverse('create_film_rating'))
        print(response.data)
        self.assertEqual(response.status_code, 401)

    def test_is_authorized(self):
        user = User.objects.get(email='baptiste@baptiste.fr')

        # Make an authenticated request to the view...
        request = self.client.post(reverse('create_film_rating'))
        force_authenticate(request, user=user)
        print(request)
        self.assertEqual(request.data, 401)


'''class ListFilmsTestCase(APITestCase):

    def setUp(self):
        Films(id_video = 1, titre = 'bibi', date_sortie = datetime.now(), poster = 'img.jpg', plot ='description', vo ='fr', duree=120).save()

    def test_list_films(self):
        url = reverse('list_film')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

#class ListCategoriesTestCase(APITestCase):
  #  def test_list_categories(self):
   #     url = reverse('list_categories')
    #    response = self.client.get(url, format='json')
     #   self.assertEqual(response.status_code, 200)'''
