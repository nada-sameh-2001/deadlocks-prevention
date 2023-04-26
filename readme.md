Deadlocks Prevention by Nada Sameh

Table of content:

1- Introduction

2 - Install

3- Usage

4- Inputs

5- Outputs

6- Requirements

7- Code Explanation

8- Limitations

9- Example

10- Features

11- License

12 - Credits

13 - Technologies Used

14 - Summary

Introduction:

This Python program helps prevent deadlocks by finding a safe sequence of processes to allocate resources. It uses the tkinter library to create a GUI for user input and output display.

Installation

Download the code from GitHub.

Install Python 3.x or later.

Install Tkinter library if not installed (for GUI).

Usage

Run the program using a Python IDE or from the command line

Enter the number of processes and resources.

Enter the allocation and maximum demand matrices.

Enter the available resources.

Click on the "Find Safe Sequence" button.

The safe sequence (if exists) will be displayed.

Inputs

The number of processes (integer)

The number of resources (integer)

Allocation matrix (2D list of integers)

Maximum demand matrix (2D list of integers)

Available resources (list of integers)

Outputs

Safe sequence (if exists) (string)

"No safe sequence" (if there is no safe sequence) (string)

Requirements:

Python 3.x

tkinter library

Code Explanation:

This is a Python program that uses the Tkinter module to create a GUI for finding a safe sequence in the banker's algorithm. The banker's algorithm is a resource allocation and deadlock avoidance algorithm that ensures that there is no deadlock in the system.

The find\_safe\_sequence() function is defined to calculate the safe sequence of processes.

The find\_safe\_sequence() function uses the input data to calculate the safe sequence of processes using the banker's algorithm.

The program takes inputs from the user, including the number of processes, the number of resources, the allocation matrix, the maximum demand matrix, and the available resources. Once the inputs are provided, the user can click the "Find Safe Sequence" button to run the algorithm and find a safe sequence.

The algorithm works by simulating the allocation of resources to processes and checking if there is a safe sequence of processes that can complete their execution without causing a deadlock. If a safe sequence is found, it is displayed in the GUI.

Overall, this program provides a simple implementation of the banker's algorithm with a user-friendly interface.


Limitations:

This program assumes that the input data is correct and does not perform any error handling.

It only finds a safe sequence of processes using the banker's algorithm if any, but does not prevent deadlocks in all situations.

Example:

The Number of processes  = 5

Indicates the Number of resources = 3

Allocations:

{ 0, 0, 1 } = P0

{ 3, 0, 0 } = P1

{ 1, 0, 1 } = P2

{ 2, 3, 2 } = P3

{ 0, 0, 3 } = P4

Max:

{ 7, 6, 3)  = P0

{ 3, 2, 2 } = P1

{ 8, 0, 2 } = P2

{ 2, 1, 2 } = P3

{ 5, 2, 3 }= P4

available  = { 2, 3, 2 }

Output = the safe sequence is : P1 -> P3 -> P4 -> P0 -> P2

Features:

This program is a deadlock prevention algorithm implemented using Python's tkinter library for GUI. It allows the user to input the number of processes, number of resources, allocation matrix, maximum demand matrix, and available resources. The program then calculates a safe sequence of processes to avoid deadlocks and displays it to the user. The user interface is user-friendly, with clear labeling and input fields for each required parameter.

License:

it is an open source for Education purposes for AAST Students

Credits

This tool was created by Nada Sameh.

Technologies Used:

Python programming language

Tkinter module for creating the graphical user interface (GUI)

The Entry widget for inputting data from the user

The Label widget for displaying text in the GUI

The Button widget for triggering an action when clicked

List and nested list data structures for holding and manipulating matrices of data

summary:

Overall, this program provides an easy-to-use GUI for calculating the safe sequence using the Banker's Algorithm, which can be useful in preventing deadlocks in computer systems.

