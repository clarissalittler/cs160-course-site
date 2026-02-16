# Lesson 5 --- Encoding Text

![Unit 1 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Represent text using the ASCII encoding scheme.
- Explain how encoding text is an abstraction.

---

## From numbers to text

In the previous lesson, we figured out how to encode numbers in binary. That's great and all, but computers need to deal with more than just numbers --- they need to handle *text*. The words you're reading right now, the texts you send, the code programmers write --- it's all text, and it all needs to live inside a computer as binary.

So how do we get from 0's and 1's to the letter "A"?

Here's the key insight: if we can figure out a way to represent information as a set of numbers, then we can encode it in bits and store it in a computer. Numbers to binary? We already know how to do that. So the only missing piece is: **how do we turn text into numbers?**

The answer, as with most things in computer science, is that a bunch of people got together and *agreed on a system*.

## ASCII

**ASCII** --- which stands for American Standard Code for Information Interchange, and is pronounced "ASK-ee" --- is an encoding scheme that maps most of the symbols you can type on an American keyboard to numbers.

The idea is beautifully simple. When we want to store the uppercase letter **A**, we store the number **65**. The computer doesn't know what an "A" is. It just knows the number 65, which it stores in binary as `01000001`. When it's time to display that value on screen, the computer looks up what character corresponds to 65 and draws an A. That's it. That's the whole trick.

![ASCII value 65 for the letter A](images/ascii_letter_A.png)
*Figure 1.7. ASCII value for 'A'*

Here's a little history that I think is fun: ASCII was first developed in the early 1960s, back when "computer" still sounded like a science fiction word to most people. The standard was published in 1963, and it's still the backbone of how we encode basic English text today. Not bad for a 60-year-old idea.

## The ASCII table

Below is the full ASCII table. You'll notice two key columns: **Dec** (the decimal number) and **Char** (the character it represents). The decimal value is what the computer actually stores --- mapped to binary, of course.

If you want a video walkthrough, here's one that [explains the ASCII table in more detail](https://www.youtube.com/watch?v=m5G5LqDE6_o). (It has some C++ programming details in it, but it's really aimed at explaining bits and bytes as they relate to ASCII and character encoding.)

