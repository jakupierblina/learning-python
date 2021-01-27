<h1 style="color: darkblue;" >Python Is Engineering, Not Art </h1>

<img src="undraw_voice_interface_eckp-1024x855.png">

<ins>Are you ready? </ins>

<ins>Make a coffee and sit with me! We gonna go through all of it together. </ins>



# Intro

Python is high level programing language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer/simpler lines of code.

Python's traditional runtime execution model: source code you type is translated to byte code, which then will be run by Python Virtual Machine. Your code is automatically compiled, but then it is interpreted.

The Python interpreter is a program that runs the Python source code you write. Source code is/are statements you write for your program - it consists of text(byte code) in textfiles that ends with .py extension. Bytecode is the lower level from your program after Python compiles it. Python automatically stores the bytecode in the files with .py extension.

After the code you type in, the Python Virtual Machine (PVM) - the runtime engine of Python interprets your bytecode (compiled byte code).



<h4> Object types </h4>

Python programs can be decomposed into modules, statements, expressions and objects as follow:

- Programs are composed of modules.
- Modules contain statements.
- Statements contain expressions.
- Expressions create and process objects.

In typical Python programs most of this grunt work goes away. Because Python provides powerful object types as an intrinsic part of the language, there is usually no need to code object implementation before you start solving problems. 

<i>Program units</i> such as functions,modules and classes are objects in Python- they are created with statements and expressions such as <b>def,class, import</b> and <b>lambda</b>. 



NOTE: In Python, data takes the form of objects - either built-in objects that Python provides or objects we create using Python tools and other languages such as C.

<h6> Numeric Type Basics</h6>

In Python numbers are not really a single object type, but a category of similar types. In a complete inventory of Python's numeric toolbox includes:

- Integers and floating-point numbers

  ​		Integers are written as strings of decimal digits. Floating-point numbers have a decimal point and an optional signed exponent!

- Complex numbers

  ​		Python complex literals are written as real-part + imaginary-part as are represented in Math. 

- Fixed-precision decimal numbers

- Rational fraction numbers

- Sets

  an unordered collection of unique and immutable objects that supports operations corresponding to mathematical set theory. By definition an item appears only once in a set, no matter how many times it is added.  Note: sets do not map keys to values, they are neither sequence nor mapping types.

- Booleans

- Unlimited integer precision

- A variety of numeric built-ins and modules



The table bellow gives a basic notes about the expression operators and precedence in Python.

<table>
    <tr>
   	 <th> Operations</th>
   	 <th> Description </th>
     </tr>
    <tr>
        <td> yeild x</td>
        <td> Generator function</td>
    </tr>
    <tr>
        <td> lambda args: expression</td>
        <td> Anonymous function generation</td>
    </tr>
    <tr>
        <td> x if y else x</td>
        <td> Ternary selection (x is evaluated only if y is true)</td>
    </tr>
    <tr>
        <td> x or y</td>
        <td> Logical OR (y is evaluated only if x is false)</td>
    </tr>
     <tr>
        <td> x and y</td>
        <td> Logical AND (y is evaluated only if x is true)</td>
    </tr>
    <tr>
        <td> not x</td>
        <td> Logical NEGATION</td>
    </tr>
    <tr>
        <td> x in y, x not in y</td>
        <td> Membership (iterables,sets)</td>
    </tr>
    <tr>
        <td> x in y, x is not y </td>
        <td> Object identity tests </td>
    </tr>
    <tr>
        <td> x<y, x<= y, x>y, x>=y, x==y, x!=y </td>
        <td> Magnitude comparson, set subset and superset; Value equality operations</td>
    </tr>
    <tr>
        <td> x | y</td>
        <td> Bitwise OR, set union </td>
    </tr>
    <tr>
        <td> x ^ y</td>
        <td> Bitwise XOR, set symetric difference </td>
    </tr>
    <tr>
        <td> x & y </td>
        <td> Bitwise AND, set intersection </td>
    </tr>
    <tr>
        <td> x << y, x >> y</td>
        <td> Shift x left or right by y bits </td>
    </tr>
    <tr>
        <td> x * y <br> x%y <br> x/y, x//y</td>
        <td> Multiplication, repetition; <br> Remainder,format; <br> Division: true and floor</td>
    </tr>
    <tr>
        <td> -x, +x</td>
        <td> Negation, identity</td>
    </tr>
    <tr>
        <td> ~x</td>
        <td> Bitwise NOT (inversion) </td>
    </tr>
    <tr>
        <td> x ** y</td>
        <td> Power (exponentiaton) </td>
    </tr>
    <tr>
        <td> x[i]</td>
        <td> Indexing(sequence, mapping, others)</td>
    </tr>
    <tr>
        <td> x[i:j:k]</td>
        <td> Slicing</td>
    </tr>
    <tr>
        <td> x(...)</td>
        <td> Call (function, method,class, othercallable)</td>
    </tr>
    <tr>
        <td> x.attr</td>
        <td> Attribute reference </td>
    </tr>
    <tr>
        <td> (...)</td>
        <td> Tuple, expression, generator expression</td>
    </tr>
    <tr>
        <td> [...]</td>
        <td> List, list comperhesion</td>
    </tr>
    <tr>
        <td> {...}</td>
        <td> Dictionary, set, set and dictionary comperhesion</td>
    </tr>
