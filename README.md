# Welcome to Connect-Five!

Before we get started you may wish to read **_[this](https://www.researchgate.net/publication/2252447_Go-Moku_and_Threat_Space_Search "(PDF) Go-Moku and Threat-Space Search")_** article about what ~~I'm~~ we're trying to do.

## Getting Started

After cloning and connecting to your own device, you might be thinking: *This repository is an absolute mess!*
To which I say: *you are absolutely correct!*
After all, so far this is only the beginning of ~~my~~ our work consisting of a hodgepodge of code, most of which are ~~useless~~ for testing purposes only!
There are no dependencies whatsoever (for now) for this project, so a vanilla `python3` environment should be all you need.

## Project Structure (Draft)

- [x] ~~Steal from CSC180~~ `From Guerzhoy.Assignments import gomoku` to get a basic structure of the game
- [x] Implement `get_threats.py` to examine the board and categorize squares (still needs testing). &rarr A starting point for `threat_space_search.py`
- [ ] Implment `threat_space_search.py` to perform search using `get_threats` to win the game (under progress). ~~_and that's it!_~~
- [ ] Cache `threat_space_search` results into a dictionary for performance.
- [ ] Get this project onto a server and create a front end web app.

### Here are some stuff you can do immediately

- Run `main.py`, and play a game of gomoku with a deprecated AI that has most of its components hiding inside the `./deprecated` folder.
- Go to `get_threats_tests.py` to learn of the only (sort of) functioning feature that this project currently has.
- Go to `./deprecated/advanced_util.py` and find the only useful (and working) function of a threat space searching prototype `def forced_play` that the deprecated AI is using.

## To infinity and beyond!

Once you've familiarized yourself with my pariah of a project you can now decide to do one of three things.
1. Ackgh! This project is going nowhere, I'm better off doing something else. (and that's fine)
2. Hmm... I'm in on the idea, but I'll rewrite the entire framework because the existing code sucks. (...)
3. Cool! I'll create a new branch and work on `threat_space_search`. (Sounds great! * *hint hint* *)
