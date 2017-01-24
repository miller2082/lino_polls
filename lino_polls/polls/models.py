import datetime
from django.utils import timezone
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from lino.api import dd


@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	hidden = models.BooleanField(
		"Hidden",
		help_text="Whether this poll should not be shown in the main window.",
		default=False)

		# Pick up from here

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
