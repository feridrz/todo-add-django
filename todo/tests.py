from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo
from datetime import datetime, timedelta


class TodoModelTest(TestCase):
    def setUp(self):
        self.todo = Todo.objects.create(
            title='Test Todo',
            description='This is a test todo'
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.description, 'This is a test todo')
        self.assertFalse(self.todo.completed)

    def test_todo_string_representation(self):
        self.assertEqual(str(self.todo), 'Test Todo')

    def test_todo_ordering(self):
        todo2 = Todo.objects.create(title='Second Todo')
        todos = Todo.objects.all()
        self.assertEqual(todos[0].id, todo2.id)  # Newer first


class TodoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            'title': 'API Test Todo',
            'description': 'Testing the API',
            'completed': False
        }
        self.todo = Todo.objects.create(**self.todo_data)

    def test_list_todos(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        response = self.client.post(reverse('todo-list'), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)

    def test_retrieve_todo(self):
        response = self.client.get(reverse('todo-detail', args=[self.todo.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo.title)

    def test_update_todo(self):
        updated_data = {'title': 'Updated Todo', 'completed': True}
        response = self.client.patch(
            reverse('todo-detail', args=[self.todo.id]),
            updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Todo')
        self.assertTrue(self.todo.completed)

    def test_delete_todo(self):
        response = self.client.delete(reverse('todo-detail', args=[self.todo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)

    def test_completed_todos_filter(self):
        Todo.objects.create(title='Completed Todo', completed=True)
        response = self.client.get(reverse('todo-completed'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_pending_todos_filter(self):
        Todo.objects.create(title='Pending Todo', completed=False)
        response = self.client.get(reverse('todo-pending'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_toggle_completed(self):
        response = self.client.patch(
            reverse('todo-toggle-completed', args=[self.todo.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)

        # Toggle back
        response = self.client.patch(
            reverse('todo-toggle-completed', args=[self.todo.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertFalse(self.todo.completed)
