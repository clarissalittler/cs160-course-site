# Lesson 6 --- Logical Operators

> **By the end of this lesson, you'll be able to:**
>
> - Evaluate simple circuits using the AND, OR, and NOT gates
> - Use the logical operators `and`, `or`, and `not` to build complex conditional statements

## Lesson Video

[Video: Logical Operators](https://www.youtube.com/watch?v=OnX91LCQ0eQ)

## Logic Gates

Logic gates are a fundamental part of your computer's hardware --- they're how the processor (CPU) actually *does* computations and directs the flow of information. Remember, inside your computer, you've got electricity flowing around. "True" is represented by a high voltage, and "false" is represented by a low voltage. That's it. Everything your computer does comes down to voltages being high or low.

## AND Gate

AND gates take two inputs (from the left) and produce one output (to the right). An AND gate outputs 1 only if *both* inputs are 1; otherwise, it outputs 0. (You can read "1" as "true" and "0" as "false".)

Below is a demo of an AND gate --- notice the shape. Turn the light switches on and off to see the results. FALSE (off) AND FALSE (off) gives you a lightbulb that's off, which is FALSE. How do you turn the lightbulb on?

[Interactive: AND gate demo](https://logic.ly/embed/?document_path=/lessons/documents/and-gate.logicly)

## OR Gate

OR gates also take two inputs and produce one output. An OR gate outputs 1 if *one or both* inputs are 1; otherwise, it outputs 0. Below is a demo of an OR gate --- notice how the shape is different from the AND gate. How do you turn the lightbulb on?

[Interactive: OR gate demo](https://logic.ly/embed/?document_path=/lessons/documents/or-gate.logicly)

## NOT Gate

The NOT gate is the simplest one --- it just flips the input. If the input is TRUE, the output is FALSE. If the input is FALSE, the output is TRUE. That's it. One input, one output, and it reverses whatever you give it. Below is a demo --- notice the shape. How do you turn the lightbulb on?

[Interactive: NOT gate demo](https://logic.ly/embed/?document_path=/lessons/documents/not-gate.logicly)

## Practice

> What's the output of this circuit when both inputs are TRUE (the light switches are turned ON)?
>
> **Note:** The two wires that cross each other are *not* connected.
>
> ![logic gate puzzle: from left to right, 1's are input to 2 NOT gates, those outputs are input into 2 AND gates along with a 1, those outputs are inputs to an OR gate](images/logic_gate_puzzle.png)

<details>
<summary>Show Solution</summary>

The output is 0 (FALSE). The input to each AND gate is a 1 and a NOT 1 (which is 0). 1 AND 0 is 0. Then those two 0's feed into the OR gate, and 0 OR 0 is also 0!

</details>

## Logical Operators in Code

In coding, we can use logical operators between conditions to create complex Boolean expressions. They work exactly like the gates we just looked at:

- **`and`** --- both conditions must be true
- **`or`** --- either condition must be true (or both)
- **`not`** --- reverses the truth of an expression

| Expression | Meaning |
|---|---|
| `x > y and a < b` | Is `x` greater than `y` AND is `a` less than `b`? |
| `x == y or x == z` | Is `x` equal to `y` OR is `x` equal to `z`? |
| `not (x > y)` | Is the expression `x > y` NOT true? |

**Note:** When you see an expression like `x > y and a < b`, Python evaluates the comparison on the left side of the `and` first, then the right side, and *then* evaluates the `and` with the two Boolean values. Think of it as `(x > y) and (a < b)`.

> **Bug Alert!**
>
> In the program below, `x = 1`, `y = 4`, and `z = 3`, and we want to check if any of them equal 2. None of them do, so we'd expect the result to be "2 is not found." Run the program to see what actually happens.
>
> Here's the gotcha: the operands on either side of a logical operator need to be true or false *expressions*. In `x or y or z == 2`, the first operand is just `x` --- which is the integer 1, not a Boolean expression. And in computer science, 0 is false but *anything else* is true! So `x` evaluates to true, and the whole expression short-circuits to true. That's... sneaky and annoying.

Fix the error by making each operand a proper Boolean expression. Copy the code or download [logical_ops.py](https://drive.google.com/file/d/1fxn3LBFqBxjhWyqT51QuYWTJdi_l-6yy/view?usp=drive_link) and run it in your IDE of choice:

```python
def main():
    x = 1
    y = 4
    z = 3

    if x or y or z == 2:
        print("There is a 2!")
    else:
        print("2 is not found.")

main()
```

## Trivia!

> How high is "high voltage" inside a computer?

<details>
<summary>Show Solution</summary>

When transistors became commonly used in computer circuitry, "high" voltage was represented by about 5 volts --- enough to make the transistors work, light a small LED, or (nowadays) power a USB flash drive. "Low" voltage has always been pretty close to 0 volts.

As manufacturing processes improved and circuits got smaller, manufacturers decreased the voltage in CPU and memory chips to reduce power consumption and heat. These days, CPUs and RAM run at about 1.3 to 1.5 volts. So when we say "high voltage" in a computer, we're really not talking about much --- you won't feel a thing!

</details>

## Check for Understanding

[LMS Activity: Unit 4 Lesson 6 --- Check for Understanding quiz]
