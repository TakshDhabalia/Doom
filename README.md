# Title: Advanced Python Mini Project Proposal: Developing an Interactive Doom-like Game with NPCs using Pygame

Abstract:
The aim of this project is to develop an interactive and engaging video game reminiscent of the classic Doom, integrating non-player characters (NPCs) within the game environment. This project will be implemented in Python using the Pygame library, leveraging its powerful features for graphics and game development. While incorporating concepts from existing tutorials and resources, this project will emphasize creativity, problem-solving, and a deep understanding of game mechanics to deliver a polished and entertaining gaming experience. All this sounds very fancy but its basically cause funny lmao.

Introduction:
The gaming industry continues to thrive, with an ever-growing demand for immersive and captivating gameplay experiences. Inspired by the iconic Doom series, this project seeks to create a Python-based game that combines fast-paced action with dynamic NPC interactions. By leveraging the Pygame library, we aim to harness its extensive capabilities in graphics rendering, event handling, and sound management to bring our game concept to life.

## Table of Contents
- [Title: Advanced Python Mini Project Proposal: Developing an Interactive Doom-like Game with NPCs using Pygame](#title-advanced-python-mini-project-proposal-developing-an-interactive-doom-like-game-with-npcs-using-pygame)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [System Diagram](#system-diagram)
  - [Modules](#modules)
  - [Installation](#installation)

---

## Project Overview

This project aims to bring the classic **DOOM** game experience to Python through efficient use of raycasting, object-oriented programming, and custom-designed algorithms. With a modular structure, it handles various aspects of the game such as player controls, non-player character (NPC) interactions, object management, and sound effects. 

The project is designed for educational purposes, allowing developers to explore how classic 3D game mechanics are simulated using 2D grids and raycasting techniques.

## System Diagram

Below is a high-level diagram showing how the system components interact with each other:

![System Diagram](./images/system_diagram.png)

This diagram highlights the main files and modules interacting in the system, such as **Player.py**, **Map.py**, **Npc.py**, and **Raycasting.py**, working together to simulate the game’s core mechanics.

---

## Modules

Here is an overview of the primary modules used in this project:

- **Main.py**: The entry point of the game, responsible for initializing the game, starting the game loop, and managing the overall state.
- **Map.py**: Manages the layout and rendering of the game world, including the design of the map and obstacles.
- **Npc.py**: Handles non-player characters (NPCs), including their movements and interactions with the player.
- **Player.py**: Contains the logic for player controls, including movement, shooting, and interacting with the environment.
- **Raycasting.py**: Implements raycasting to render walls and objects from a first-person perspective.
- **Obj_handler.py**: Manages in-game objects, handling their placement, interaction, and removal as necessary.
- **Wepon.py**: Implements the weapons system, allowing the player to fire at enemies and interact with objects.
- **Settings.py**: Contains game settings like resolution, audio levels, and difficulty options.
- **Sound.py**: Manages sound effects, background music, and dynamic audio based on in-game events.
- **PS4_keys.py**: Adds support for PS4 controllers to enhance the gameplay experience on consoles.
- **Actor.py**: Manages actors in the game, including the player and NPCs.
  
Each module is designed to handle a specific aspect of the game, ensuring that the codebase is modular, scalable, and easy to manage.

---

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/doom-python.git
   
2. You may need to do several pip installations but I am too lazy to create a req.txt file for this so yea .

