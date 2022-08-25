# Boggle

Boggle game in Javascript and Python.

## The Game

The goal of the game is to get the highest point total. To gain points, players create words from a random assortment of letters in a 5x5 grid. We will be providing the functionality to generate the grid.

Words can be created from adjacent letters – that is, letters which are horizontal or vertical neighbors of each other as well as diagonals. The letters must connect to each other in the proper sequence to spell the word correctly. This means that the next letter in the word can be above, below, left, or right of the previous letter in the word (excluding any letters previously used to construct the word).

## Set up

__Linux:__

```python3 -m venv venv```

```source venv/bin/activate```

```(venv) pip install -r requirements.txt```

```(venv) flask run```

__Windows:__

```python3 -m venv venv```

or

```python3 -m pip install virtualenv venv```

```venv\Scripts\activate.bat```

```(venv) python3 -m pip install -r requirements.txt```

```(venv) flask run ```