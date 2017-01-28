from polls.models import Question, Choice

DATA = """
#What is your preferred colour" | Blue | Red | Yellow | other
#Do you like Django? | Yes | No | Not yet decided
#Do you like ExtJS? | Yes | No | Not yet decided
#Which was first? | chicken | Egg | Turkey
"""

def objects():
	for ln in DATA.splitlines():
		if ln:
			a = ln.split('|')
			q = Question(question_text=a[0].strip())
			yield q
			for choice in a[1:]:
				yield Choice(choice_text=choice.strip(), question=q)

"""
def objects():
	p = Question(question_text="What is your preferred colour?")
	yield p
	yield Choice(choice_text="Blue", question=p)
	yield Choice(choice_text="Red", question=p)
	yield Choice(choice_text="Yellow", question=p)
	yield Choice(choice_text="other", question=p)
	
	p = Question(question_text="Do you like Django?")
	yield p
	yield Choice(choice_text="yes", question=p)
	yield Choice(choice_text="No", question=p)
	yield Choice(choice_text="Not yet decided", question=p)

	p = Question(question_text="Do you like ExtJS?")
	yield p
	yield Choice(choice_text="Yes", question=p)
	yield Choice(choice_text="No", question=p)
	yield Choice(choice_text="Not yet decided.", question=p)
"""


# The code below is more easily maintained, and does the same thing.

# Just comment out the above code if you\'d like to use the code below.


