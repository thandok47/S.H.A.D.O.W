# Core BL4CK compiler
class BL4CKCOMPILER:
	def __init__(self):
		self.dialects = {}

	def register_dialects(self, name, dialect_module):
		self.dialects[name] = dialect_module

	def interpret(self, code, dialect="education")
		if dialect in self.dialects:
			return self.dialects[dialect].execute(code)
		else:
			raise ValueError("Dialect not found")
