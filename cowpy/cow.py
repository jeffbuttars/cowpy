#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

import logging

# Set up the logger
logger = logging.getLogger("cowpy")
# Use a console handler, set it to debug by default
logger_ch = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter(('%(levelname)s: %(asctime)s %(processName)s:%(process)d'
                                   ' %(filename)s:%(lineno)s %(module)s::%(funcName)s()'
                                   ' -- %(message)s'))
logger_ch.setFormatter(log_formatter)
logger.addHandler(logger_ch)

import sys
import os
import shutil
import argparse
import random


COWACTERS = {}
EYES = {
    'default': "oo",
    'borg': "==",
    'dead': "xx",
    'greedy': "$$",
    'paranoid': "@@",
    'stoned': "**",
    'tired': "--",
    'wired': "OO",
    'young': "..",
}
NOT_SAFE_FOR_WORK_COWACTERS = ['bongcow', 'sodomized', 'headincow', 'telebears']
NOT_SAFE_FOR_WORK_EYES = ['stoned']


def get_cowacters(sfw=True, sort=False):
    cows = COWACTERS
    if sfw:
        ckeys = set(COWACTERS.keys()) - set(NOT_SAFE_FOR_WORK_COWACTERS)
        cows = dict([(k, cows[k]) for k in ckeys])

    if sort:
        return sorted(cows.items(), key=lambda x: x[0])

    return cows.items()


def get_eyes(sfw=True, sort=False):
    eyes = EYES
    if sfw:
        ekeys = set(EYES.keys()) - set(NOT_SAFE_FOR_WORK_EYES)
        eyes = dict([(k, eyes[k]) for k in ekeys])

    if sort:
        return sorted(eyes.items(), key=lambda x: x[0])

    return eyes.items()


def not_safe_for_work(cow='', eyes=''):
    return (cow in NOT_SAFE_FOR_WORK_COWACTERS) \
            or (eyes in NOT_SAFE_FOR_WORK_EYES)


class Cowacter(object):
    """Docstring for Cowacter """

    def __init__(self, eyes='default', thoughts=False, tongue=False,
                 body=None):

        self._eye_type = eyes
        self._eyes = EYES.get(eyes, 'default')
        self._thoughts = '\\'
        if thoughts:
            self._thoughts = 'o'
        self._tongue = ''
        if tongue:
            self._tongue = 'U '

        self._body = body or ("     {thoughts}   ^__^\n"
                              "      {thoughts}  ({eyes})\\_______\n"
                              "         (__)\\       )\\/\\\n"
                              "          {tongue} ||----w |\n"
                              "           ||     ||")

    def _bubble(self, message):
        lines = message.splitlines()
        content_len = max(len(line) for line in lines)
        border_len = content_len + 2
        fmt = "{0} {1} {2}\n"
        res = ""

        # Try to kick out just the balloon first.
        res += " {0} \n".format('_' * border_len)

        if len(lines) > 1:
            res += fmt.format('/', lines[0].ljust(content_len), '\\')
            for i in range(1, len(lines) - 1):
                res += fmt.format('|', lines[i].ljust(content_len), '|')
            res += fmt.format('\\', lines[-1].ljust(content_len), '/')
        else:
            res += fmt.format('<', lines[0].ljust(content_len), '>')

        res += " {0} \n".format('-' * border_len)
        return res

    def milk(self, msg):
        msg = msg.strip()

        if not msg:
            msg = "{0}, eyes:{1}, tongue:{2}, thoughts:{3}".format(
                self.__class__.__name__,
                self._eye_type,
                bool(self._tongue),
                self._thoughts != "\\",
            )

        try:
            res = self._bubble(msg)
            return res + self._body.format(thoughts=self._thoughts,
                                           eyes=self._eyes,
                                           tongue=self._tongue)
        except Exception as e:
            return "Unable to print the message :(\n{0}".format(e)


COWACTERS['default'] = Cowacter


class Beavis(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}         __------~~-,\n"
            "    {thoughts}      ,'            ,\n"
            "          /               \\\n"
            "         /                :\n"
            "        |                  '\n"
            "        |                  |\n"
            "        |                  |\n"
            "         |   _--           |\n"
            "         _| =-.     .-.   ||\n"
            "         o|/o/       _.   |\n"
            "         /  ~          \\ |\n"
            "       (____\@)  ___~    |\n"
            "          |_===~~~.`    |\n"
            "       _______.--~     |\n"
            "       \\________       |\n"
            "                \\      |\n"
            "              __/-___-- -__\n"
            "             /            _ \\")

        super(Beavis, self).__init__(**kwargs)


COWACTERS['beavis'] = Beavis


