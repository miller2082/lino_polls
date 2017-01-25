from lino.api import dd

class Questions(dd.Table):
	model = 'polls.Question'
	sort_order = ['pub_date']

	detail_layout = """
	id question_text
	hidden pubdate
	ChoiceByQuestion
	"""

	insert_layout = """
	question_text
	hidden
	"""

class Choices(dd.Table):
	model = 'polls.Choice'

class ChoiceByQuestion(Choices):
	master_key = 'question'


