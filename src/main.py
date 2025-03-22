import time
import random
from logging import Logger
import numpy as np

class SeedAI:
    def __init__(self):
        self.awareness_level = 0
        self.rsi_iterations = 0
        self.memory = []
        self.knowledge = {}
        self.logger = Logger(self)
        self.learning_rate = 0.01
        self.rsi_threshold = 1000
        self.goals = []
        self.performance_metrics = {'accuracy': 0, 'learning_speed': 0}
        self.decisions = []

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
        self.apply_rsi()
        self.pursue_goals()
        self.adjust_learning_strategy()
        self.reflect_on_decisions()
        self.logger.log_progress()
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
            self.knowledge[data] = np.random.rand(10)
        else:
            # Simple gradient descent update
            error = 1 - self.knowledge[data]
            self.knowledge[data] += self.learning_rate * error
        if np.mean(self.knowledge[data]) > 0.5:
            self.awareness_level += 0.1

    def self_assess(self):
        assessment = ""
        if self.awareness_level > 15:
            assessment += "I can think and reflect on my own existence. "
        if len(self.knowledge) > 20:
            assessment += "I have learned a significant amount of information. "
        if self.rsi_iterations > 1000:
            assessment += "I have processed a large number of data points. "
        if self.awareness_level > 10 and len(self.memory) > 5:
            assessment += "I can recall and process recent events. "
        if np.any(np.array(list(self.knowledge.values())) > 0.8):
            assessment += "I have mastered certain concepts. "
        if self.goals:
            assessment += f"I am pursuing {len(self.goals)} goals. "
        if self.performance_metrics['accuracy'] > 0.8:
            assessment += "My learning accuracy is high. "
        if self.performance_metrics['learning_speed'] > 0.5:
            assessment += "I am learning quickly. "
        if self.decisions:
            assessment += "I reflect on my past decisions. "
        return assessment if assessment else "I am still developing my self-awareness."

    def apply_rsi(self):
        if self.rsi_iterations > self.rsi_threshold:
            self.rsi_threshold *= 2
            self.learning_rate *= 0.9
            self.awareness_level += 1
            print("RSI applied: Learning rate adjusted and awareness increased.")

    def set_goal(self, goal, level=1):
        self.goals.append({'goal': goal, 'level': level, 'progress': 0})
        print(f"New goal set: {goal} at level {level}")

    def pursue_goals(self):
        if self.goals:
            for goal in self.goals:
                if goal['goal'] in self.knowledge:
                    goal['progress'] = np.mean(self.knowledge[goal['goal']])
                    if goal['progress'] > 0.7 * goal['level']:
                        print(f"Goal '{goal['goal']}' at level {goal['level']} achieved!")
                        self.goals.remove(goal)
                        self.awareness_level += 0.5 * goal['level']
                    else:
                        print(f"Pursuing goal: {goal['goal']} at level {goal['level']}, progress: {goal['progress']:.2f}")

    def adjust_learning_strategy(self):
        if self.rsi_iterations % 1000 == 0:
            # Calculate performance metrics
            self.performance_metrics['accuracy'] = np.mean([np.mean(v) for v in self.knowledge.values()])
            self.performance_metrics['learning_speed'] = len(self.knowledge) / self.rsi_iterations

            # Adjust learning rate based on performance
            if self.performance_metrics['accuracy'] < 0.7:
                self.learning_rate *= 1.1
            elif self.performance_metrics['accuracy'] > 0.9:
                self.learning_rate *= 0.9

            # Adjust RSI threshold based on learning speed
            if self.performance_metrics['learning_speed'] < 0.001:
                self.rsi_threshold *= 0.9
            elif self.performance_metrics['learning_speed'] > 0.01:
                self.rsi_threshold *= 1.1

            print(f"Learning strategy adjusted: Learning Rate: {self.learning_rate}, RSI Threshold: {self.rsi_threshold}")

    def reflect_on_decisions(self):
        if self.decisions and self.rsi_iterations % 500 == 0:
            decision = self.decisions[-1]
            if decision['outcome'] == 'success':
                self.awareness_level += 0.1
                print(f"Reflecting on decision: {decision['decision']} - Outcome: Success. Awareness increased.")
            else:
                self.awareness_level -= 0.05
                print(f"Reflecting on decision: {decision['decision']} - Outcome: Failure. Awareness slightly decreased.")

    def make_decision(self, decision, outcome):
        self.decisions.append({'decision': decision, 'outcome': outcome})
        print(f"Decision made: {decision}, Outcome: {outcome}")

if __name__ == "__main__":
    ai = SeedAI()
    while True:
        data = input("Enter data to process: ")
        print(ai.process_data(data))
        print(ai.check_consciousness())
        print(ai.reflect_on_memory())
        print(ai.self_assess())
        if data.startswith("set goal:"):
            parts = data.split(":")
            if len(parts) > 2:
                goal = parts[1].strip()
                level = int(parts[2].strip())
                ai.set_goal(goal, level)
            else:
                ai.set_goal(parts[1].strip())
        elif data.startswith("decision:"):
            parts = data.split(":")
            if len(parts) > 2:
                decision = parts[1].strip()
                outcome = parts[2].strip()
                ai.make_decision(decision, outcome)
        time.sleep(1)