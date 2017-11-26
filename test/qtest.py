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

# Create a random cow with a one-line message
msg = cow.milk_random_cow("A random message for fun")
print(msg)

# Create a random cow with a multi-line message
msg = cow.milk_random_cow("\n".join([
    "A random multi-line message:",
    "1. for fun",
    "2. for fun",
    "3. and for fun"
]))
print(msg)

# all the eye options
eye_options = cow.eye_options()
print(eye_options)

# all the cowacter options
cow_options = cow.cow_options()
print(cow_options)
