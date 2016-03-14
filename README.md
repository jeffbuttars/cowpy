cowpy
=====

_This is a direct derivation of the cowsay program_


[Install](#install)  
[Module Usage](#module-usage)  
[CLI Usage](#cli-usage)  
[Available Cowacters](#available-cowacters)    


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

```python
#!/usr/bin/env python
# encoding: utf-8

from cowpy import cow

# Create a Cow
cheese = cow.Moose()

# Get a cowsay message by milking the cow
msg = cheese.milk("My witty mesage")

# do something with the message
print(msg)

# Create a Cow with a thought bubble
cheese = cow.Moose(thoughts=True)
msg = cheese.milk("My witty mesage, with thought")
print(msg)

# Create a Cow with a tongue
cheese = cow.Moose(tongue=True)
msg = cheese.milk("My witty mesage, with tongue")
print(msg)

# Create a Cow with dead eyes
cheese = cow.Moose(eyes='dead')
msg = cheese.milk("my witty mesage, i'm dead")
print(msg)

# Get a cow by name
cow_cls = cow.get_cow('moose')
cheese = cow_cls()
msg = cheese.milk("Cow by name is moose")
print(msg)

# Create a Cow with a thought bubble, a tongue, and dead eyes
cheese = cow.Moose(thoughts=True, tongue=True, eyes='dead')
msg = cheese.milk("My witty mesage with several attributes")
print(msg)

# Create a random cow with a message
msg = cow.milk_random_cow("A random message for fun")
print(msg)

# all the eye options
eye_options = cow.eye_options()
print(eye_options)

# all the cowacter options
cow_options = cow.cow_options()
print(cow_options)
```

## CLI Usage

The cowsay message is provided by `stdin` or as a command line parameter.  
*NSFW* cows and eyes are not displayed in listings by default.

```sh
echo "my message" | cowpy
```
or
```sh
cowpy my message
```
    
CLI Arguments:

```
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

Enable NSFW cow output. (Use with --random, --list, --list-eyes and --list-available)
cowpy --nsfw
cowpy -x

Create a local copy of cow.py for you to include in your own python program.
cowpy --copy
cowpy -C
```

##Available Cowacters

```
 ________ 
< beavis >
 -------- 
   \         __------~~-,
    \      ,'            ,
          /               \
         /                :
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \ |
       (____\@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \________       |
                \      |
              __/-___-- -__
             /            _ \
 __________ 
< budfrogs >
 ---------- 
     \
      \
          oO)-.                       .-(Oo
         /__  _\                     /_  __\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '
 _______ 
< bunny >
 ------- 
  \
   \   \
        \ /\
        ( )
      .( o ).
 ________ 
< cheese >
 -------- 
   \
    \
      _____   _________
     /     \_/         |
    |                 ||
    |                 ||
   |    ###\  /###   | |
   |     0  \/  0    | |
  /|                 | |
 / |        <        |\ \
| /|                 | | |
| |     \_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\  /___\
 _______ 
< cower >
 ------- 
     \
      \
        ,__, |    | 
        (oo)\|    |___
        (__)\|    |   )\_
             |    |_w |  \
             |    |  ||   *

             Cower....
 ________ 
< daemon >
 -------- 
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/
 _________ 
< default >
 --------- 
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\
           ||----w |
           ||     ||
 ______________ 
< dragonandcow >
 -------------- 
             \                    ^    /^
              \                  / \  // \
               \   |\___/|      /   \//  .\
                \  /O  O  \__  /    //  | \ \           *----*
                  /     /  \/_/    //   |  \  \          \   |
                  \@___\@`    \/_   //    |   \   \         \/\ \
                 0/0/|       \/_ //     |    \    \         \ \
             0/0/0/0/|        \///      |     \     \       | |
          0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
       0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
                   ,-}        _      *-.|.-~-.           .~    ~
  \     \__/        `/\      /                 ~-. _ .-~      /
   \____(oo)           *.   }            {                   /
   (    (--)          .----~-.\        \-`                 .~
   //__\\  \__ Ack!   ///.----..<        \             _ -~
  //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~
 ______ 
< eyes >
 ------ 
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW\$\$\$ 
      :\$\$NWX!!:           .:!!!!!!XUWW\$\$\$\$\$\$\$\$\$P 
      \$\$\$\$\$##WX!:      .<!!!!UW\$\$\$\$"  \$\$\$\$\$\$\$\$#
      \$\$\$\$\$  \$\$\$UX   :!!UW\$\$\$\$\$\$\$\$\$   4\$\$\$\$\$\* 
      ^\$\$\$B  \$\$\$\$\     \$\$\$\$\$\$\$\$\$\$\$\$   d\$\$R
        "*\$bd\$\$\$\$      '*\$\$\$\$\$\$\$\$\$\$\$o+#" 
             """"          """"""" 

 ______________ 
< flamingsheep >
 -------------- 
  \            .    .     .   
   \      .  . .     `  ,     
    \    .; .  : .' :  :  : . 
     \   i..`: i` i.i.,i  i . 
      \   `,--.|i |i|ii|ii|i: 
           UooU\.'\@\@\@\@\@\@`.||' 
           \__/(\@\@\@\@\@\@\@\@\@\@)'  
                (\@\@\@\@\@\@\@\@)    
                `YY~~~~YY'    
                 ||    ||     
 ______________ 
< ghostbusters >
 -------------- 
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
 ____________ 
< hellokitty >
 ------------ 
  \
   \
      /\_)o<
     |      \
     | O . O|
      \_____/
 ______ 
< kiss >
 ------ 
     \
      \
             ,;;;;;;;,
            ;;;;;;;;;;;,
           ;;;;;'_____;'
           ;;;(/))))|((\
           _;;((((((|))))
          / |_\\\\\\\\\\\\
     .--~(  \ ~))))))))))))
    /     \  `\-(((((((((((\\
    |    | `\   ) |\       /|)
     |    |  `. _/  \_____/ |
      |    , `\~            /
       |    \  \           /
      | `.   `\|          /
      |   ~-   `\        /
       \____~._/~ -_,   (\
        |-----|\   \    ';;
       |      | :;;;'     \
      |  /    |            |
      |       |            |
 _______ 
< kitty >
 ------- 
     \
      \
       ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'
 _______ 
< koala >
 ------- 
  \
   \
       ___  
     {~._.~}
      ( Y )
     ()~*~()   
     (_)-(_)
 ______ 
< kosh >
 ------ 
    \
     \
      \
  ___       _____     ___
 /   \     /    /|   /   \
|     |   /    / |  |     |
|     |  /____/  |  |     |
|     |  |    |  |  |     |
|     |  | {} | /   |     |
|     |  |____|/    |     |
|     |    |==|     |     |
|      \___________/      |
|                         |
|                         |
 ___________ 
< lukekoala >
 ----------- 
  \
   \          .
       ___   //
     {~._.~}// 
      ( Y )K/  
     ()~*~()   
     (_)-(_)   
     Luke    
     Sywalker
     koala
 ____________ 
< mechandcow >
 ------------ 
                                   ,-----.
                                   |     |
                                ,--|     |-.
                         __,----|  |     | |
                       ,;::     |  `_____' |
                       `._______|    i^i   |
                                `----| |---'| .
                           ,-------._| |== ||//
                           |       |_|P`.  /'/
                           `-------' 'Y Y/'/'
                                     .==\ /_\
   ^__^                             /   /'|  `i
   (oo)\_______                   /'   /  |   |
   (__)\       )\/\             /'    /   |   `i
       ||----w |           ___,;`----'.___L_,-'`\__
       ||     ||          i_____;----\.____i""\____\
 ______ 
< meow >
 ------ 
  \
   \ ,   _ ___.--'''`--''//-,-_--_.
      \`"' ` || \\ \ \\/ / // / ,-\\`,_
     /'`  \ \ || Y  | \|/ / // / - |__ `-,
    /\@"\  ` \ `\ |  | ||/ // | \/  \  `-._`-,_.,
   /  _.-. `.-\,___/\ _/|_/_\_\/|_/ |     `-._._)
   `-'``/  /  |  // \__/\__  /  \__/ \
        `-'  /-\/  | -|   \__ \   |-' |
          __/\ / _/ \/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'
 ______ 
< milk >
 ------ 
 \     ____________ 
  \    |__________|
      /           /\
     /           /  \
    /___________/___/|
    |          |     |
    |  ==\ /== |     |
    |   O   O  | \ \ |
    |     <    |  \ \|
   /|          |   \ \
  / |  \_____/ |   / /
 / /|          |  / /|
/||\|          | /||\/
    -------------|   
        | |    | | 
       <__/    \__>
 _________ 
< moofasa >
 --------- 
       \    ____
        \  /    \
          | ^__^ |
          | (oo) |______
          | (__) |      )\/\
           \____/|----w |
                ||     ||

                Moofasa
 _______ 
< moose >
 ------- 
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
 ___________ 
< mutilated >
 ----------- 
       \   \_______
 v__v   \  \   O   )
 (oo)      ||----w |
 (__)      ||     ||  \/\
  
 _____ 
< ren >
 ----- 
   \
    \
    ____  
   /# /_\_
  |  |/o\o\
  |  \\_/_/
 / |_   |  
|  ||\_ ~| 
|  ||| \/  
|  |||_    
 \//  |    
  ||  |    
  ||_  \   
  \_|  o|  
  /\___/   
 /  ||||__ 
    (___)_)
 _________ 
< satanic >
 --------- 
     \
      \  (__)  
         (\/)  
  /-------\/    
 / | 666 ||    
*  ||----||      
   ~~    ~~
 _______ 
< sheep >
 ------- 
  \
   \
       __     
      UooU\.'\@\@\@\@\@\@`.
      \__/(\@\@\@\@\@\@\@\@\@\@)
           (\@\@\@\@\@\@\@\@)
           `YY~~~~YY'
            ||    ||
 __________ 
< skeleton >
 ---------- 
          \      (__)      
           \     /oo|  
            \   (_"_)*+++++++++*
                   //I#\\\\\\\\I\
                   I[I|I|||||I I `
                   I`I'///'' I I
                   I I       I I
                   ~ ~       ~ ~
                     Scowleton
 _______ 
< small >
 ------- 
       \   ,__,
        \  (oo)____
           (__)    )\
            ||--|| *
 __________ 
< squirrel >
 ---------- 
  \
     \
                  _ _
       | \__/|  .~    ~.
       /oo `./      .'
      {o__,   \    {
        / .  . )    \
        `-` '-' \    }
       .(   _(   )_.'
      '---.~_ _ _|
 _____________ 
< stegosaurus >
 ------------- 
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
 ________ 
< stimpy >
 -------- 
  \     .    _  .    
   \    |\_|/__/|    
       / / \/ \  \  
      /__|O||O|__ \ 
     |/_ \_/\_/ _\ |  
     | | (____) | ||  
     \/\___/\__/  // 
     (_/         ||
      |          ||
      |          ||\   
       \        //_/  
        \______//
       __ || __||
      (____(____)
 _____________ 
< supermilker >
 ------------- 
  \   ^__^
   \  (oo)\_______        ________
      (__)\       )\/\    |Super |
        ||----W |       |Milker|
          ||    UDDDDDDDDD|______|
 _________ 
< surgery >
 --------- 
          \           \  /
           \           \/
               (__)    /\
               (oo)   O  O
               _\/_   //
         *    (    ) //
          \  (\\    //
           \(  \\    )
            (   \\   )   /\
  ___[\______/^^^^^^^\__/) o-)__
 |\__[=======______//________)__\
 \|_______________//____________|
     |||      || //||     |||
     |||      || @.||     |||
      ||      \/  .\/      ||
                 . .
                '.'.`

            COW-OPERATION
 ___________ 
< threeeyes >
 ----------- 
        \  ^___^
         \ (ooo)\_______
           (___)\       )\/\
                ||----w |
                ||     ||
 ________ 
< turkey >
 -------- 
  \                                  ,+*^^*+___+++_
   \                           ,*^^^^              )
    \                       _+*                     ^**+_
     \                    +^       _ _++*+_+++_,         )
              _+^^*+_    (     ,+*^ ^          \+_        )
             {       )  (    ,(    ,_+--+--,      ^)      ^\
            { (\@)    } f   ,(  ,+-^ __*_*_  ^^\_   ^\       )
           {:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
          ( /  (    (        ,___    ^*+_+* )   <    <      \
           U _/     )    *--<  ) ^\-----++__)   )    )       )
            (      )  _(^)^^))  )  )\^^^^^))^*+/    /       /
          (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
         (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
          *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
          \             \_)^)_)) ))^^^^^^^^^^))^^^^)
           (_             ^\__^^^^^^^^^^^^))^^^^^^^)
             ^\___            ^\__^^^^^^))^^^^^^^^)\\
                  ^^^^^\uuu/^^\uuu/^^^^\^\^\^\^\^\^\^\
                     ___) >____) >___   ^\_\_\_\_\_\_\)
                    ^^^//\\_^^//\\_^       ^(\_\_\_\)
                      ^^^ ^^ ^^^ ^
 ________ 
< turtle >
 -------- 
    \                                  ___-------___
     \                             _-~~             ~~-_
      \                         _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /|  O|| O|        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)
 _____ 
< tux >
 ----- 
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
 _______ 
< udder >
 ------- 
  \
   \    (__)
        oo\
       ('') \---------
          \           \
           |          |\
           ||---(  )_|| *
           ||    UU  ||
           ==        ==
 _______ 
< vader >
 ------- 
        \    ,-^-.
         \   !oYo!
          \ /./=\.\______
               ##        )\/\
                ||-----w||
                ||      ||

               Cowth Vader
 ____________ 
< vaderkoala >
 ------------ 
   \
    \        .
     .---.  //
    Y|o o|Y// 
   /_(i=i)K/ 
   ~()~*~()~  
    (_)-(_)   

     Darth
     Vader
     koala
 _____ 
< www >
 ----- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
              ||--WWW |
                ||     ||
```
