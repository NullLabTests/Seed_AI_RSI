import time
from main import SeedAI

class Logger:
    def __init__(self, ai):
        self.ai = ai
        self.log_file = open("logs/ai_progress.log", "w")

    def log_progress(self):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_entry = f"{timestamp} - Awareness Level: {self.ai.awareness_level}, RSI Iterations: {self.ai.rsi_iterations}, Consciousness: {self.ai.check_consciousness()}, Memory: {self.ai.reflect_on_memory()}, Self-Assessment: {self.ai.self_assess()}\n"
        self.log_file.write(log_entry)
        self.log_file.flush()

    def close(self):
        self.log_file.close()

if __name__ == "__main__":
    ai = SeedAI()
    logger = Logger(ai)
    while True:
        data = input("Enter data to process: ")
        ai.process_data(data)
        logger.log_progress()
        time.sleep(1)