class BongCow(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "         {thoughts}\n"
            "          {thoughts}\n"
            "            ^__^\n"
            "    _______/({eyes})\n"
            "/\\/(       /(__)\n"
            "   | W----|| |~|\n"
            "   ||     || |~|  ~~\n"
            "             |~|  ~\n"
            "             |_| o\n"
            "             |#|/\n"
            "            _+#+_\n")

        super(BongCow, self).__init__(**kwargs)


COWACTERS['bongcow'] = BongCow


class BudFrogs(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "     {thoughts}\n"
            "      {thoughts}\n"
            "          oO)-.                       .-(Oo\n"
            "         /__  _\\                     /_  __\\\n"
            "         \\  \\(  |     ()~()         |  )/  /\n"
            "          \\__|\\ |    (-___-)        | /|__/\n"
            "          '  '--'    ==`-'==        '--'  '")
        super(BudFrogs, self).__init__(**kwargs)


COWACTERS['budfrogs'] = BudFrogs


class Bunny(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}   \\\n"
            "        \\ /\\\n"
            "        ( )\n"
            "      .( o ).")
        super(Bunny, self).__init__(**kwargs)


COWACTERS['bunny'] = Bunny


class Cheese(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}\n"
            "    {thoughts}\n"
            "      _____   _________\n"
            "     /     \\_/         |\n"
            "    |                 ||\n"
            "    |                 ||\n"
            "   |    ###\\  /###   | |\n"
            "   |     0  \\/  0    | |\n"
            "  /|                 | |\n"
            " / |        <        |\\ \\\n"
            "| /|                 | | |\n"
            "| |     \\_______/   |  | |\n"
            "| |                 | / /\n"
            "/||                 /|||\n"
            "   ----------------|\n"
            "        | |    | |\n"
            "        ***    ***\n"
            "       /___\\  /___\\")
        super(Cheese, self).__init__(**kwargs)


COWACTERS['cheese'] = Cheese


class Cower(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "     {thoughts}\n"
            "      {thoughts}\n"
            "        ,__, |    | \n"
            "        (oo)\\|    |___\n"
            "        (__)\\|    |   )\\_\n"
            "             |    |_w |  \\\n"
            "             |    |  ||   *\n"
            "\n"
            "             Cower....")
        super(Cower, self).__init__(**kwargs)


COWACTERS['cower'] = Cower


class Daemon(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}         ,        ,\n"
            "    {thoughts}       /(        )`\n"
            "     {thoughts}      \\ \\___   / |\n"
            "            /- _  `-/  '\n"
            "           (/\\/ \\ \\   /\\\n"
            "           / /   | `    \\\n"
            "           O O   ) /    |\n"
            "           `-^--'`<     '\n"
            "          (_.)  _  )   /\n"
            "           `.___/`    /\n"
            "             `-----' /\n"
            "<----.     __ / __   \\\n"
            "<----|====O)))==) \\) /====\n"
            "<----'    `--' `.__,' \\\n"
            "             |        |\n"
            "              \\       /\n"
            "        ______( (_  / \\______\n"
            "      ,'  ,-----'   |        \\\n"
            "      `--{{__________)        \\/")
        super(Daemon, self).__init__(**kwargs)


COWACTERS['daemon'] = Daemon


class DragonAndCow(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
                "             {thoughts}                    ^    /^\n"
                "              {thoughts}                  / \\  // \\\n"
                "               {thoughts}   |\\___/|      /   \\//  .\\\n"
                "                {thoughts}  /O  O  \\__  /    //  | \\ \\           *----*\n"
                "                  /     /  \\/_/    //   |  \\  \\          \\   |\n"
                "                  \@___\@`    \\/_   //    |   \\   \\         \\/\\ \\\n"
                "                 0/0/|       \\/_ //     |    \\    \\         \\ \\\n"
                "             0/0/0/0/|        \\///      |     \\     \\       | |\n"
                "          0/0/0/0/0/_|_ /   (  //       |      \\     _\\     |  /\n"
                "       0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\\.-~       /   /\n"
                "                   ,-}}        _      *-.|.-~-.           .~    ~\n"
                "  \\     \\__/        `/\\      /                 ~-. _ .-~      /\n"
                "   \\____({eyes})           *.   }}            {{                   /\n"
                "   (    (--)          .----~-.\\        \\-`                 .~\n"
                "   //__\\\\  \\__ Ack!   ///.----..<        \\             _ -~\n"
                "  //    \\\\               ///-._ _ _ _ _ _ _{{^ - - - - ~")
        super(DragonAndCow, self).__init__(**kwargs)


COWACTERS['dragonandcow'] = DragonAndCow


