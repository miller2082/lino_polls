BUG_REPORT

PROBLEM:

After writing the fixture in demo.py, running '$ python manage.py initdb demo' an error occurred: 

The fixture worked, but the Question() class threw an error, path below:

Could not load polls.Question(pk=None): table polls_question has no column named hidden

File "/home/jmm/virtualenvs/a/local/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py", line 323, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: 
Problem installing fixture 
'/home/jmm/projects/lino_polls/lino_polls/polls/fixtures/demo.py': 
Could not load polls.Question(pk=None): table polls_question has no column named hidden


SOLUTION:
run:
$ python manage.py makemigrations
$ python manage.py migrate

Then running the following lines worked fine:

$ python manage.py initdb demo

