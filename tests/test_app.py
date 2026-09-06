import unittest

from app import add_task, complete_task, list_tasks, tasks


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        task = add_task("Learn GitHub Agent")
        self.assertEqual(task["title"], "Learn GitHub Agent")
        self.assertFalse(task["completed"])

    def test_list_tasks(self):
        add_task("Task one")
        add_task("Task two")
        self.assertEqual(len(list_tasks()), 2)

    def test_complete_task(self):
        add_task("Finish tutorial")
        completed = complete_task(0)
        self.assertTrue(completed["completed"])

    def test_complete_invalid_task(self):
        with self.assertRaises(IndexError):
            complete_task(0)


if __name__ == "__main__":
    unittest.main()
