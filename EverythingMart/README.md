# EverythingMart

Cooperate to complete orders in an otherworldly supermarket, where the grocery items you need to collect are walking around! Play with up to four players.

- August 2025 - Present (ongoing, expected August 2026 release)
- Unity, C#, FishNet

<img width="480" height="275" alt="EverythingMart banner" src="https://raw.githubusercontent.com/CharlesAtUW/Portfolio/refs/heads/main/EverythingMart/EverythingMart_Banner.png" />

## Where to play

This project is still in progress. A demo is currently available on the [Steam](https://store.steampowered.com/app/4637430/Everything_Mart/) page. Look out for the Steam release!

## Contributions
- Networked the gameplay features using the FishNet networking library. Connected players together using Unity Relay.
  - Improved player responsiveness of physics using authority transfers for various physics items.
    - Made networking authority of items transfer to the player who collided with it or picked it up.
    - "Ownership priority" system: For example, holding an item has a higher priority than colliding with it, meaning a player cannot take ownership of an item that another player is currently holding.
  - Ensured that features implemented by other engineers were properly synchronized across the network.
- Contributed to many of the gameplay features, including but not limited to:
  - Picking up and throwing items
    - Including charging up for a stronger throw
    - Including the unique physics interactions that come with holding an item
    - "Crosshair correction" for thrown items: Slightly adjust the throwing angle so the throw better matches the crosshair at the center of the screen.
  - Created a shopping cart that you can push around, and tuned its unique movement to create a drifting-like feel. Items can also stick to the inside of the cart.
  - Added a menu for rebinding controls (highlighting duplicate keybinds with a different color).

This project was a collaborative effort. The team size was 14 members.
