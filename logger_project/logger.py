# logger.py
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

# Create a single global instance
logger = Logger()