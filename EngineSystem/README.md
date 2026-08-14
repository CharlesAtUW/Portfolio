# Engine System

This class project implements significant parts of a game engine. It takes a deep dive game engine architecture, 3D rendering, file formats, and platform dependent/independent code. Includes a camera system with several different modes of position and rotation tracking, inspired by Unity's Cinemachine. The final product is an interactive cutscene, that integrates classmates' sound and animation systems with my camera system.

- August - December 2025
- C++

<img width="480" height="335" alt="Water plants task" src="https://raw.githubusercontent.com/CharlesAtUW/Portfolio/refs/heads/main/EngineSystem/EngineSystem_Cutscene.png" />

## Where to Play

A Windows executable build of the final can be downloaded [here](https://drive.google.com/file/d/1yAHDQ1DazBk2H9wPnmGinWZi8m2M7T25/view?usp=sharing).

Controls:
- Space: Perform quicktime event
  - The quicktime event is indicated by the exclamation mark above the player’s head. Press space during the quicktime event for your player to succeed in the cutscene! The window for the quicktime event is pretty long, so don’t worry about any precise timing.
- R: Restart cutscene
  - Can be done at any point in the cutscene.
- Escape: Exit game

## Contributions
- Organized Visual Studio project/solution structure (for better sepration-of-concerns and compile times)
- Organized the project build pipeline for the project, to build properly in Visual Studio.
  - This includes managing references, dependencies, build order, built-file input/output locations, and property sheets. 
  - Separated platform-dependent implementations (OpenGL, Direct3D) into different .cpp files (while sharing the same .h file), and included/excluded them based on build configuration.
- Architectured a simple ECS (Entity Component System) to make it easier to add objects with various behaviors into the game world.
- Added interpolation to the rendered positions of objects, for their movement to look smoother (since their actual positions only update during physics updates).
- Implemented a simple Maya plugin for exporting meshes to be imported into the game. Created a human-readable, Lua-based file format for these meshes.
  - Created a binary file format for the meshes, that the human-readable files are converted into during the build process.
  - Made different design decisions for each of the formats based on their use cases (e.g. designing the binary file format for performance).
  - The built binary files changes depending on the build setting (OpenGL or Direct3D) for faster file load time (e.g. pre-emptively setting the correct triangle winding order).
- Built a configurable camera system that lets the camera track a target. Different modes for position and rotation control can be mixed-and-matched for various types of cameras.
  - Created detailed documented for this system, allowing for classmates to use this system in their projects.
- For the final project, built an interactive cutscene using several different camera configurations. Integrated classmates' sound and animation systems into my project for a complete cutscene.

Apart from starter code, the animation system, and the sound system, this was a solo project.