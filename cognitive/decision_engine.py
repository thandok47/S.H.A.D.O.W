#Routes tasks
from cognitive.logger import Logger
import json

with open("cognitive/playbooks.json") as f:
	playbooks = json.load(f)

# Rules to enforce policies

for rule in playbooks["rules"]:
	print(f"Policy for {rule['task_type']}: {rule['policy']}")

class DecisionEngine:
	def __init__(self):
		self.routes = {
			"cipher": "operational.cipher_hook",
			"lumos": "operational.lumos_hook",
			"ignis": "operational.ignis_hook",
		}
	def route_task(self, task_type, payload):
		if task_type in self.routes:
			#Placeholder for actual routing logic
			print(f"Routing {task_type} task with payload: {payload}")
		else:
			print("Unkown task type")

