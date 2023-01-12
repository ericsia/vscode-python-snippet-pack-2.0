[![pytest](https://github.com/ericsia/vscode-python-snippet-pack-2.0/actions/workflows/pytest.yml/badge.svg)](https://github.com/ericsia/vscode-python-snippet-pack-2.0/actions/workflows/pytest.yml)
### Best Python3 Snippets Pack (2022) for Visual Studio Code (python 3.x)
[![status.svg](status.svg)](https://github.com/ericsia/vscode-python-snippet-pack-2.0/issues) ![light.svg](light.svg) ![easy.svg](easy.svg)

#### A beginner friendly Python Snippets auto suggestion pack making you more productive
#### Please help to rate this extensions [5 stars](https://marketplace.visualstudio.com/items?itemName=EricSia.pythonsnippets3&ssr=false#review-details) and [share](https://marketplace.visualstudio.com/items?itemName=EricSia.pythonsnippets3) it, [feedback is welcome](https://github.com/ericsia/vscode-python-snippet-pack-2.0/blob/master/CONTRIBUTING.md)
#### Tips: uninstall similar python snippet extension first. Then install and Reopen
* added with new [python](https://docs.python.org/3/library/stdtypes.html) function, update legacy code
* fixes a few unintended typo left by previous developer
* use `TAB` to rename field in every method / feature
* added `def.function.main-()` as a main method, type `main-`
* added `def.function.class-(init)` for class, type `class-` or `init-`
* added label to method belong to string/list/tuple/set/dict
* added python `<datatype>` and snippet initialisation, try typing `str`
* added `match` snippet - python 3.10
* added `np-init` snippet for numpy array [pip3 install numpy]
* added `import` snippet, `documentation` snippet
* added `random` snippet try `random-TextGen`
* added `for-`loop snippet
* added `print-` snippet
* added matplotlib template `plt`
* added algorithm template `algo-`
* added PyMySQL template `PyMySQL`
* added Django template `django`
* added `dp` decimal place, `swap`, `slice`, `sleep`, `end`, `benchmark`, `timeit`, `env`, `self` snippet
* new format for easier selection, to see built in example type `apply-`, `random-`, `class` 
* get example use `<datatype>-` while for available method use `-<datatype>` ex: `-string`
* welcome to contribute through feedback to add more ideas, make it as complete as possible

### Extra
* checkout my [site](https://github.com/MedlexoNews/Update)

<img src="https://github.com/ericsia/vscode-python-snippet-pack-2.0/raw/HEAD/python.gif" alt="screenshot" height="450" />

#### Don't worry if you never see that method before, this extension provided a lot of code examples for that.
#### This extensions not only provide snippets but also is helpful for learning python programming language.
* all python built-in snippets and with at least one example `=>` for each method
* For example if you want to use string replace method type `.replace` 
* But if you don't know how to use replace method then type `str` find str-replace=>
* Contains a lot of other code snippets (like if:else, for, while, while:else, try:catch, fileIO and oop class snippets examples (polymorphism, encapsulation, inheritance)


## Old gif from (2018) pay tribute to Ferhat Yalçın
![oldScreenshot](oldpython.gif)

## Snippets | Descriptions (from 2018, new one is at top)
| There are string/list/tuple/set/dict datatype snippet      | E.g. Type Out |
|------------------------------------------------------------|---------------|
| To get `__main__` type `def` or `function` or `main-`      | `main-`       |
| To see built-in method example type `apply-` scroll down   | `apply-`      |
| Tips: to see specific method type example `name=`          | `count=`      |
| To see datatype method example type `<datatype>-`          | `str-`        |
| To see datatype method only type `-<datatype>` scroll down | `-string`     |
| To see python `datatype`                                   | `dtype`       |
| To initialise type `<datatype> initialise` snippet         | `bool init`   |
| To get fileIO type `file-` then scroll down                | `file-`       |
| To get block comment type `documentation`                  | `doc`         |
| To get algorithm snippet like `is_prime`                   | `algo-`       |

<br />

| Built-in methods code snippets | Description                                                                                                                                                                                             |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abs                            | Returns the absolute value of a number                                                                                                                                                                  |
| all                            | Returns True if all items in an iterable object are true                                                                                                                                                |
| any                            | Returns True if any item in an iterable object is true                                                                                                                                                  |
| ascii                          | Returns a readable version of an object. Replaces none-ascii characters with escape character                                                                                                           |
| bin                            | Returns the binary version of a number                                                                                                                                                                  |
| bool                           | Returns the boolean value of the specified object                                                                                                                                                       |
| bytearray                      | Returns an array of bytes                                                                                                                                                                               |
| bytes                          | Returns a bytes object                                                                                                                                                                                  |
| callable                       | Returns True if the specified object is callable, otherwise False                                                                                                                                       |
| chr                            | Returns a character from the specified Unicode code.                                                                                                                                                    |
| delattr                        | Deletes the specified attribute (property or method) from the specified object                                                                                                                          |
| dict                           | Returns a dictionary (Array)                                                                                                                                                                            |
| dir                            | Returns a list of the specified object's properties and methods                                                                                                                                         |
| divmod                         | Returns the quotient and the remainder when argument1 is divided by argument2                                                                                                                           |
| enumerate                      | Takes a collection (e.g. a tuple) and returns it as an enumerate object                                                                                                                                 |
| eval                           | Evaluates and executes an expression                                                                                                                                                                    |
| exec                           | Executes the specified code (or object)                                                                                                                                                                 |
| filter                         | Use a filter function to exclude items in an iterable object                                                                                                                                            |
| float                          | Returns a floating point number                                                                                                                                                                         |
| frozenset                      | Returns a frozenset object                                                                                                                                                                              |
| getattr                        | Returns the value of the specified attribute (property or method)                                                                                                                                       |
| globals                        | Returns the current global symbol table as a dictionary                                                                                                                                                 |
| hasattr                        | Returns True if the specified object has the specified attribute (property/method)                                                                                                                      |
| hash                           | Returns the hash value of a specified object                                                                                                                                                            |
| help                           | Executes the built-in help system                                                                                                                                                                       |
| hex                            | Converts a number into a hexadecimal value                                                                                                                                                              |
| id                             | Returns the id of an object                                                                                                                                                                             |
| input                          | Allowing user input                                                                                                                                                                                     |
| int                            | Returns an integer number                                                                                                                                                                               |
| isinstance                     | Returns True if a specified object is an instance of a specified object                                                                                                                                 |
| issubclass                     | Returns True if a specified class is a subclass of a specified object                                                                                                                                   |
| iter                           | Returns an iterator object                                                                                                                                                                              |
| len                            | Returns the length of an object                                                                                                                                                                         |
| locals                         | Returns an updated dictionary of the current local symbol table                                                                                                                                         |
| map                            | Returns the specified iterator with the specified function applied to each item                                                                                                                         |
| max                            | Returns the largest item in an iterable                                                                                                                                                                 |
| memoryview                     | Returns a memory view object                                                                                                                                                                            |
| min                            | Returns the smallest item in an iterable                                                                                                                                                                |
| next                           | Returns the next item in an iterable                                                                                                                                                                    |
| object                         | Returns a new object                                                                                                                                                                                    |
| oct                            | Converts a number into an octal                                                                                                                                                                         |
| open                           | Opens a file and returns a file object                                                                                                                                                                  |
| ord                            | Given a string of length one, return an integer representing the Unicode code point of the character when the argument is a unicode object, or the value of the byte when the argument is an 8-bit str. |
| pow                            | Return x to the power y                                                                                                                                                                                 |
| print                          | Prints to the standard output device                                                                                                                                                                    |
| property                       | Gets, sets, deletes a property                                                                                                                                                                          |
| range                          | Returns a sequence of numbers, starting from 0 and increments by 1 (by default)                                                                                                                         |
| repr                           | Returns a readable version of an object                                                                                                                                                                 |
| reversed                       | Returns a reversed iterator                                                                                                                                                                             |
| round                          | Rounds a numbers                                                                                                                                                                                        |
| slice                          | Returns a slice object                                                                                                                                                                                  |
| sorted                         | Returns a sorted list                                                                                                                                                                                   |
| staticmethod                   | Converts a method into a static method                                                                                                                                                                  |
| str                            | Returns a string object                                                                                                                                                                                 |
| sum                            | Sums the items of an iterator                                                                                                                                                                           |
| super                          | Return a proxy object that delegates method calls to a parent or sibling class of type.                                                                                                                 |
| type                           | Returns the type of an object                                                                                                                                                                           |
| unichr                         | Return the Unicode string of one character whose Unicode code is the integer i.                                                                                                                         |
| vars                           | Returns the __dict__ property of an object                                                                                                                                                              |
| zip                            | Returns an iterator, from two or more iterators                                                                                                                                                         |

<br />

| import code snippets | Description   |
|----------------------|---------------|
| import               | import module |

<br />

| function code snippets  | Description                           |
|-------------------------|---------------------------------------|
| def or function         | Defining Function                     |
| def=>with_default_value | Defining Function with default values |

<br />

| file code examples `file-`      | Description                           |
|---------------------------------|---------------------------------------|
| withFile-listFile               | List files in that path               |
| withFile-listFileWithPath       | List files with path                  |
| withFile-openFile               | Open a file                           |
| withFile-openFileReadLine       | Read file line by line                |
| withFile-openFileReadSingleLine | Read one line of the file             |
| withFile-appendFile             | Write to an Existing File             |
| withFile-overwriteFile          | Open a file and overwrite the content |
| withFile-deleteFile             | Delete a file                         |

<br />

| if/else statement | code snippets | Description     |
|-------------------|---------------|-----------------|
| if-               |               | if              |
| if-elif           | or ifelif     | if:else if      |
| if-elif-else      | or ifelifelse | if:else if:else |
| if-else           | or ifelse     | if:else         |
| if-short          | or ifshort    | ternary if      |
| else              |               | else            |

<br />

| match aka switch code snippets | Description     |
|--------------------------------|-----------------|
| switch or match                | match Statement |

<br />

| try catch | code snippets | Description             |
|-----------|---------------|-------------------------|
| try-      |               | try:except              |
| try-f     | or tryf       | try:except:finally      |
| try-e     | or trye       | try:except:else         |
| try-e-f   | or tryef      | try:except:else:finally |

<br />

| for loop code snippets | Description   |
|------------------------|---------------|
| for-                   | for Statement |

| for loop code examples  |             |
|-------------------------|-------------|
| for=>                   | for example |
| for=>through_a_string   | for example |
| for=>break_statement    | for example |
| for=>continue_statement | for example |
| for=>range_function_1   | for example |
| for=>range_function_2   | for example |
| for=>range_function_3   | for example |
| for=>for_else           | for example |

<br />

| while loop code snippets | Description     |
|--------------------------|-----------------|
| while-                   | while Statement |

| while loop code examples  | Description   |
|---------------------------|---------------|
| while=>                   | while example |
| while=>break_statement    | while example |
| while=>continue_statement | while example |

<br />

| List Comprehensions code snippets | Description         |
|-----------------------------------|---------------------|
| comp=>                            | List Comprehensions |

<br />

| lambda code examples | Description                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| lambda               | A lambda function can take any number of arguments, but can only have one expression. |

<br />

| class code snippets | Description           |
|---------------------|-----------------------|
| class=>             | python class          |
| `__init__`=>        | class __init__ method |
| `__iter__`=>        | class __iter__ method |
| `__next__`=>        | class __next__ method |

| class code examples     | Description                  |
|-------------------------|------------------------------|
| class=>_1               | oop inheritance example      |
| class=>inheritance_1    | oop inheritance example      |
| class=>inheritance_2    | oop inheritance example      |
| class=>with_attribute_1 | class with attribute example |
| class=>with_attribute_2 | class with attribute example |
| class=>with_attribute_3 | class with attribute example |
| class=>with_method_1    | class with method example    |
| class=>with_method_2    | class with method example    |
| class=>encapsulation    | class encapsulation example  |
| class=>polymorphism     | class polymorphism example   |

### For example

Class Template - thanks for `snippsat` mention f-string

class=>with_attribute_1

```
class Parrot:

# class attribute
 species = 'bird'

# instance attribute
 def __init__(self, name, age):
 self.name = name
 self.age = age

# instantiate the Parrot class
blu = Parrot('Blu', 10)
woo = Parrot('woo', 15)

# access the class attributes
print(f'Blu is a {blu.__class__.species}')
print(f'Woo is also a {woo.__class__.species}')
# access the instance attributes
print(f'{blu.name} is {blu.age} years old')
print(f'{woo.name} is {woo.age} years old')
```

## Release Notes

This extension aim to cover as many new Python3 method make it as complete as possible, please help to contribute from feedback link above.

### For more information - Thanks to

* [python documentation](https://docs.python.org/3/tutorial/index.html)
* [w3schools](https://www.w3schools.com/python/default.asp)
* [www.programiz](https://www.programiz.com/python-programming)
* [python.swaroopch](https://python.swaroopch.com/oop.html)
* [pythonforbeginners](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)
* [Christian Clauss's Python Algorithms ](https://github.com/TheAlgorithms/Python) - open source community for providing algorithms for our snippets


**Enjoy! Type less do more**

### 1.0.2

Initial release and update README.md

### 2.0.2

Updated and maintain in year 2022

### 3.0.2

Change .format into f-string and remove unnecessary files

### 3.3.5

change . become - due to vscode clash ex `apply.` become `apply-`

### 3.3.11
added PyMySQL, Algo, Random snippet by Lakshmikanth

### 3.3.12
remove dot in built-in methods for good, to see type `-<datatype>` then scroll down.
Tips, tick in setting: Python › Analysis: Complete Function Parens

### 3.3.13
added Django snippet by Lakshmikanth

-----------------------------------------------------------------------------------------------------------