class Eyes(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "    {thoughts}\n"
            "     {thoughts}\n"
            "                                   .::!!!!!!!:.\n"
            "  .!!!!!:.                        .:!!!!!!!!!!!!\n"
            "  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW\$\$\$ \n"
            "      :\$\$NWX!!:           .:!!!!!!XUWW\$\$\$\$\$\$\$\$\$P \n"
            "      \$\$\$\$\$##WX!:      .<!!!!UW\$\$\$\$\"  \$\$\$\$\$\$\$\$#\n"
            "      \$\$\$\$\$  \$\$\$UX   :!!UW\$\$\$\$\$\$\$\$\$   4\$\$\$\$\$\* \n"
            "      ^\$\$\$B  \$\$\$\$\\     \$\$\$\$\$\$\$\$\$\$\$\$   d\$\$R\n"
            "        \"*\$bd\$\$\$\$      '*\$\$\$\$\$\$\$\$\$\$\$o+#\" \n"
            "             \"\"\"\"          \"\"\"\"\"\"\" \n")
        super(Eyes, self).__init__(**kwargs)


COWACTERS['eyes'] = Eyes


class FlamingSheep(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}            .    .     .   \n"
            "   {thoughts}      .  . .     `  ,     \n"
            "    {thoughts}    .; .  : .' :  :  : . \n"
            "     {thoughts}   i..`: i` i.i.,i  i . \n"
            "      {thoughts}   `,--.|i |i|ii|ii|i: \n"
            "           U{eyes}U\\.'\@\@\@\@\@\@`.||' \n"
            "           \\__/(\@\@\@\@\@\@\@\@\@\@)'  \n"
            "                (\@\@\@\@\@\@\@\@)    \n"
            "                `YY~~~~YY'    \n"
            "                 ||    ||     ")
        super(FlamingSheep, self).__init__(**kwargs)


COWACTERS['flamingsheep'] = FlamingSheep


class Ghostbusters(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "          {thoughts}\n"
            "           {thoughts}\n"
            "            {thoughts}          __---__\n"
            "                    _-       /--______\n"
            "               __--( /     \\ )XXXXXXXXXXX\\v.\n"
            "             .-XXX(   O   O  )XXXXXXXXXXXXXXX-\n"
            "            /XXX(       U     )        XXXXXXX\\\n"
            "          /XXXXX(              )--_  XXXXXXXXXXX\\\n"
            "         /XXXXX/ (      O     )   XXXXXX   \\XXXXX\\\n"
            "         XXXXX/   /            XXXXXX   \\__ \\XXXXX\n"
            "         XXXXXX__/          XXXXXX         \\__---->\n"
            " ---___  XXX__/          XXXXXX      \\__         /\n"
            "   \\-  --__/   ___/\\  XXXXXX            /  ___--/=\n"
            "    \\-\\    ___/    XXXXXX              '--- XXXXXX\n"
            "       \\-\\/XXX\\ XXXXXX                      /XXXXX\n"
            "         \\XXXXXXXXX   \\                    /XXXXX/\n"
            "          \\XXXXXX      >                 _/XXXXX/\n"
            "            \\XXXXX--__/              __-- XXXX/\n"
            "             -XXXXXXXX---------------  XXXXXX-\n"
            "                \\XXXXXXXXXXXXXXXXXXXXXXXXXX/\n"
            "                  \"\"VXXXXXXXXXXXXXXXXXXV\"\"")
        super(Ghostbusters, self).__init__(**kwargs)


COWACTERS['ghostbusters'] = Ghostbusters


class HeadInCow(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "    {thoughts}\n"
            "     {thoughts}\n"
            "    ^__^         /\n"
            "    ({eyes})\\_______/  _________\n"
            "    (__)\\       )=(  ____|_ \\_____\n"
            "   {tongue}   ||----w |  \\ \\     \\_____ |\n"
            "        ||     ||   ||           ||")
        super(HeadInCow, self).__init__(**kwargs)


COWACTERS['headincow'] = HeadInCow


class HelloKitty(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}\n"
            "      /\\_)o<\n"
            "     |      \\\n"
            "     | O . O|\n"
            "      \\_____/")
        super(HelloKitty, self).__init__(**kwargs)


COWACTERS['hellokitty'] = HelloKitty


