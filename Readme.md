# Simple Calculator

## Table of Contents

- [Simple Calculator](#simple-calculator)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Execution](#execution)
  - [Libraries](#libraries)

## Overview

 A simple calculator that can do basic arithmetic operations. The calculator comes with 2 modes, GUI and CLI.

## Features

- **GUI** :
  - Themes - This incudes dark mode and light mode.
  - History - The ability to store past operations along with their result.

- **CLI** :
  - Simple mode - Enables performing arithmetic operations on two values
  - Advanced Mode - Enables performing arithmetic operations on a list of values (max input is 10).

## Installation

1. Clone the Repository :

    ```bash
    git clone git@github.com:M00N-N1T3/codsoft_task1.git
    ```

## Execution

1. GUI

    ```python
    python3 calculator.py
    ```

2. CLI

   ```python
    python3 calculator --no-gui
    ```

Run python3 calculator --hep to access the help manual.

## Libraries

- tkinter - for the graphical user interface

All used libraries are placed in the [lib](lib) package.
