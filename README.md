# snake_game
A repository containing code mimicking the classic Snake game in Python for memories' sake. The configuration variables for the game are stored in the module `config.py` and can be changed accordingly to increase/reduce the difficulty of the game.

## Requirements
Nothing beyond the `turtle` module that comes with default `Python` installation. The `Python` version used for this project is `3.9.5`. So create a virtual environment using your favourite tool, install the corresponding `Python` version and play away! For those that are developing on WSL and do not have X-Server set up, you can refer to this [guide](https://techcommunity.microsoft.com/t5/windows-dev-appconsult/running-wsl-gui-apps-on-windows-10/ba-p/1493242).

## Features
There are some slight variants to how I remember this game. In this implementation, I choose to go with the following:

### Wall Collision
The game ends upon snake's collision with the wall. It is possible in other implementations that the snake can pass through the wall and appear on the opposite side. Unfortunately this feature is **NOT** implemented here.

### Varying Speed
The snake's speed increases everytime it consumes `config_FOOD_PER_LEVEL` of food. The degree of change can be increased by reducing `config.SPEED_FACTOR`, or vice versa.

### Changing Playing Area
The size of the playing area can be increased/reduced by changing `config.HEIGHT` and `config.WIDTH` accordingly. A smaller playing area puts a higher demand on player's reflexes and skills. It also imposes a theoretical upper limit on the maximum possible score.