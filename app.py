from cognitive.decision_engine import DecisionEngine
from cognitive.logger import Logger

engine = DecisionEngine()
logger = Logger()

engine.route_task("cipher", {"action": "open_doc"})
logger.log_audit("cipher task executed", user="tester")