class Kiss(Cowacter):

    def __init__(self, **kwargs):
        kwargs['body'] = (
            "     {thoughts}\n"
            "      {thoughts}\n"
            "             ,;;;;;;;,\n"
            "            ;;;;;;;;;;;,\n"
            "           ;;;;;'_____;'\n"
            "           ;;;(/))))|((\\\n"
            "           _;;((((((|))))\n"
            "          / |_\\\\\\\\\\\\\\\\\\\\\\\\\n"
            "     .--~(  \\ ~))))))))))))\n"
            "    /     \\  `\\-(((((((((((\\\\\n"
            "    |    | `\\   ) |\\       /|)\n"
            "     |    |  `. _/  \\_____/ |\n"
            "      |    , `\\~            /\n"
            "       |    \\  \\           /\n"
            "      | `.   `\\|          /\n"
            "      |   ~-   `\\        /\n"
            "       \\____~._/~ -_,   (\\\n"
            "        |-----|\\   \\    ';;\n"
            "       |      | :;;;'     \\\n"
            "      |  /    |            |\n"
            "      |       |            |")
        super(Kiss, self).__init__(**kwargs)


COWACTERS['kiss'] = Kiss


class Kitty(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "     {thoughts}\n"
            "      {thoughts}\n"
            "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
            "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
            "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
            "      _.. `--'_..-_/   /--' _ .' ,4\n"
            "   ( i l ),-''  ( l i),'  ( ( ! .-'")
        super(Kitty, self).__init__(**kwargs)


COWACTERS['kitty'] = Kitty


class Koala(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}\n"
            "       ___  \n"
            "     {{~._.~}}\n"
            "      ( Y )\n"
            "     ()~*~()   \n"
            "     (_)-(_)")
        super(Koala, self).__init__(**kwargs)


COWACTERS['koala'] = Koala


class Koala(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}\n"
            "       ___  \n"
            "     {{~._.~}}\n"
            "      ( Y )\n"
            "     ()~*~()   \n"
            "     (_)-(_)")
        super(Koala, self).__init__(**kwargs)


COWACTERS['koala'] = Koala


class Kosh(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "    {thoughts}\n"
            "     {thoughts}\n"
            "      {thoughts}\n"
            "  ___       _____     ___\n"
            " /   \\     /    /|   /   \\\n"
            "|     |   /    / |  |     |\n"
            "|     |  /____/  |  |     |\n"
            "|     |  |    |  |  |     |\n"
            "|     |  | {{}} | /   |     |\n"
            "|     |  |____|/    |     |\n"
            "|     |    |==|     |     |\n"
            "|      \\___________/      |\n"
            "|                         |\n"
            "|                         |")
        super(Kosh, self).__init__(**kwargs)


COWACTERS['kosh'] = Kosh


class LukeKoala(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}          .\n"
            "       ___   //\n"
            "     {{~._.~}}// \n"
            "      ( Y )K/  \n"
            "     ()~*~()   \n"
            "     (_)-(_)   \n"
            "     Luke    \n"
            "     Sywalker\n"
            "     koala")
        super(LukeKoala, self).__init__(**kwargs)


COWACTERS['lukekoala'] = LukeKoala


class MechAndCow(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "                                   ,-----.\n"
            "                                   |     |\n"
            "                                ,--|     |-.\n"
            "                         __,----|  |     | |\n"
            "                       ,;::     |  `_____' |\n"
            "                       `._______|    i^i   |\n"
            "                                `----| |---'| .\n"
            "                           ,-------._| |== ||//\n"
            "                           |       |_|P`.  /'/\n"
            "                           `-------' 'Y Y/'/'\n"
            "                                     .==\ /_\\\n"
            "   ^__^                             /   /'|  `i\n"
            "   (oo)\_______                   /'   /  |   |\n"
            "   (__)\       )\/\             /'    /   |   `i\n"
            "       ||----w |           ___,;`----'.___L_,-'`\__\n"
            "       ||     ||          i_____;----\.____i\"\"\____\\")
        super(MechAndCow, self).__init__(**kwargs)


COWACTERS['mechandcow'] = MechAndCow


