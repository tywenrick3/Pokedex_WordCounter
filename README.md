## CS-UY 1114 — Lab 9
# The Wonderful World of Dictionaries
#### Friday, April 9th, 2021


**All lab work must be submitted within 24 hours of the start of your lab period on Gradescope** (we will be checking
this using the timestamps of your last submission on GradeScope). This, of course, also means that if you submit a
solution before your allotted lab time, you will get no credit. You must try each problem at least once (that is,
submitting at least one attempt to GradeScope, whether it is correct or not). You are welcome to continue to work on the
problems and continue submitting to Gradescope until you are satisfied with your results. It is your responsibility to
remember to submit your work.


Please note that your overall point value is awarded by the teaching assistants verifying that you attempted and
submitted each problem at least once! For every hour that your work is late on GradeScope, we will deduct 0.5 points
from the total 10-point value of the lab. **The points awarded by the auto-grader on GradeScope will not be counted
towards your lab's grade, so don't worry if you don't pass every or any of its tests!**


Please do not hesitate to check with your TAs if you are ever confused as to how to proceed!


---

### The use of any modules that handle files non-natively (i.e. `csv`, `pandas`, etc.) is forbidden, not only in this lab, but in the course in general. Using them will result in a zero for that problem. Use `open`, `readline`, etc. instead.

While utilizing modules is not discouraged, the course is designed to teach you
programming basics. This requires from you a demonstration of an understanding of these basic concepts even when 
modules exist for simplifying these tasks. While modules can be very powerful, using them without really understanding 
them can lead to more trouble and confusion than they're worth. You will have plenty of time to experiment with modules
that are outside of the scope of this course after you complete CS1114.

As a rule, only use the material that you have learned in class up to this point and, if you're ever in doubt about
whether you can use something, ask!

### Important Note on Lab Collaboration

While discussion of the lab problems is allowed amongst students in the course, when it is time to implement your
solution, the code must be **entirely** your own work. Submitting code that has been written by someone other than
yourself will, at a minimum, result in receiving a 0 on the lab assignment. Other possible penalties include having
the incident reported to the Office of Student Affairs to be added to your official academic record and/or failing the
course.


---

### Problem 1: _(Probably) The Most Famous Computer Science Problem Ever_


One of the canonical problems in computer science is the word counter. As the name implies, it is a program that scans a
body of words (sometimes called a _corpus_), and returns a data structure that tells you how many times each word in
the corpus appears. We will be implementing a simple version of this program.


Write a function, **`get_word_counts()`**, that accepts `filepath` as a parameter (i.e. the name of the file we are 
going to scan), and returns a dictionary containing each word's frequency. Implement this function inside the file 
[**word_counter.py**](word_counter.py). Your program must function as follows :


```python
from pprint import pprint  # all this function does is print dictionaries nicely. You don't have to use it


def main():
  filepath = "lyrics.txt"
  word_counts = get_word_counts(filepath)


  pprint(word_counts)


main()
```
Output:
```text
{'a': 4,
'abide': 1,
'above': 1,
'abused': 1,
'all': 1,
'along': 1,
'always': 1,
'am': 1,
'and': 5,
'awake': 1,
'be': 1,
'bed': 1,
'beside': 1,
'breath': 1,
'bug': 3,
'but': 3,
'butterflies': 1,
'buzz': 1,
'by': 1,
'came': 2,
'can': 1,
'colors': 1,
'darling': 1,
'decides': 1,
'did': 1,
'die': 1,
'digest': 1,
'dissolve': 1,
"don't": 1,
'embrace,': 2,
'far': 1,
'final': 2,
'firm': 2,
'floor': 1,
'fluent': 1,
'flutter': 1,
'flytrap': 1,
'forest': 1,
'forever': 1,
'got': 1,
'haiku': 1,
'have': 1,
'head': 2,
'her': 4,
'hold': 1,
'i': 6,
"i'll": 3,
"i'm": 4,
'if': 1,
'in': 3,
'into': 1,
'it': 3,
'just': 5,
'lay': 2,
'leave': 1,
'lie': 2,
'like': 1,
'living': 1,
'love': 1,
'lying': 1,
'make': 1,
'me': 1,
'means': 1,
'mother': 2,
'my': 4,
'nature': 2,
'never': 1,
'no': 1,
'on': 1,
'out': 1,
'prisoners': 1,
'rest': 2,
'rule': 1,
'seduced': 1,
"she'll": 1,
'slowly': 1,
'stuck': 1,
'supposed': 1,
'take': 1,
'takes': 1,
'that': 1,
"that's": 2,
'the': 3,
'these': 1,
'to': 7,
'too': 1,
'venus': 1,
'walls': 1,
'we': 1,
'weekend': 1,
'what': 1,
'where': 1,
'why': 1,
"won't": 1,
'would': 2,
'you': 2,
"you'll": 1,
'yours': 1}
```

