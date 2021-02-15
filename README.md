# koolCode
## Info
koolCode is a simple coding language build in Python.
### .py and .exe
You can use either `main.py` or `main.exe`.
### Contributing
Feel free to create pull requests.
You should edit `interp.py`, not `main.py`. Upon pull request approval, I will edit `main.py` and create an exe release.
## Guide
### Functions/Keywords
```
print "Hello World!" "This is on a new line!"
add "Module name here!"
```
### Built In Modules
Custom modules are not yet supported.
#### Python
Example:
```
add "python"
runpy "print('Hello World!')
```
### Create Modules
**CUSTOM MODULES ARE NOT SUPPORTED YET!**
#### Getting Started
Start by making a file with any extension, however `.kocm` is recommeneded and can be trusted.
In this example I'll be using `input-print.kocm`.
Ill be using Python, so inside this file I'll add `{"runlang":"python"}`.
Now I need to add a function, so I'll add a function called `repeat`. Now my code is `{"runlang":"python","repeat":"print(input())"}`.
Now to run my function I'll use `add "input-print.kocm"`. and then `repeat`. Now if I type something in it will repeat it.
Alternativly I could use `{"runlang":"koolcode","repeat":"print \"%quote%\""}` and `repeat "thing"`, however this is just like using `print "thing"`.
