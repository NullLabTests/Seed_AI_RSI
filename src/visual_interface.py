import pygame
import time
from main import SeedAI
from logging import Logger

pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seed AI Consciousness Level")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

# Initialize Seed AI and Logger
ai = SeedAI()
logger = Logger(ai)

running = True
clock = pygame.time.Clock()
input_text = ''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text.startswith("set goal:"):
                    parts = input_text.split(":")
                    if len(parts) > 2:
                        goal = parts[1].strip()
                        level = int(parts[2].strip())
                        ai.set_goal(goal, level)
                    else:
                        ai.set_goal(parts[1].strip())
                elif input_text.startswith("decision:"):
                    parts = input_text.split(":")
                    if len(parts) > 2:
                        decision = parts[1].strip()
                        outcome = parts[2].strip()
                        ai.make_decision(decision, outcome)
                else:
                    ai.process_data(input_text)
                logger.log_progress()
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    screen.fill(WHITE)

    # Draw consciousness level bar
    bar_height = int((ai.awareness_level / 20) * HEIGHT)
    pygame.draw.rect(screen, BLUE, (WIDTH - 50, HEIGHT - bar_height, 50, bar_height))

    # Draw text
    consciousness_text = font.render(ai.check_consciousness(), True, BLACK)
    screen.blit(consciousness_text, (10, 10))

    memory_text = font.render(ai.reflect_on_memory(), True, BLACK)
    screen.blit(memory_text, (10, 50))

    self_assess_text = font.render(ai.self_assess(), True, BLACK)
    screen.blit(self_assess_text, (10, 90))

    # Draw RSI iterations
    rsi_text = font.render(f"RSI Iterations: {ai.rsi_iterations}", True, BLACK)
    screen.blit(rsi_text, (10, 130))

    # Draw knowledge count
    knowledge_text = font.render(f"Knowledge Items: {len(ai.knowledge)}", True, BLACK)
    screen.blit(knowledge_text, (10, 170))

    # Draw input field
    input_field = font.render(f"Input: {input_text}", True, BLACK)
    screen.blit(input_field, (10, 210))

    # Draw learning progress
    learning_progress = font.render(f"Learning Accuracy: {ai.performance_metrics['accuracy']:.2f}", True, BLACK)
    screen.blit(learning_progress, (10, 250))

    learning_speed = font.render(f"Learning Speed: {ai.performance_metrics['learning_speed']:.4f}", True, BLACK)
    screen.blit(learning_speed, (10, 290))

    # Draw goals
    if ai.goals:
        goals_text = font.render("Goals:", True, BLACK)
        screen.blit(goals_text, (10, 330))
        for i, goal in enumerate(ai.goals):
            goal_text = font.render(f"{goal['goal']} (Level {goal['level']}): {goal['progress']:.2f}", True, BLACK)
            screen.blit(goal_text, (20, 370 + i * 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
logger.close()