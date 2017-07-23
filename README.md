![](/images/logos/logo_white.jpg?raw=True "Alien Invasion")
# Alien Invasion

In Alien Invasion, the player controls a shit that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys aliens. If the player shoots all the aliens a new fleet appears that moves faster than the previous fleet. If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends. After the game ends the users score is saved to the file [scores.json](https://github.com/domdew23/Alien-Invasion/blob/master/data_files/scores.json). The top 10 scores are displayed once the game is over. The user then has the option to play again or could close out the window to stop playing. Once the user reopens the program all the previous high scores will be retained. The user has the option to clear all previous saved scores by running [clear_scores.py](https://github.com/domdew23/Alien-Invasion/blob/master/program_files/clear_scores.py) while in the [program_files](https://github.com/domdew23/Alien-Invasion/tree/master/program_files) directory. 

## Getting Started

To play Alien Invasion download the repository and navigate to the [program_files](https://github.com/domdew23/Alien-Invasion/tree/master/program_files) directory. From there run the command from the command line 'python [alien_invasion.py](https://github.com/domdew23/Alien-Invasion/blob/master/program_files/alien_invasion.py)'. Press play and the game will begin.

### Prerequisites

To run this game you must have Python 3.x installed and pygame installed. [Click Here to download Python](https://www.python.org).

#### - Installing Pygame on Linux 

* $ sudo apt-get install python-pygame

#### - Installing Pygame on OS X

##### - Install Homebrew

* $ xcode-select --install
* $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
* $ brew doctor

* $ brew install hg sdl sdl_image sdl_ttf
* $ pip3 install --user hg+http://bitbucket.org/pygame/pygame

#### - Installing Pygame on Windows

[Click Here to install Pygame for Windows](https://bitbucket.org/pygame/pygame/downloads/). Then choose the version of python you are running. You can check this by typing 'python -m pip --version'.

## Built With
* [Python](https://www.python.org/) - The functionality of the game
* [Pygame](https://www.pygame.org/news) - Used to display graphics and implement user interaction

## Author

* **Dominic Dewhurst**

## Links
* [Linkedin](https://www.linkedin.com/in/dominic-dewhurst-b1a971129)
* [Youtube](https://www.youtube.com/channel/UCPrj3XZlY39YiaHc6yaodLg)

## Acknowledgments

This project was based of the work done in the book [Python Crash Course: A Hands-On, Project-Based Introduction to Programming by Eric Matthes](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1499567328&sr=8-1&keywords=python+crash+course).
