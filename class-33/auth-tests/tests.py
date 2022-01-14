from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from unittest import skip

from .models import Post
from .views import PostsList, PostsDetail


class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'Title of Blog')
        self.assertEqual(post.body, 'Words about the blog')



class APITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_post.save()

    def test_list(self):
  
        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='tester')
        view = PostsList.as_view()

        # Make an authenticated request to the view...
        url = reverse('posts_list')
        request = factory.get(url)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_detail(self):

        response = self.client.get(reverse('posts_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'title': 'Title of Blog',
            'body': 'Words about the blog',
            'author': 1,
        })

    def test_create(self):
        
        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='tester')
        view = PostsList.as_view()

        # Make an authenticated request to the view...
        data = {
            "title":"Testing is Fun!!!",
            "body":"when the right tools are available",
            "author":1,
        }

        url = reverse('posts_list')
        request = factory.post(url, data)
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, data['title'])

    def test_update(self):
        
        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='tester')
        view = PostsDetail.as_view()

        data = {
            "title":"Updated Title",
            "author":1,
            "body": "Updated Body",
        }

        url = reverse('posts_detail', args=[1])
        request = factory.put(url, data)
        force_authenticate(request, user=user)
        response = view(request,pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, data['title'])


    def test_delete(self):
        """Test the api can delete a post."""

        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='tester')
        view = PostsDetail.as_view()

        url = reverse('posts_detail', kwargs={'pk': 1})

        request = factory.delete(url)
        
        force_authenticate(request, user=user)
        response = view(request,pk=1)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)

    def test_delete_bad_user(self):
        """Test the api can delete a post."""

        factory = APIRequestFactory()
        user = get_user_model().objects.create_user(username="faker", password="pass")
        user.save()
        view = PostsDetail.as_view()

        url = reverse('posts_detail', kwargs={'pk': 1}) # alternate way of constructing url

        request = factory.delete(url)
        
        force_authenticate(request, user=user)
        response = view(request,pk=1)

        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)