class Post:
	def __init__(self, title, content):
		self.title = title
		self. content = content
		
	# converts the post to json so that it can return a dictionery representing this post
	def json(self):
		return {
			'title': self.title,
			'content':self.content,
		}