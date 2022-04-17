# 8puzzle
NYU Tandon's CS-UY 4613 Intro to Artificial Intelligence.   
**Project 1**: the 8 puzzle game.  

## Description
This program uses A-star search on the classic 8-puzzle game to find a solution. We programmed this project using Python due to it's syntactical simplicity.

You pass in a document with the initial and goal states and it returns the shallowest depth, total number of nodes generated, the sequence of moves, and the f(n) values for each node in the solution tree.   

A big topic of discussion was how to dequeue when we get the same f(n) values. We decided to dequeue the most recent node first because the best case is that it was at a deeper depth, giving it a lower h(n) value. This would indicate that it's closer to the goal node. The worst case is that it's just a sister node, which is at the same depth, so, it's not a big sacrifice. 


## Resources Used
We had to look at Python documentation a whole lot, and occasionally email the professor, but no other outside resources were used.

We also used the slides on A-star search and the textbook.

We had a lot of questions about implementing Nilsson Sequence Score, so we spoke to the professor about that. He told us that we skip the blank tile when going clockwise and count the centre tile of the goal node. We account for this by stating that the successor of the centre tile is itself. 


## Running the Project
It is recommended that you use a computer running Linux or macOS to run this code. Also ensure that the computer has a clean copy of `Python >3.8` installed. This project has been tested with all releases of Python till the latest one, `Python 3.10`.   

This code has been tested on Ubuntu, Arch, and macOS.   

Keep in mind that you need to have Python installed.   

You need to invoke this file from the terminal using two command line parameters:   
1. Path to input file   
2. Heuristic: 1 for Manhattan distance or 2 for Nilsson's Sequence score.
```bash
python3 puzzle8.py path/to/input/file.txt heuristic
```
For example, if you wanted to call this file on `Input1.txt` with Manhattan distance, and both files were in the same directory, you would invoke:
```bash
python3 puzzle8.py Input1.txt 1
```
If either argument is ignored, the file will throw an error.

## Files Submitted
As stated above, this project has been categorised into multiple module files that add layers of abstraction to better keep track of what is going on.
| File | Purpose |
|:----:|---|
|board.py|Holds the entire Board and Node modules, including the heuristic functions.It also contains an equality operator definition to compare nodes.|
|algorithm.py|The algorithm code. Holds the A* search algorithm, node expansion, and priority queue handling|
|puzzle8.py|The main file that you should run. This takes the path of the input file as an input and returns the final output as a file.|


## Miscellaneous
Everything has been commented in [Google Docstings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).   

There are additional comments in the files to explain the obscure blocks of code, to help grade.   

Overall, this project was quite interesting to finish. We had fun.  

## Authors
Juan Jose Castano Moreno   
jc10536@nyu.edu   
[@juanjomoreno11](https://github.com/juanjomoreno11)   

Rishyak Panchal   
rishyak@nyu.edu   
[@rishyak](https://github.com/rishyak)   
