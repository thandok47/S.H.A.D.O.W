# Logging + audit
import logging
import os

# Ensure logs directory exists
if not os.path.exists("logs"):
	os.makedirs("logs")

logging.basicConfig(
	filename="logs/shadow.log", 
	level=logging.INFO,
	format="%(asctime)s [%(levelname)s] %(message)s"
)

class Logger:
	def log_info(self, message):
		logging.info(message)
		print(f"[INFO] {message}")

	def log_error(self, message):
		logging.error(message)
		print(f"[ERROR] {message}")

	def log_audit(self, action, user="system"):
		logging.info(f"AUDIT: {user} performed {action}")
