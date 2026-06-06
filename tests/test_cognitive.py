import unitest
from cognitive.decision_engine import DecisionEngine

class TestDecisionEngine(unittest.TestCase):
	def test_cipher_route(self):
		engine = DecisionEngine()
		results = engine.route_task("cipher", {"action": "test"})
		self.assertIsNone(result)
