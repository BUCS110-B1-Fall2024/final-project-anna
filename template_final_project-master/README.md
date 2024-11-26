
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Frog run
## CS110 B1 Final Project Fall, 2024

## Team Members

Anna Lei

***

## Project Description

The player would be a frog and they would have to jump over obstacles but they would also have to collect lily pads and it would give them points. When the player reaches a certain amount of point, they win the game. If they hit an obstacle, it would be game over.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. moveable character
2. obstacles
3. points/rewards system
4. moving background
5. game over screen

### Classes

- Frog: Creates a frog that can jump with the influence of gravity. It's a 2D frog that starts at the x, y position and when the frog jumps, the position will be updated based on gravity.
- Obstacle: Creates the obstacles in the game which are spikes that can detect when the frog collides with the obstacle.
- Points: Creates a lily pad that the frog can collect and give the player points and contribute to the score. This class handles the positioning, collision detection, and collection status of the lily pads.

## ATP
Player movement
Verify that the player can jump and the player will fall back to the ground due to gravity. 
| Step                 |Procedure                    |Expected Results                                               |
|----------------------|:---------------------------:|--------------------------------------------------------------:|
|  1                   | Start the game              | Player's frog should jump up and fall back down to the ground |
|  2                   | Press the space bar         |                                                               |
|  3                   | Verify that the player jumps|                                                               |
Collision Detection
Verify that the obstacle and point objects work and when the player collides with it, it will either end the game or give them a point.
| Step                 |Procedure                                 |Expected Results                                                       |
|----------------------|:----------------------------------------:|----------------------------------------------------------------------:|
|  1                   | Start the game                           | Player should collide with obstacle object and point object correctly.|
|  2                   | Don't jump over a spike obstacle         | If player collides with an obstacle, game over screen should display. |
|  3                   | Verify the player ran into the obstacle  | If player collides with a lily pad, player should earn a point.       |
|  4                   | Jump into a lily pad (point object)      |                                                                       |
|  5                   | Verify the player ran into the lily pad  |                                                                       |
Game over screen
Verify that the game over screen would display when player collides with an obstacle.
| Step                 |Procedure                                  |Expected Results                                                       |
|----------------------|:-----------------------------------------:|----------------------------------------------------------------------:|
|  1                   | Start the game                            | Game over screen should display when player collides with an obstacle.|
|  2                   | Play until player hits an obstacle.       | There should be a try again button to allow players to play again.    |
|  3                   | Verify the "Game over" screen will display|                                                                       |
Winner screen
Verify that when player reaches 10 points, it will display a winner screen.
| Step                 |Procedure                                  |Expected Results                                                       |
|----------------------|:-----------------------------------------:|----------------------------------------------------------------------:|
|  1                   | Start the game                            | Winner screen should display when player collects 10 points.          |
|  2                   | Play until player collects 10 points.     |                                                                       |
|  3                   | Verify the "Winner" screen will display   |                                                                       |