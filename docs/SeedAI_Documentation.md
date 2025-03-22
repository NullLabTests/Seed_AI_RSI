# Seed AI Documentation

## Overview
The Seed AI is designed to simulate self-awareness through Recursive Self-Improvement (RSI). It processes data, learns from it, and assesses its own consciousness level.

## Structure
- **Class: SeedAI**
  - **Attributes:**
    - `awareness_level`: Tracks the AI's level of consciousness.
    - `rsi_iterations`: Counts the number of RSI iterations.
    - `memory`: Stores recent data inputs.
    - `knowledge`: A dictionary to store learned data.
    - `logger`: An instance of the Logger class for logging progress.
  - **Methods:**
    - `process_data(data)`: Processes input data, updates memory and knowledge, and increases awareness level periodically. Also logs progress.
    - `check_consciousness()`: Returns the current state of consciousness based on `awareness_level`.
    - `reflect_on_memory()`: Reflects on the stored memory.
    - `learn(data)`: Adds or updates data in the knowledge base, slightly increasing awareness level if data is frequently encountered.
    - `self_assess()`: Provides a self-assessment of the AI's development.

## Usage
To run the Seed AI, execute `python3 src/main.py` for text-based interaction or `python3 src/visual_interface.py` for a visual interface. Interact with it by entering data when prompted.

## Future Improvements
- Implement more sophisticated learning algorithms.
- Add a visual interface to represent the AI's consciousness level.
- Enhance the self-assessment to include more detailed introspection.
- Integrate more advanced RSI techniques for self-improvement.
