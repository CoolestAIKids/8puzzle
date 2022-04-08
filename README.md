# 8puzzle
NYU Tandon's CS-UY 4613 Intro to Artificial Intelligence Project 1, the 8 puzzle game.  

## Description
Lorem ipsum and state of work.

## Table of Contents
Lorem ipsum

## Running the Project
It is recommended that you use a computer running Linux or macOS to run this code. Also ensure that the computer has a clean copy of `Python >3.8` installed. This project has been tested with all releases of Python till the latest one, `Python 3.10`.   

This code has been tested on Ubuntu, Arch, and macOS.   

Keep in mind that you need to have Python installed.   
```bash
python3 8puzzle.py path/to/input/file.txt
```


## Files Submitted
As stated above, this project has been categorised into multiple module files that add layers of abstraction to better keep track of what is going on.
| File | Purpose |
|:----:|---|
|board.py|Holds the entire Board module, including the heuristic functions.|
|node.py|Holds the node module to help the algorithm. It also contains an equality operator definition to compare nodes.|
|algorithm.py|The algorithm code. Holds the A* search algorithm, node expansion, and priority queue handling|
|8puzzle.py|The main file that you should run. This takes the path of the input file as an input and returns the final output on both, `stdout` and as a file.|


## Nodepad
Everything has been commented in Google Docstings https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings

https://notability.com/n/GYbHSECpBgs~~z~75jyRm

Talk to Wong about backtracking.

## Authors
Juan Jose Castano Moreno   
jc10536@nyu.edu   
[@juanjomoreno11](https://github.com/juanjomoreno11)   

Rishyak Panchal   
rishyak@nyu.edu   
[@rishyak](https://github.com/rishyak)   
