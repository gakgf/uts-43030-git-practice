import unittest
from todo import Task, TaskPool

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("A new task")
        self.pool.add_task(task)
        self.assertEqual(self.pool.tasks, [task])

    def test_get_open_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_open_tasks()), 3)
        self.assertTrue(all(t.status == "ToDo" and not t.completed for t in self.pool.get_open_tasks()))

    def test_get_done_tasks(self):
        self.pool.populate()
        self.assertEqual(len(self.pool.get_done_tasks()), 3)
        self.assertTrue(all(t.status == "Done" and t.completed for t in self.pool.get_done_tasks()))

    def test_mark_completed_moves_task_between_filters(self):
        task = Task("Complete me")
        self.pool.add_task(task)
        task.mark_completed()
        self.assertEqual(self.pool.get_open_tasks(), [])
        self.assertEqual(self.pool.get_done_tasks(), [task])

    def test_initial_done_status_is_consistent(self):
        task = Task("Already completed", status="Done")
        self.pool.add_task(task)
        self.assertTrue(task.completed)
        self.assertEqual(self.pool.get_done_tasks(), [task])
        self.assertEqual(self.pool.get_open_tasks(), [])

    def test_task_representation(self):
        task = Task("Example")
        self.assertEqual(repr(task), "Example - ToDo")
        self.assertEqual(str(task), "Task: Example, Status: ToDo")

if __name__ == "__main__":
    unittest.main(verbosity=2)
