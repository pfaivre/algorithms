# Weighted Random Pick

## Definition

Considering that we have a list of weighted elements, we want to choose randomly
one of them based on the probability given by their weight.

This is an efficient implementation that doesn't construct a second array and 
can work with decimal weights values.

**complexity**: _O_(_n_)

**input**: 
* An array with couples (object, weight);
* A function that will be called to generate a random number between 0 and 1.
**output**: The choosen object.

## usage

