# Assignment 1 Due 3/2 Monday, 11:59pm 


**Please read Code Grading Rubric carefully before you start this assignment.**

1. (20 points) Factoring of integers. Write a program that asks the user for an integer and then prints out all its factors. For example, when the user enters 150, the program should print
    ```
    2
    3
    5
    5
    ```
    You need to check user's input first to make sure it is an integer.


2. (20 points) The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions and stumbles to the next intersection, then again randomly picks one of four directions, and so on. You might think that on average the drunkard doesn’t move very far because the choices cancel each other out, but that is actually not the case.

	Write a function to calculate the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) after n intersections. 

3. (20 points) Use `Turtle` to draw the drunkard's walk in #3. 

4. (20 points) Find out how many words in the text file, `drunkard_words.txt`, are good words.

    A good word should:
    - contain at least three vowels (`aeiou` only).
    - contain at least one letter that occurs twice in a row.
    - not contain any of the disallowed strings even if they are part of above requirements. The disallowed strings are `ab`, `cd` and `xy`, 
  
5. (20 points) Find out how many words in the text file, `drunkard_words.txt`, are awesome words.

    A awesome word should:
    - contain a combination of any two adjacent letters that occurs at least twice in the same word without overlapping. For example, `abcdefgab` is awesome (because `ab` appears twice), but `zzz` is not.
    - contain at least a `xyx`-type substring. For example: `aba`, `abcdefegh` (because of `efe`), or even `zzz`.




 
