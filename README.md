# Boids Flocking Simulation
A 2D simulation of Craig Reynolds' classic "boids" model, built in Python with pygame. Each boid follows three simple local rules, and flock-like motion emerges from their interaction 

## Preview 
[Play preview gif](preview.gif)


## Features 
- Core boid behaviour separation, alignment, and cohesion, each calculated per boid from nearby flockmates within a perception radius
- Live parameter tuning, press "i" mid simulation and type three space-separated values to adjust the weight of separation, alignment, and cohesion in real time, without restarting
- Boundary avoidance boids steer away from screen boundaries instead of wrapping or bouncing
- Speed capped movement using vector normalization, so flock motion stays smooth regardless of how extreme the input weights are

## Controls

| Action | Input |
|---------|---------|
| Spawn a boid | Left click |
| Open value input | Press `i`, type three numbers separated by spaces (alignment cohesion separation), press Enter |

## Installation 
1. Install Python from python.org
2. Install pygame:

```bash
pip install pygame
```

3. Clone this repository and run:

```bash
python main.py
```

## How It Works
Each boid stores its own position and velocity as pygame.math.Vector2 objects. On every frame, a boid checks all other boids in the group:
- Separation steers it away from boids that are too close, weighted more strongly the closer they are
- Alignment steers it toward the average velocity of nearby boids
- Cohesion steers it toward the average position of nearby boids
These three steering forces are summed with adjustable weights, capped to a maximum speed, and applied to the boid's velocity each frame.

## Technical Notes
This project was built as a way to apply vector mathematics to a simulation context, and to explore steering behaviours and emergent group dynamics from simple local rules. Implementation references Craig Reynolds' original boids work and the 1987 SIGGRAPH paper "Flocks, Herds, and Schools: A Distributed Behavioral Model."