| Dec | Char | Name/Function | | Dec | Char | | Dec | Char | | Dec | Char |
|-----|------|---------------|-|-----|------|-|-----|------|-|-----|------|
| 0 | NUL | Null | | 32 | (space) | | 64 | @ | | 96 | \` |
| 1 | SOH | Start Of Heading | | 33 | ! | | 65 | A | | 97 | a |
| 2 | STX | Start Of Text | | 34 | " | | 66 | B | | 98 | b |
| 3 | ETX | End Of Text | | 35 | # | | 67 | C | | 99 | c |
| 4 | EOT | End Of Transmit | | 36 | $ | | 68 | D | | 100 | d |
| 5 | ENQ | Enquiry | | 37 | % | | 69 | E | | 101 | e |
| 6 | ACK | Acknowledge | | 38 | & | | 70 | F | | 102 | f |
| 7 | BEL | Bell | | 39 | ' | | 71 | G | | 103 | g |
| 8 | BS | Backspace | | 40 | ( | | 72 | H | | 104 | h |
| 9 | HT | Horizontal Tab | | 41 | ) | | 73 | I | | 105 | i |
| 10 | LF | Line Feed | | 42 | * | | 74 | J | | 106 | j |
| 11 | VT | Vertical Tab | | 43 | + | | 75 | K | | 107 | k |
| 12 | FF | Form Feed | | 44 | , | | 76 | L | | 108 | l |
| 13 | CR | Carriage Return | | 45 | - | | 77 | M | | 109 | m |
| 14 | SO | Shift Out | | 46 | . | | 78 | N | | 110 | n |
| 15 | SI | Shift In | | 47 | / | | 79 | O | | 111 | o |
| 16 | DLE | Data Line Escape | | 48 | 0 | | 80 | P | | 112 | p |
| 17 | DC1 | Device Control 1 | | 49 | 1 | | 81 | Q | | 113 | q |
| 18 | DC2 | Device Control 2 | | 50 | 2 | | 82 | R | | 114 | r |
| 19 | DC3 | Device Control 3 | | 51 | 3 | | 83 | S | | 115 | s |
| 20 | DC4 | Device Control 4 | | 52 | 4 | | 84 | T | | 116 | t |
| 21 | NAK | Non Acknowledge | | 53 | 5 | | 85 | U | | 117 | u |
| 22 | SYN | Synchronous Idle | | 54 | 6 | | 86 | V | | 118 | v |
| 23 | ETB | End Transmit Block | | 55 | 7 | | 87 | W | | 119 | w |
| 24 | CAN | Cancel | | 56 | 8 | | 88 | X | | 120 | x |
| 25 | EM | End Of Medium | | 57 | 9 | | 89 | Y | | 121 | y |
| 26 | SUB | Substitute | | 58 | : | | 90 | Z | | 122 | z |
| 27 | ESC | Escape | | 59 | ; | | 91 | [ | | 123 | { |
| 28 | FS | File Separator | | 60 | < | | 92 | \ | | 124 | \| |
| 29 | GS | Group Separator | | 61 | = | | 93 | ] | | 125 | } |
| 30 | RS | Record Separator | | 62 | > | | 94 | ^ | | 126 | ~ |
| 31 | US | Unit Separator | | 63 | ? | | 95 | _ | | 127 | DEL |

*Figure 1.8. ASCII Table*

ASCII codes were originally **7 bits** long, which gives us 128 possible values (2^7 = 128). Here's how they break down:

- **0--31** are "control characters" --- they're largely defunct now, but they used to control various aspects of machines and printers. Some are still kicking around, though: you've probably heard of "carriage return" (13) and "line feed" (10) --- those are still how computers represent the end of a line of text. The name "carriage return" comes from typewriters, where you'd literally shove the carriage back to the left side. (There's code 7, BEL, which was supposed to ring an actual bell. Computers used to be *noisy*.)

- **32--126** are the printable characters --- digits 0--9, all 26 letters in both lowercase and uppercase, and common punctuation symbols. This is the stuff you actually type.

- **127** is delete.

Over time, 8 bits became the standard "chunk size" for storing data --- a byte. ASCII made the transition to 8-bit encoding by simply adding an extra 0 to the front of the old 7-bit codes. So the letter A, which was `1000001` in 7-bit ASCII, became `01000001` in 8-bit ASCII. Simple enough.

### But wait --- what about other languages?

You might have noticed that ASCII is very *American*. It handles English just fine, but what about Chinese characters? Arabic script? Japanese? Accented letters in French or Spanish? Even something as basic as the pound sign (as in British currency) wasn't in the original ASCII table.

This is a genuinely important limitation, and it led to the development of **Unicode**, which we'll encounter later. For now, just know that ASCII was a great start, but the world is bigger than the American keyboard. There's definitely no possibility that this limited character set will cause problems later in a really annoying way!

## Abstraction in action

Here's a thought exercise. Look at the picture below --- a simple text conversation:

![Text messages between two users](images/text_messages.png)

What details are hidden from our focus?

<details>
<summary>Show Solution</summary>

When you send a text message, the letters you press on your screen are stored and sent as binary numbers. But you don't see any of that. You just type "hey what's up" and hit send. The conversion from characters to ASCII values to binary and back again is completely invisible.

This is what we call an **abstraction** --- something where you don't need to understand how it works under the hood in order to use it confidently. You text people every day without thinking about binary. You drive a car without understanding combustion engineering. You flip a light switch without knowing anything about electrical grids.

![Text message as an abstraction --- text is stored as ASCII, sent as 0's and 1's](images/ascii_abstraction.png)

Abstraction is one of the most powerful ideas in computer science. It's how we manage complexity --- by hiding the messy details behind clean interfaces. We'll keep coming back to this concept throughout the course.

What are some other abstractions in your everyday life? Things where you don't completely understand how they work, but you use them with total confidence?

</details>

## Check for understanding!

[LMS Activity: Unit 1 Lesson 5 Check for Understanding]
