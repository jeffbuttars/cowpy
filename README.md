cowpy
=====

_This is a direct derivation of the cowsay program_

## Install

```sh
pip install cowpy
```

## What's the point? This is has been done, many times already.
Cowsay, in Python, makes pies. One file, easily embedded into your app.
It's directly executable and can be used on the CLI much like the original
Cowsay. Or it can be used as a Python module that is imported into a
Python program. It also has the option to copy itself so you can easily
distribute it embedded into your own package.

## Module Usage

## CLI Usage

The cowsay message is provided by `stdin` or as a command line parameter.

```sh
echo "my message" | cowpy
```
or
```sh
cowpy my message
```
    
CLI Arguments:

```sh
Output all available cowacters
cowpy --list
cowpy -l

Output all available cowacters and their variations.
cowpy --list-variations
cowpy -L

Use a thought bubble instead of a dialog bubble.
cowpy --thoughts
cowpy -t

Add a tounge to the selected cowacter,  if appropriate.
cowpy --tongue
cowpy -u 

Use a specifice type of eyes on the cowacter
cowpy --eyes
cowpy -e 

Specify which cowacter to use. (case insensitive)
cowpy --cowacter
cowpy -c 

Print a listing of the available eye types.
cowpy --list-eyes
cowpy -E 

Choose a cowacter at random.
cowpy --random
cowpy -r 

Create a local copy of cow.py for you to include in your own python program.
cowpy --copy
cowpy -C
```