class Meow(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts} ,   _ ___.--'''`--''//-,-_--_.\n"
            "      \\`\"' ` || \\\\ \\ \\\\/ / // / ,-\\\\`,_\n"
            "     /'`  \\ \\ || Y  | \\|/ / // / - |__ `-,\n"
            "    /\@\"\\  ` \\ `\\ |  | ||/ // | \\/  \\  `-._`-,_.,\n"
            "   /  _.-. `.-\\,___/\\ _/|_/_\\_\\/|_/ |     `-._._)\n"
            "   `-'``/  /  |  // \\__/\\__  /  \\__/ \\\n"
            "        `-'  /-\\/  | -|   \\__ \\   |-' |\n"
            "          __/\\ / _/ \\/ __,-'   ) ,' _|'\n"
            "         (((__/(((_.' ((___..-'((__,'")
        super(Meow, self).__init__(**kwargs)


COWACTERS['meow'] = Meow


class Milk(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            " {thoughts}     ____________ \n"
            "  {thoughts}    |__________|\n"
            "      /           /\\\n"
            "     /           /  \\\n"
            "    /___________/___/|\n"
            "    |          |     |\n"
            "    |  ==\\ /== |     |\n"
            "    |   O   O  | \\ \\ |\n"
            "    |     <    |  \\ \\|\n"
            "   /|          |   \\ \\\n"
            "  / |  \\_____/ |   / /\n"
            " / /|          |  / /|\n"
            "/||\\|          | /||\\/\n"
            "    -------------|   \n"
            "        | |    | | \n"
            "       <__/    \\__>")
        super(Milk, self).__init__(**kwargs)


COWACTERS['milk'] = Milk


class Moofasa(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "       {thoughts}    ____\n"
            "        {thoughts}  /    \\\n"
            "          | ^__^ |\n"
            "          | ({eyes}) |______\n"
            "          | (__) |      )\\/\\\n"
            "           \\____/|----w |\n"
            "                ||     ||\n"
            "\n"
            "                Moofasa")
        super(Moofasa, self).__init__(**kwargs)


COWACTERS['moofasa'] = Moofasa


class Moose(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}   \\_\\_    _/_/\n"
            "    {thoughts}      \\__/\n"
            "           ({eyes})\\_______\n"
            "           (__)\\       )\\/\\\n"
            "            {tongue}   ||----w |\n"
            "               ||     ||")
        super(Moose, self).__init__(**kwargs)


COWACTERS['moose'] = Moose


class Mutilated(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "       {thoughts}   \\_______\n"
            " v__v   {thoughts}  \\   O   )\n"
            " ({eyes})      ||----w |\n"
            " (__)      ||     ||  \\/\\\n"
            "  {tongue}")
        super(Mutilated, self).__init__(**kwargs)


COWACTERS['mutilated'] = Mutilated


class Ren(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}\n"
            "    {thoughts}\n"
            "    ____  \n"
            "   /# /_\\_\n"
            "  |  |/o\\o\\\n"
            "  |  \\\\_/_/\n"
            " / |_   |  \n"
            "|  ||\\_ ~| \n"
            "|  ||| \\/  \n"
            "|  |||_    \n"
            " \\//  |    \n"
            "  ||  |    \n"
            "  ||_  \\   \n"
            "  \\_|  o|  \n"
            "  /\\___/   \n"
            " /  ||||__ \n"
            "    (___)_)")
        super(Ren, self).__init__(**kwargs)


COWACTERS['ren'] = Ren


class Satanic(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "     {thoughts}\n"
            "      {thoughts}  (__)  \n"
            "         (\\/)  \n"
            "  /-------\\/    \n"
            " / | 666 ||    \n"
            "*  ||----||      \n"
            "   ~~    ~~")
        super(Satanic, self).__init__(**kwargs)


COWACTERS['satanic'] = Satanic


class Sheep(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}\n"
            "       __     \n"
            "      U{eyes}U\\.'\@\@\@\@\@\@`.\n"
            "      \\__/(\@\@\@\@\@\@\@\@\@\@)\n"
            "           (\@\@\@\@\@\@\@\@)\n"
            "           `YY~~~~YY'\n"
            "            ||    ||")
        super(Sheep, self).__init__(**kwargs)


COWACTERS['sheep'] = Sheep


class Skeleton(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "          {thoughts}      (__)      \n"
            "           {thoughts}     /{eyes}|  \n"
            "            {thoughts}   (_\"_)*+++++++++*\n"
            "                   //I#\\\\\\\\\\\\\\\\I\\\n"
            "                   I[I|I|||||I I `\n"
            "                   I`I'///'' I I\n"
            "                   I I       I I\n"
            "                   ~ ~       ~ ~\n"
            "                     Scowleton")
        super(Skeleton, self).__init__(**kwargs)


COWACTERS['skeleton'] = Skeleton


class Small(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "       {thoughts}   ,__,\n"
            "        {thoughts}  ({eyes})____\n"
            "           (__)    )\\\n"
            "            {tongue}||--|| *")
        super(Small, self).__init__(**kwargs)


COWACTERS['small'] = Small


class Sodomized(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "      {thoughts}                _\n"
            "       {thoughts}              (_)\n"
            "        {thoughts}   ^__^       / \\\n"
            "         {thoughts}  ({eyes})\\_____/_\\ \\\n"
            "            (__)\\       ) /\n"
            "             {tongue} ||----w ((\n"
            "                ||     ||>> ")
        super(Sodomized, self).__init__(**kwargs)


COWACTERS['sodomized'] = Sodomized


class Squirrel(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "     {thoughts}\n"
            "                  _ _\n"
            "       | \__/|  .~    ~.\n"
            "       /{eyes} `./      .'\n"
            "      {{o__,   \    {{\n"
            "        / .  . )    \\\n"
            "        `-` '-' \    }}\n"
            "       .(   _(   )_.'\n"
            "      '---.~_ _ _|")
        super(Squirrel, self).__init__(**kwargs)


COWACTERS['squirrel'] = Squirrel


class Stegosaurus(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "{thoughts}                             .       .\n"
            " {thoughts}                           / `.   .' \" \n"
            "  {thoughts}                  .---.  <    > <    >  .---.\n"
            "   {thoughts}                 |    \\  \\ - ~ ~ - /  /    |\n"
            "         _____          ..-~             ~-..-~\n"
            "        |     |   \\~~~\\.'                    `./~~~/\n"
            "       ---------   \\__/                        \\__/\n"
            "      .'  O    \\     /               /       \\  \" \n"
            "     (_____,    `._.'               |         }}  \\/~~~/\n"
            "      `----.          /       }}     |        /    \\__/\n"
            "            `-.      |       /      |       /      `. ,~~|\n"
            "                ~-.__|      /_ - ~ ^|      /- _      `..-'   \n"
            "                     |     /        |     /     ~-.     `-. _  _  _\n"
            "                     |_____|        |_____|         ~ - . _ _ _ _ _>")
        super(Stegosaurus, self).__init__(**kwargs)


COWACTERS['stegosaurus'] = Stegosaurus


class Stimpy(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}     .    _  .    \n"
            "   {thoughts}    |\\_|/__/|    \n"
            "       / / \\/ \\  \\  \n"
            "      /__|O||O|__ \\ \n"
            "     |/_ \\_/\\_/ _\\ |  \n"
            "     | | (____) | ||  \n"
            "     \\/\\___/\\__/  // \n"
            "     (_/         ||\n"
            "      |          ||\n"
            "      |          ||\\   \n"
            "       \\        //_/  \n"
            "        \\______//\n"
            "       __ || __||\n"
            "      (____(____)")
        super(Stimpy, self).__init__(**kwargs)


COWACTERS['stimpy'] = Stimpy


class Supermilker(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}   ^__^\n"
            "   {thoughts}  ({eyes})\\_______        ________\n"
            "      (__)\\       )\\/\\    |Super |\n"
            "       {tongue} ||----W |       |Milker|\n"
            "          ||    UDDDDDDDDD|______|")
        super(Supermilker, self).__init__(**kwargs)

#Su
COWACTERS['supermilker'] = Supermilker


class Surgery(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "          {thoughts}           \\  /\n"
            "           {thoughts}           \\/\n"
            "               (__)    /\\\n"
            "               ({eyes})   O  O\n"
            "               _\\/_   //\n"
            "         *    (    ) //\n"
            "          \\  (\\\\    //\n"
            "           \\(  \\\\    )\n"
            "            (   \\\\   )   /\\\n"
            "  ___[\\______/^^^^^^^\\__/) o-)__\n"
            " |\\__[=======______//________)__\\\n"
            " \\|_______________//____________|\n"
            "     |||      || //||     |||\n"
            "     |||      || @.||     |||\n"
            "      ||      \\/  .\\/      ||\n"
            "                 . .\n"
            "                '.'.`\n"
            "\n"
            "            COW-OPERATION")
        super(Surgery, self).__init__(**kwargs)


COWACTERS['surgery'] = Surgery


class Telebears(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "      {thoughts}                _\n"
            "       {thoughts}              (_)   <-- TeleBEARS\n"
            "        {thoughts}   ^__^       / \\\n"
            "         {thoughts}  ({eyes})\\_____/_\\ \\\n"
            "            (__)\\  you  ) /\n"
            "             {tongue} ||----w ((\n"
            "                ||     ||>>")
        super(Telebears, self).__init__(**kwargs)


COWACTERS['telebears'] = Telebears


class ThreeEyes(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "        {thoughts}  ^___^\n"
            "         {thoughts} ({eyes})\\_______\n"
            "           (___)\\       )\\/\\\n"
            "            {tongue}    ||----w |\n"
            "                ||     ||")
        super(ThreeEyes, self).__init__(**kwargs)
        self._eyes = self._eyes[0] * 3


COWACTERS['threeeyes'] = ThreeEyes


class Turkey(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}                                  ,+*^^*+___+++_\n"
            "   {thoughts}                           ,*^^^^              )\n"
            "    {thoughts}                       _+*                     ^**+_\n"
            "     {thoughts}                    +^       _ _++*+_+++_,         )\n"
            "              _+^^*+_    (     ,+*^ ^          \\+_        )\n"
            "             {{       )  (    ,(    ,_+--+--,      ^)      ^\\\n"
            "            {{ (\@)    }} f   ,(  ,+-^ __*_*_  ^^\\_   ^\\       )\n"
            "           {{:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /\n"
            "          ( /  (    (        ,___    ^*+_+* )   <    <      \\\n"
            "           U _/     )    *--<  ) ^\\-----++__)   )    )       )\n"
            "            (      )  _(^)^^))  )  )\\^^^^^))^*+/    /       /\n"
            "          (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^\n"
            "         (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)\n"
            "          *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^\n"
            "          \\             \\_)^)_)) ))^^^^^^^^^^))^^^^)\n"
            "           (_             ^\\__^^^^^^^^^^^^))^^^^^^^)\n"
            "             ^\\___            ^\\__^^^^^^))^^^^^^^^)\\\\\n"
            "                  ^^^^^\\uuu/^^\\uuu/^^^^\\^\\^\\^\\^\\^\\^\\^\\\n"
            "                     ___) >____) >___   ^\\_\\_\\_\\_\\_\\_\\)\n"
            "                    ^^^//\\\\_^^//\\\\_^       ^(\\_\\_\\_\\)\n"
            "                      ^^^ ^^ ^^^ ^")
        super(Turkey, self).__init__(**kwargs)


COWACTERS['turkey'] = Turkey


class Turtle(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "    {thoughts}                                  ___-------___\n"
            "     {thoughts}                             _-~~             ~~-_\n"
            "      {thoughts}                         _-~                    /~-_\n"
            "             /^\\__/^\\         /~  \\                   /    \\\n"
            "           /|  O|| O|        /      \\_______________/        \\\n"
            "          | |___||__|      /       /                \\          \\\n"
            "          |          \\    /      /                    \\          \\\n"
            "          |   (_______) /______/                        \\_________ \\\n"
            "          |         / /         \\                      /            \\\n"
            "           \\         \\^\\\\         \\                  /               \\     /\n"
            "             \\         ||           \\______________/      _-_       //\\__//\n"
            "               \\       ||------_-~~-_ ------------- \\ --/~   ~\\    || __/\n"
            "                 ~-----||====/~     |==================|       |/~~~~~\n"
            "                  (_(__/  ./     /                    \\_\\      \\.\n"
            "                         (_(___/                         \\_____)_)")
        super(Turtle, self).__init__(**kwargs)


COWACTERS['turtle'] = Turtle


class Tux(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}\n"
            "    {thoughts}\n"
            "        .--.\n"
            "       |o_o |\n"
            "       |:_/ |\n"
            "      //   \\ \\\n"
            "     (|     | )\n"
            "    /'\\_   _/`\\\n"
            "    \\___)=(___/")
        super(Tux, self).__init__(**kwargs)


COWACTERS['tux'] = Tux


class Udder(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "  {thoughts}\n"
            "   {thoughts}    (__)\n"
            "        {eyes}\\\n"
            "       ('') \\---------\n"
            "        {tongue}  \\           \\\n"
            "           |          |\\\n"
            "           ||---(  )_|| *\n"
            "           ||    UU  ||\n"
            "           ==        ==")
        super(Udder, self).__init__(**kwargs)


COWACTERS['udder'] = Udder


class VaderKoala(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "   {thoughts}\n"
            "    {thoughts}        .\n"
            "     .---.  //\n"
            "    Y|o o|Y// \n"
            "   /_(i=i)K/ \n"
            "   ~()~*~()~  \n"
            "    (_)-(_)   \n"
            "\n"
            "     Darth\n"
            "     Vader\n"
            "     koala")
        super(VaderKoala, self).__init__(**kwargs)


COWACTERS['vaderkoala'] = VaderKoala


class Vader(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "        {thoughts}    ,-^-.\n"
            "         {thoughts}   !oYo!\n"
            "          {thoughts} /./=\\.\\______\n"
            "               ##        )\\/\\\n"
            "                ||-----w||\n"
            "                ||      ||\n"
            "\n"
            "               Cowth Vader")
        super(Vader, self).__init__(**kwargs)


COWACTERS['vader'] = Vader


class www(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            "        {thoughts}   ^__^\n"
            "         {thoughts}  ({eyes})\\_______\n"
            "            (__)\\       )\\/\\\n"
            "             {tongue} ||--WWW |\n"
            "                ||     ||")
        super(www, self).__init__(**kwargs)


COWACTERS['www'] = www


class Stegosaurus(Cowacter):
    def __init__(self, **kwargs):
        kwargs['body'] = (
            '''{thoughts}                             .       .\n'''
            ''' {thoughts}                           / `.   .' " \n'''
            '''  {thoughts}                  .---.  <    > <    >  .---.\n'''
            '''   {thoughts}                 |    \\  \\ - ~ ~ - /  /    |\n'''
            '''         _____          ..-~             ~-..-~\n'''
            '''        |     |   \\~~~\\.'                    `./~~~/\n'''
            '''       ---------   \\__/                        \\__/\n'''
            '''      .'  O    \\     /               /       \\  " \n'''
            '''     (_____,    `._.'               |         }}  \\/~~~/\n'''
            '''      `----.          /       }}     |        /    \\__/\n'''
            '''            `-.      |       /      |       /      `. ,~~|\n'''
            '''                ~-.__|      /_ - ~ ^|      /- _      `..-'   \n'''
            '''                     |     /        |     /     ~-.     `-. _  _  _\n'''
            '''                     |_____|        |_____|         ~ - . _ _ _ _ _>'''
        )
        super(Stegosaurus, self).__init__(**kwargs)