</table>



repr -> is used by echoes: as-code form

str -> is used by print: user-friendly form

Both of these convert arbitrary objects to their string representation

***

<i><mark><b>In python explicit is better than implicit and simple is better than complex.</b></mark> </i>

***



<h4> Dive in </h4>

Python is unique for <i>dynamic typing</i> model. In Python, types are determined automatically at runtime, not in response to declarations in your code. This means that your variables are never declared ahead time. This <i>dynamic typing</i> is can be explained in an easier form;

for example if we declare x =9, Python will perform this request into three steps:

1. Create an object to represent the value 9.
2. Create the variable <b>x</b>, if it doesn't exist yet.
3. Link the variable <b>x</b> to the new object 3.

Long story short variable x becomes a reference to the object 9.

Remainder:

- <i><b>Variables</b></i> are entries that links to objects.
- <i><b>Object</b></i> are representation of the values they stand for.
- <i><b>References</b></i> are pointers.

Each time you generate a new value in your script by running the file, Python creates a new object to represent that value. Furthermore Python handles the reclaim of the object by Garbage-Collection, which means that every times you update the value of the object it will automatically thrown the future/new object.







<h4> Debugging </h4>

Read the error message and go fix the tagged line. 

Another way debugging your code is to insert <i>print</i> statements. 

Furthermore you can use <i>IDE GUI debuggers </i>which is a sort of point-and-click debugging support.



# Q&A

1. <b>What are the six main reasons that people choose to use Python?</b>

   Software quality, developer productivity, program portability, support libraries, component integration, and simple enjoyment. Of these, the quality and productivity themes seem to be the main reasons that people choose to use Python

2.  <b>Name four notable companies or organizations using Python today.</b>

   Google, Industrial Light & Magic, EVE Online, Jet Propulsion Labs, Maya, ESRI, and many more. Almost every organization doing software development uses Python in some fashion, whether for long-term strategic product development or for short-term tactical tasks such as testing and system administration.

   

3. <b>Why might you not want to use Python in an application?</b>

   Python’s downside is performance: it won’t run as quickly as fully compiled languages like C and C++. On the other hand, it’s quick enough for most applications, and typical Python code runs at close to  speed anyhow because it invokes linked-in C code in the interpreter. If speed is critical, compiled extensions are available for number-crunching parts of an application.

4. <b>What can you do with Python? </b>

   You can use Python for nearly anything you can do with a computer, from website development and gaming to robotics and spacecraft control.

5. <b>What’s the significance of the Python import this statement? </b>

   import this triggers an Easter egg inside Python that displays some of the design philosophies underlying the language. You’ll learn how to run this statement in the next chapter.

6. <b>Why does “spam” show up in so many Python examples in books and on the Web? </b>

   “Spam” is a reference from a famous Monty Python skit in which people trying to order food in a cafeteria are drowned out by a chorus of Vikings singing about spam. Oh, and it’s also a common variable name in Python scripts..

   