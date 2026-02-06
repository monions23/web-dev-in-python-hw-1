# Web Development in Python

# HW 1: Python Refresher

## Basic Setup

Clone the repository in VSCode and open in a local folder on your machine.

Then, activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

The .gitignore file will ensure that this venv is not pushed to the remote repository.

Create a python file 'echo.py' with the following code:

```
def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo."""
    pass


if __name__ == "__main__":
    text = input("Yell something at a mountain\n")
    # note: newline character added by me for formatting purposes

    print(echo(text))
```

## My Work

### Part 1: Python Programming Basics: The Echo Function

Below is the initial function that I wrote. I iterated over the **repetitions** variable in reverse, adding a substring of the text variable every time using slicing. I skipped over the value i = 0, as a string sliced with [-0:] would just return that string.

I also put the maximum range argument as **repetitions + 1**, as the specified stop parameter within the range function is not included in the range's count. I wanted to include the value of the repetitions variable, so I had to stop my range at repetitions + 1.

![Echo with If Statement to Handle Range](assets/ReadMe/Echo_Screenshots/Echo_With_If_Statement.png)

However, I quickly remembered that the range function has parameters that can control both the beginning and end of one's chosen range. I therefore got rid of my if statement and changed my **range() arguments** accordingly:

![Echo Correct Range](assets/ReadMe/Echo_Screenshots/Echo_Correct_Range_Extra_Space.png)

**The Output:**

```
Yell something at a mountain
hello there
ere
re
e

```

There was just one problem left - the way my function was written, it was returning an **empty line** after my output was printed. I did some research, and to fix this issue, I turned the echoed_string variable into a **list**, appending to the list during each iteration of the for loop. Then, I used the **join function** to place a newline character in between each element of the list. This effectively produced the correctly formatted output.

![Echo Final Code](assets/ReadMe/Echo_Screenshots/Echo_Final_Code.png)

**The Output:**

```
Yell something at a mountain
hello there
ere
re
e
```

### Part 2: Python Decorator Implementation: The Fibonacci Sequence
