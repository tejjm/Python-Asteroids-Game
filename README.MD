Asteroids Game in Python – Pygame
A classic space shooter game built using Python's Pygame library. The player controls a spaceship, avoiding and destroying asteroids that break into smaller pieces when hit. The game showcases collision detection, object splitting, sprite management, and game state handling. Developed to deepen understanding of game development fundamentals.

Features
Controlled spaceship that can rotate left/right, accelerate, and shoot bullets

Moving asteroids of different sizes that split into smaller ones when hit

Bullet objects with lifetime and collision detection with asteroids

Real-time game over and victory conditions

Visual and audio effects for immersion (optional)

How It Works
The spaceship is controlled by arrow keys and spacebar for shooting.

Asteroids spawn and move around the screen, avoiding the player.

Shooting a bullet hits an asteroid, destroying or splitting it based on size.

The game ends when all asteroids are destroyed or when the spaceship collides with one.

The game physics include rotation, acceleration, and collision detection for realistic movement.

How to Run
Install Pygame:

text
pip install pygame
Save the code files into a directory.

Run the main game script:

text
python main.py
Play by navigating the spaceship to avoid or shoot asteroids.

What I Practiced & Learned
Developing a complete arcade-style game with Pygame

Handling sprite movements, rotations, and collision detection

Implementing object splitting and multiple game states

Managing game loop and real-time inputs efficiently

Building a functional, expandable game architecture

File Structure
AsteroidsGame/
├── main.py
├── constants.py
├── player.py
├── asteroid.py
├── shot.py
├── asteroidfield.py
└── README.md