While the file [**lyrics.txt**](lyrics.txt) was used in this example, your function must work with any file of the 
expected format. We've included [**lyrics.txt**](lyrics.txt) for your convenience. (These, by the way, are the lyrics 
to a [**great song**](https://www.youtube.com/watch?v=x4llqoD2kq8) by the Dutch band _Feng Suave_.)

A few of things to keep in mind when working on this program:


1. First **attempt** to open the file that corresponds to the file name that was passed in to your
function. If the file name points to a file that does not exist, your program must return an empty dictionary. (_HINT_:
**`try`**, **`except`**, and **`FileNotFoundError`**).
2. Your program must be **case-insensitive**. That is, "Hello", "HELLO", and "hello" should be counted as the same word.
3. You may assume all words are separated by either a space or by a newline (`\n`).
4. You may assume that no punctuation will exist in the file.
5. You may assume contractions count as separate words (e.g. "I'm" is counted separately from the words "I am").
6. You may assume the file will contain words in English only.

Remember that we cannot possibly predict which words will appear in our corpus, as our program must work with any given
text. We, therefore, need a way to dynamically build our dictionary. Consider the following example where, instead of
wanting to get the frequency of each word, we want to get the frequency of each nucleotide in a DNA sequence:
```python
def get_nucleotide_frequencies(dna_strand_string):
   """
   Assumes only 'A', 'C', 'G', and 'T' will appear in dna_strand_string
   """
   frequencies = {}
   for nucleotide in dna_strand_string:
       # does this nucleotide exist as a key in our dictionary yet?
       if nucleotide not in frequencies:
           frequencies[nucleotide] = 1  # If not, this is our first time encountering this frequency
       else:
           frequencies[nucleotide] += 1  # If yes, this is a subsequent encounter
   return frequencies

def main():
   dna_strand = "ACGTCTT"
   frequencies = get_nucleotide_frequencies(dna_strand)
   print(frequencies)
main()
```
Output:
```text
{"A": 1, "C": 2, "G": 1, T: "3"}
```
How might we adapt this algorithm to our word counter?

### Problem 2: _Dictionaries, I Choose You!_

Back at it again with the _Pokémon_ problems. Problems 2 and 3 will be related to building a PokéDex which, in case you
have never seen the show or played the games, it is basically a dictionary (conveniently) where you can look up the
information of any Pokémon. Let's first focus on creating a single entry. In the file [**pokedex.py**](pokedex.py),
write a function **`create_entry()`**, that will accept the following parameters:


| **Parameter Name** | **Type** | **Notes**                                                                        |
|--------------------|----------|----------------------------------------------------------------------------------|
| `number`           | `int`  | Commonly abbreviated as simply `#`, denotes the ID number of this Pokémon.       |
| `name`             | `str`   |                                                                                  |
| `type_1`           | `str`   |                                                                                  |
| `type_2`           | `str`   | While all Pokémon have a `type_1`, not all Pokémon have a `type_2`. Be careful!  |
| `health_points`    | `int`  | Commonly abbreviated as `HP`.                                                    |
| `attack`           | `int`  |                                                                                  |
| `defense`          | `int`  |                                                                                  |
| `special_attack`   | `int`  | Commonly abbreviated as `Sp. Atk`.                                               |
| `special_defense`  | `int`  | Commonly abbreviated as `Sp. Def`.                                               |
| `speed`            | `int`  |                                                                                  |
| `generation`       | `int`  | Batches of Pokémon are released on a game-by-game basis, known as "Generations." |
| `is_legendary`     | `bool`     | There are special, usually very powerful, Pokémon called "Legendary Pokemon."    |


_**Figure 1**: Parameters of function **`create_entry()`**._


When these arguments are passed as parameters, a **`create_entry()`** function call  will create and return a
dictionary.


```python
def main():
  a_random_pokemon = create_entry(81, "Magnemite", "Electric", "Steel", 25, 35, 70, 95, 55, 45, 1, False)


  for key in a_random_pokemon.keys():
      print("{}: {}".format(key, a_random_pokemon[key]))


main()
```


Possible output for the program (since dictionary key-value pairs are unordered, the key-value pairs could be printed 
out in any order and still be correct):


```text
Number: 81
Name: Magnemite
Types: ('Electric', 'Steel')
Battle Stats: {'HP': 25, 'Attack': 35, 'Defense': 70, 'Sp. Atk': 95, 'Sp. Def': 55, 'Speed': 45}
Generation: 1
Legendary: False
```


A few of things to note when working on this problem:


- Notice that not all Pokémon will have a second type. If this is the case, you may assume `type_2` will be passed into
**`create_entry()`** as an **empty string** (`""`).
- Instead of having an individual key for both types, create a tuple containing both types, in order. If `type_2` is an
empty string, the second value  in the tuple should be **`None`** (the keyword, not a string).
- Also, notice that instead of creating an individual entry with each Pokémon's battle stat as a key, the key
`Battle Stats` maps to another dictionary containing them. The example output below demonstrates this dictionary 
structure:


```python
print(a_random_pokemon["Battle Stats"]) 
print(a_random_pokemon["Battle Stats"]["HP"])    
print(a_random_pokemon["Battle Stats"]["Attack"])
```
Output:
```text
{'HP': 25, 'Attack': 35, 'Defense': 70, 'Sp. Atk': 95, 'Sp. Def': 55, 'Speed': 45}
25
35
```


Writing a separate function to create this battle stats dictionary might be useful.


### Problem 3: Gotta Archive 'Em All!


Take a look at the file [**pokemon.csv**](pokemon.csv) that we've included in this lab:


```csv
#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
3,Venusaur,Grass,Poison,525,80,82,83,100,100,80,1,False
3,VenusaurMega Venusaur,Grass,Poison,625,80,100,123,122,120,80,1,False
4,Charmander,Fire,,309,39,52,43,60,50,65,1,False
```


| # | Name                  | Type 1 | Type 2 | Total | HP | Attack | Defense | Sp. Atk | Sp. Def | Speed | Generation | Legendary |
|---|-----------------------|--------|--------|-------|----|--------|---------|---------|---------|-------|------------|-----------|
| 1 | Bulbasaur             | Grass  | Poison | 318   | 45 | 49     | 49      | 65      | 65      | 45    | 1          | False     |
| 2 | Ivysaur               | Grass  | Poison | 405   | 60 | 62     | 63      | 80      | 80      | 60    | 1          | False     |
| 3 | Venusaur              | Grass  | Poison | 525   | 80 | 82     | 83      | 100     | 100     | 80    | 1          | False     |
| 3 | VenusaurMega Venusaur | Grass  | Poison | 625   | 80 | 100    | 123     | 122     | 120     | 80    | 1          | False     |
| 4 | Charmander            | Fire   |        | 309   | 39 | 52     | 43      | 60      | 50      | 65    | 1          | False     |


_**Figures 2 & 3**: File [**pokemon.csv**](pokemon.csv) and tabular representation. First 6 lines. Note `Venusaur` and
`VenusaurMega Venusaur` have the same number ID. This is permissible, and they should still be included as individual
Pokémon._


Write a function, **`create_pokedex()`**, that will accept one parameter, `filepath`, which represents the address of 
the CSV file that contains each Pokémon's information, such as [**pokemon.csv**](pokemon.csv). This function should 
also be implemented in the file [**pokedex.py**](pokedex.py).


Your program must:


1. First **attempt** to open the file that corresponds to the file name that was passed in to your
function. If the file name points to a file that does not exist, your program must return an empty dictionary. (_HINT_:
**`try`**, **`except`**, and **`FileNotFoundError`**).
2. Then, your program must create a Pokémon entry from every line inside the CSV file (using the function
**`create_entry()`** we created in problem 2). Once you create an entry, add it to the  PokéDex dictionary (that is,
just a regular Python dictionary that is initially empty), using the Pokémon's **name as the key**, and the **whole 
entry as the value**.
3. Once you have gone through every Pokémon in the file, return the PokéDex dictionary.


When **`create_pokedex()`** is implemented, your program will exhibit the following behavior:


```python
def main():
  filepath = "pokemon.csv"
  pokedex = create_pokedex(filepath)
  pokemon_key = "Glaceon"


  # This is one of the many ways to check if a certain key exists in a dictionary!
  try:
      # This step could potentially fail, so we "try" it first.
      my_favorite_pokemon = pokedex[pokemon_key]
  except KeyError:
      # If it does fail due to a KeyError, we'll print an error message.
      print("ERROR: Pokemon {} does not exist!".format(pokemon_key))
  else:
      # If it doesn't fail due to a KeyError, we'll print the Pokemon's info!
      print("PRINTING {}'S INFORMATION..." .format(pokemon_key))
      for key in my_favorite_pokemon.keys():
          print("{}: {}".format(key, my_favorite_pokemon[key]))


main()
```
Output:
```text
PRINTING Glaceon'S INFORMATION...
Number: 471
Name: Glaceon
Types: ('Ice', None)
Battle Stats: {'HP': 65, 'Attack': 60, 'Defense': 110, 'Sp. Atk': 130, 'Sp. Def': 95, 'Speed': 65}
Generation: 4
Legendary: False
```
If we changed the value of the variable `pokemon_key` to, say, `"Mikami"` (i.e. not a Pokémon), we'd instead see the 
following message printed onto our console:
```text
ERROR: Pokemon Mikami does not exist!
```