# Udon Uncaged

In this alt-control game, control Udon the hamster by rolling around in the giant hamster ball! Traverse and escape the room!

- January - April 2025
- Unity, C#

[![Trailer](https://img.youtube.com/vi/hEAv1nY5gTM/0.jpg)](https://youtu.be/hEAv1nY5gTM) <img width="480" height="270" alt="Controller" src="https://github.com/user-attachments/assets/3481c208-7efe-4c95-a81a-22a7a6768d93" />

## Where to play

This game is playable at GDC 2026, at the "alt.ctrl.GDC" area, in the expo hall.

## Contributions
- I did the bulk of the programming for this game, including but not limited to:
  - Created a modular event trigger system, that allows events to be chained together without them directly knowing about each other. Used mainly for transitioning between different parts of the level.
  - Created an "Object on Spline" system, where objects' positions and rotations can be constrained to a spline, while still being able to respond to physics.
  - Created a fan that can blow the player away. The fan's force becomes weaker as you get farther away, or if you're partially behind cover.
  - Programmed an Arduino to respond to the ball rolling on the treadmill, as input for the game. Used Ardity to connect the Arduino to Unity.
- Worked closely with the game's designers to ensure that my work aligned with the game's design vision.

This project was a collaborative effort. The team size was 14 members.