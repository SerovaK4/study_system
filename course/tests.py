from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@sky.pro',
        )
        self.user.set_password('test123')
        self.user.save()
        self.user.set_password('test123')
        self.user.save()

        self.course = Course.objects.create(
            name='test course',
            description='test description',
        )

        self.lesson = Lesson.objects.create(
            name='test',
            description='description',
            link_video='https://www.sky_youtube.com',
            course=self.course,
            owner=self.user,
        )

    def test_create_lesson(self):
        """Тестирование создания урока"""
        data = {
            'name': 'tester',
            'description': 'description',
            'link_video': 'https://www.sky_youtube.com',
            'course': self.course.pk,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/lesson/create/',
            data=data,
        )
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.json(),
            {'name': 'tester', 'img': None, 'description': 'description', 'link_video': 'https://www.sky_youtube.com',
             'course': 1, 'owner': 1}
        )

        self.assertTrue(
            Lesson.objects.all().exists()
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""
        response = self.client.get(
            '/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        print(response.json())
        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 5, 'payment': [], 'last_payment': 0, 'name': 'test', 'img': None, 'description': 'description',
                 'link_video': 'https://www.sky_youtube.com', 'course': 5, 'owner': 5}]}

        )

    def test_lesson_retrieve(self) -> None:

        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/lesson/{self.lesson.pk}/')

        print(response.json())

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        response = response.json()

        self.assertEqual(response.get('name'), 'test')
        self.assertEqual(response.get('description'), 'description')
        self.assertEqual(response.get('img'), None)
        self.assertEqual(response.get('link_video'), 'https://www.sky_youtube.com')
        self.assertEqual(response.get('course'), self.course.pk)
        self.assertEqual(response.get('owner'), self.user.pk)

    def test_lesson_update(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'updated tester',
            'description': 'updated description',
        }

        response = self.client.put(
            f'/lesson/update/{self.lesson.pk}/', data=data,
        )

        print(response.status_code)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertEqual(response.get('name'), 'updated tester')
        self.assertEqual(response.get('description'), 'updated description')
        self.assertEqual(response.get('img'), None)
        self.assertEqual(response.get('link_video'), 'https://www.sky_youtube.com')
        self.assertEqual(response.get('course'), self.course.pk)
        self.assertEqual(response.get('owner'), self.user.pk)

    def test_lesson_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            f'/lesson/delete/{self.lesson.pk}/',
        )

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Lesson.objects.all().exists(),
        )

    def tearDown(self) -> None:
        self.user.delete()
        self.course.delete()
        self.lesson.delete()