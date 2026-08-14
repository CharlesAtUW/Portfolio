# Game AI System

This class project implments various algorithms of game AI on multiple levels of abstraction. Lower-level algorithms include position/rotation matching and chasing. The project is architectured so that higher-level algorithms, such as behavior trees and goal-oriented action planning (GOAP), are built on top of the lower-level algorithms.

- January - April 2026
- C++, OpenFrameworks

<img width="480" height="359" alt="Water plants task" src="https://raw.githubusercontent.com/CharlesAtUW/Portfolio/refs/heads/main/GameAISystem/GameAISystem_GoalPlanning.png" />

## Where to Play

A Windows executable build of the main project can be downloaded [here](https://drive.google.com/file/d/1jodEVyus3iFJvlH2MSm6qWUqc0K2AXKt/view?usp=drive_link).

Controls:
- 1-8: Go to different scenes.
  - Each scene will display its different controls near the top-left of the screen.
  - The program will start at scene 1 (Decision Tree). Note that the order of the scenes isn't the same as the order that things were implementated.
- Escape: Exit game

Decision-making scene details:
- "Decision Tree" scene: the entity will wander randomly around a room, unless it detects the target nearby, which it will pathfind towards. After reaching the target it will "eat" the target, and then rest for a moment.
- "Behavior Tree" scene: the enemy (red) entity will patrol between a set of patrol points, unless it detects the player nearby. In that case, it will pathfind towards its last known location of the player. If it doesn't actively detect the player for some time, it will "lose" the player and go back to patrolling.
- "Goal Planning" scene: The player can set a goal to follow (either pulling the lever or defeating the enemy), and it will automatically pathfind to the relevant items. The enemy (red) entity operates the same as in the "Behavior Tree" scene, except it will try to flee if they detect the player when they have the powerup.

<br/>

A Windows executable build of the graph search performance-testing part of the project (which compares different A* heuristics) can be downloaded [here](https://drive.google.com/file/d/1lo3kjnfg1SzlwzSszwzClnml7ae07BD5/view?usp=drive_link). Note that these tests will take some time to complete.

## Contributions

- Architectured a game AI system with multiple layers of abstraction, along with a simple game object system to more easily populate scenes. Used OpenFrameworks as the base of the program.
- Implemented several position-matching and rotation-matching algorithms (where entities move and rotate towards a target) as the first layer of the game AI.
  - "Seeking", where the entity will move at full speed towards the target position/rotation.
  - "Arriving", where the entity will slow down to stop at the target.
  - Kinematic versions of seek/arrive directly change position and orientation, while dynamic versions change the linear velocity and rotational velocity.
  - Wandering, where the entity chooses random nearby positions in front of it (i.e., no sudden turnarounds) to move towards and face.
  - Flocking, where entities will try to move in a "flock" and avoid being too close or too far from each other.
    - Wandering and flocking build on top of seeking and arriving.
- Implemented different forms of pathfinding as the second layer, building on top of movement.
  - Experimented with Dijkstra's algorithm and different A* search heuristics (Euclidean distance, Manhattan distance, custom mixes of both) to test how quickly they find paths, and how optimal the paths are.
  - Used this pathfinding to let an entity navigate a room while avoiding walls and obstacles.
- Implemented different decision-making algorithms as the third layer, building on top of pathfinding.
  - Decision Tree, Behavior Tree, Goal-Oriented Action Planning (GOAP) 
  - Designed a Blackboard data structure (inspired by Unreal Engine's Blackboard) that lets Decision/Behavior Tree nodes to communicate with each other and with other game elements, without them needing to know directly about each other. 

This was a solo project.