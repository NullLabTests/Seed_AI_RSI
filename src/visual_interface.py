import pygame
import time
from main import SeedAI

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

# Initialize Seed AI
ai = SeedAI()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                data = input("Enter data to process: ")
                ai.process_data(data)

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

    pygame.display.flip()
    clock.tick(60)

pygame.quit()