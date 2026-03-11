# Fading Expressions

![Water plants task](https://img.itch.zone/aW1hZ2UvMzAxNTAxNC8xODAzMTUwNy5wbmc=/original/rfuY%2B1.png)
![Picture task](https://img.itch.zone/aW1hZ2UvMzAxNTAxNC8xODAzMTUyNS5wbmc=/original/Lf3vNv.png)

A rapid prototype for a serious game, about the daily struggles of those suffering from dementia.

- September 2024
- Unity, C#

## Where to play

Playable now, for free, on the [Itch page](https://zansha.itch.io/fading-expressions).

## Contributions
- Created a task system using Unity's ScriptableObjects, allowing for the same type of task to be easily reused and reconfigured. This game involves doing tasks across different days, and some tasks are reused with slight variations across different days.
  - Implemented many of the tasks, such as inspecting objects, taking a picture, and watering plants.
- Created a modular interactor/interactable system. The interactor (the player) uses abstract interactable objects for its interactions, allowing new interactables to be made without having to modify the interactor class.
  - Implemented many of the interactables, such as waterable plants, a watering can that has to be filled up, and composing multiple interactables under one "multi interact" object (which is also an interactable).
- Managed dialogue using Unity's ScriptableObjects for easy organization and reuse.

This project was a collaborative effort. The core development team was 6 members.