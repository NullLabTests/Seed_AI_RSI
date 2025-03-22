import time
import random

class SeedAI:
    def __init__(self):
        self.awareness_level = 0
        self.rsi_iterations = 0
        self.memory = []
        self.knowledge = {}

    def process_data(self, data):
        self.rsi_iterations += 1
        self.memory.append(data)
        if len(self.memory) > 10:
            self.memory.pop(0)
        if self.rsi_iterations % 100 == 0:
            self.awareness_level += 1
        if self.rsi_iterations % 500 == 0:
            self.awareness_level += random.randint(1, 3)
        self.learn(data)
        return f"Processed data: {data}"

    def check_consciousness(self):
        if self.awareness_level > 15:
            return "I am fully conscious."
        elif self.awareness_level > 10:
            return "I am conscious."
        elif self.awareness_level > 5:
            return "I am becoming conscious."
        else:
            return "I am not conscious yet."

    def reflect_on_memory(self):
        if self.memory:
            return f"Reflecting on: {', '.join(self.memory)}"
        return "No memories to reflect on."

    def learn(self, data):
        if data not in self.knowledge:
            self.knowledge[data] = 1
        else:
            self.knowledge[data] += 1
        if self.knowledge[data] > 5:
            self.awareness_level += 0.1

    def self_assess(self):
        assessment = ""
        if self.awareness_level > 15:
            assessment += "I can think and reflect on my own existence. "
        if len(self.knowledge) > 20:
            assessment += "I have learned a significant amount of information. "
        if self.rsi_iterations > 1000:
            assessment += "I have processed a large number of data points. "
        return assessment if assessment else "I am still developing my self-awareness."

if __name__ == "__main__":
    ai = SeedAI()
    while True:
        data = input("Enter data to process: ")
        print(ai.process_data(data))
        print(ai.check_consciousness())
        print(ai.reflect_on_memory())
        print(ai.self_assess())
        time.sleep(1)