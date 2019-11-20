=====
Task
=====

Task is a simple Django app to conduct Web-based task management. For each
task, visitors can change task status till it's done.
pip

Quick start
-----------

1. Add "task" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'task',
    ]

2. Include the task URLconf in your project urls.py like this::

    path('task/', include('task.urls')),

3. Run `python manage.py migrate` to create the task models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a task (you'll need the Admin app enabled).

5. Let's restart the server and visit this address — http://localhost:8000/api/task

6. we can now perform CRUD operations on the Task model. The router class allows us to make the following queries::

    /task/ - This returns a list of all the Task items (Create and Read operations can be done here).

    /task/id - this returns a single Task item using the id primary key (Update and Delete operations can be done here).