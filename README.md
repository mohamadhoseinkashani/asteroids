# Asteroids

A classic Asteroids arcade game built in Python with Pygame — pilot a ship, shoot asteroids, and don't get hit. Large asteroids split into smaller ones when shot.

Built as part of the [Boot.dev](https://www.boot.dev) OOP / "Build Asteroids using OOP" course to practice object-oriented design in a real, playable project.

<!-- Add a screenshot or GIF here — this is the #1 thing that makes this repo stand out -->
<!-- ![Gameplay](docs/gameplay.gif) -->

## How to play

| Key | Action |
|-----|--------|
| W / ↑ | Thrust forward |
| S / ↓ | Reverse |
| A / ← | Rotate left |
| D / → | Rotate right |
| Space | Shoot |

Colliding with an asteroid ends the game.

## Running it locally

**Prerequisites:** Python 3.13+ (see `.python-version`) and [uv](https://docs.astral.sh/uv/)

```bash
# Install dependencies
uv sync

# Start the game
uv run main.py
```

## Project structure

```
.
├── main.py            # Game loop, collisions, entry point
├── player.py          # Player ship (movement, rotation, shooting)
├── shot.py            # Projectiles fired by the player
├── asteroid.py        # Single asteroid behaviour & splitting
├── asteroidsfield.py  # Spawns asteroids over time
├── shaping.py         # Base shape / circle collision helpers
├── constants.py       # Screen size, speeds, radii, etc.
├── logger.py          # Debug / event logging
└── pyproject.toml
```

The design leans on OOP: game entities share a common shape base, update/draw themselves each frame, and the main loop stays focused on orchestration and collisions.

## What I learned

- Object-oriented programming in Python (inheritance, encapsulation, polymorphism via game entities)
- Game loops, delta time, and vector movement
- Circle collision detection
- Structuring a Python project with `uv`

## Next improvements

- [ ] Add gameplay GIF to this README
- [ ] Score counter & lives system
- [ ] Screen wrapping for the player ship
- [ ] Sound effects

---
Made by Hossein Kashani
