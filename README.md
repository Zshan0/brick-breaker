# brick-breaker
A terminal based game inspired from the classic brick breaker built on python from scratch.

## How to Play

### Installation
```zsh
pip3 install -r requirements.txt
```
### Starting the game
```zsh
cd src
python3 main.py
```
This will start the game and print the screen.

## General Instructions

- The game starts in the paused phase. To generate the level press 1
- This will start the game where you can move the paddle and press `space` to launch the ball.
- Hitting bricks will drop powerups which can be picked up by getting them on the paddle.
- The player has 3 lives, each which is lost when all the balls are lost
- Score is calculated based on the bricks that have been destroyed
- You can pause the game at any point with `q` After which you can choose the options from the menu.

### Bricks
There are 4 types of bricks
- first correspond to normal ones with 3 levels of health
- The unbreakable bricks which can't be broken until `through ball` powerup is available or through the explosive bricks.
- Explosive bricks are the ones which occur 10 in a row and will destroy all the blocks around them.

### Powerups
There are 6 powerups, all of them last 10 seconds. Ball multiplier does not expire.
- Through ball: Ball passes through all the bricks
- Shrink paddle: Shrinks the paddle once by a fixed amount
- Ball multiplier: Doubles the number of balls that are present
- Fast ball: doubles the speed in both vertical and horizontal direction
- Thru ball: Balls are able to pass through all the bricks
- Paddle grab: When the ball hits the paddle, it is held onto till the player decides to release it again.
