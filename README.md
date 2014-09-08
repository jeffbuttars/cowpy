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
    
    parser.add_argument('msg',
                        default= ["Cowsay | cowpy. Please seek --help"],
                        type=str, nargs='*',
                        help=("Message for the cow to say"),
                       )

    parser.add_argument('-l', '--list',
                        default=False,
                        help=("Output all available cowacters"),
                        action="store_true")
    parser.add_argument('-L', '--list-variations',
                        default=False,
                        help=("Output all available cowacters and their variations."),
                        action="store_true")
    parser.add_argument('-t', '--thoughts',
                        default=False,
                        help=("Use a thought bubble instead of a dialog bubble."),
                        action="store_true")
    parser.add_argument('-u', '--tongue',
                        default=False,
                        help=("Add a tounge to the selected cowacter,  if appropriate."),
                        action="store_true")
    parser.add_argument('-e', '--eyes',
                        default='default',
                        help=("Use a specifice type of eyes on the cowacter"))
    parser.add_argument('-c', '--cowacter',
                        default='default',
                        help=("Specify which cowacter to use. (case insensitive)"))
    parser.add_argument('-E', '--list-eyes',
                        help=("Print a listing of the available eye types."),
                        action="store_true")
    parser.add_argument('-r', '--random',
                        help=("Choose a cowacter at random."),
                        action="store_true")
    parser.add_argument('-C', '--copy',
                        help=("Create a local copy of cow.py for you to include in your own "
                              "python program."),
                        action="store_true")