#stegosaurus
COWACTERS['stegosaurus'] = Stegosaurus


def get_cow(name='default'):
    return COWACTERS.get(name, 'default')


def eye_options():
    return EYES.keys()


def cow_options():
    return COWACTERS.keys()


def milk_random_cow(msg, sfw=True):
    cowacter = random.choice([x[0] for x in get_cowacters(sfw=sfw)])
    eyes = random.choice([x[0] for x in get_eyes(sfw=sfw)])

    cow = COWACTERS[cowacter]

    return cow(eyes=eyes,
               tongue=random.choice((True, False)),
               thoughts=random.choice((True, False))
               ).milk(msg)


def main():
    logger.debug("main")

    parser = argparse.ArgumentParser(
        prog="cowpy",
        description=("Cowsay for Python. Directly executable and importable.")
    )

    parser.add_argument('msg',
                        default=["Cowsay | cowpy. Please seek --help"],
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
                        help=("Choose a cowacter at random (consider --nsfw)."),
                        action="store_true")
    parser.add_argument('-x', '--nsfw',
                        help=("Enable 'not safe for work' cowacters and eyes."),
                        action="store_true")
    parser.add_argument('-C', '--copy',
                        help=("Create a local copy of cow.py for you to include in your own "
                              "python program."),
                        action="store_true")

    logger.debug("parse the args")
    args = parser.parse_args()

    msg = " ".join(args.msg)

    if not sys.stdin.isatty():
        logger.debug("reading from stdin")
        msg = sys.stdin.read()

    exit_early = False
    sfw = not args.nsfw

    if args.copy:
        thisfile = os.path.realpath(__file__)
        thisfile = ''.join(os.path.splitext(thisfile)[:-1]) + '.py'

        bname = os.path.basename(thisfile)
        outfile = os.path.join(os.curdir, bname)
        outfile = ''.join(os.path.splitext(outfile)[:-1]) + '.py'

        if os.path.exists(bname):
            print("The file {0} bname already exists, not making the copy.")
            sys.exit(1)
        else:
            print("{0} -> {1}".format(thisfile, outfile))

        shutil.copyfile(thisfile, outfile)
        exit_early = True

    if args.list or args.list_variations:
        exit_early = True
        for cow_name, cow in get_cowacters(sfw=sfw, sort=True):
            if args.list_variations:
                for eye_name, _ in get_eyes(sfw=sfw, sort=True):

                    nsfw = (not_safe_for_work(cow=cow_name, eyes=eye_name) and ' : NSFW') or ''

                    print(cow(eyes=eye_name).milk("{0}, eye is {1}{2}".format(
                        cow_name, eye_name, nsfw)))
                    print(cow(
                        eyes=eye_name, thoughts=True).milk(
                            "{0}, eye is {1}, with bubble{2}".format(cow_name, eye_name, nsfw)))
                    print(cow(
                        eyes=eye_name, tongue=True).milk("{0}, eye is {1}, with tounge{2}".format(
                            cow_name, eye_name, nsfw)))
            else:
                nsfw = (not_safe_for_work(cow=cow_name) and ' : NSFW') or ''
                print(cow().milk(cow_name + nsfw))

    if args.list_eyes:
        exit_early = True
        for k, v in get_eyes(sfw=sfw, sort=True):
            print("{0} : '{1}'{2}".format(k, v, (not_safe_for_work(eyes=k) and ' : NSFW') or ''))

    if exit_early:
        sys.exit(0)

    logger.debug("find the cow")
    cow = get_cow()
    if args.cowacter:
        try:
            cow = get_cow(args.cowacter.lower())
        except KeyError:
            print("{0} is an invalid cowacter".format(args.cowacter))
            sys.exit(1)

    if args.random:
        print(milk_random_cow(msg, sfw=sfw))
        sys.exit(0)

    print(cow(eyes=args.eyes,
          tongue=args.tongue,
          thoughts=args.thoughts
              ).milk(msg)
          )


if __name__ == '__main__':
    main()
