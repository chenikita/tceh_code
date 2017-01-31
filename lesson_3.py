Last login: Tue Jan 31 15:51:48 on ttys002
chenikita:~ chenikita$ 
chenikita:~ chenikita$ Python3
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(1 /0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> try:
...     print(1 / 0)
... except:
...     print('0!!')
... 
0!!
>>> try:
...    print(1 / 0)
... except Exception:
...     print('0!!')
... try:
  File "<stdin>", line 5
    try:
      ^
SyntaxError: invalid syntax
>>> try:
... 
  File "<stdin>", line 2
    
    ^
IndentationError: expected an indented block
>>> try:
... ...    print(1 / 0)
  File "<stdin>", line 2
    ...    print(1 / 0)
      ^
IndentationError: expected an indented block
>>> ... except Exception:
  File "<stdin>", line 1
    ... except Exception:
             ^
SyntaxError: invalid syntax
>>> ...     print('0!!')
  File "<stdin>", line 1
    ...     print('0!!')
                ^
SyntaxError: invalid syntax
>>> try:
...     3 / int(imput('Some number: '))
... except Exception
  File "<stdin>", line 3
    except Exception
                   ^
SyntaxError: invalid syntax
>>> try:
...     print(1 / 0)
... except ZeroDivisionError:
...     print('Exception!')
... 
Exception!
>>> try:
...     print(1 / 0)
... except ZeroDivisionError as e:
...     print('Exception! Stop it!')
...     print(e)
... 
Exception! Stop it!
division by zero
>>> try:
...     d = {'key': 23}
...     print(d['does not exist'])
... except KeyError:
...     print('fail')
... 
fail
>>> raise KeyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError
>>> raise ValueError('Custom message')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Custom message
>>> try:
...     raise VallueError('Custom message')
... xcept ValueError as e:
  File "<stdin>", line 3
    xcept ValueError as e:
        ^
SyntaxError: invalid syntax
>>> except ValueError as e:
  File "<stdin>", line 1
    except ValueError as e:
         ^
SyntaxError: invalid syntax
>>>     raise VallueError('Custom message')
  File "<stdin>", line 1
    raise VallueError('Custom message')
    ^
IndentationError: unexpected indent
>>> try:
...     raise ValueError()
... except ZeroDivisionError:
...     print('Divided by zero')
... except Exception as ex:
...     print('strange')
... 
strange
>>> try:
...     print(1 / 0)
... except ZeroDivisionError:
...     print('0!!')
... finally:
...     print('end of the end')
... 
0!!
end of the end
>>> try:
...         print('try')
...     except ValueError:
  File "<stdin>", line 3
    except ValueError:
                     ^
IndentationError: unindent does not match any outer indentation level
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finaly:
  File "<stdin>", line 1
    finaly:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')
  File "<stdin>", line 1
    print('finally нах!!!')
    ^
IndentationError: unexpected indent
>>>     try:
  File "<stdin>", line 1
    try:
    ^
IndentationError: unexpected indent
>>>         print('try')
  File "<stdin>", line 1
    print('try')
    ^
IndentationError: unexpected indent
>>>     except ValueError:
  File "<stdin>", line 1
    except ValueError:
    ^
IndentationError: unexpected indent
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finaly:
  File "<stdin>", line 1
    finaly:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')
  File "<stdin>", line 1
    print('finally нах!!!')
    ^
IndentationError: unexpected indent
>>> try:
...         print('try')
...     except ValueError:
  File "<stdin>", line 3
    except ValueError:
                     ^
IndentationError: unindent does not match any outer indentation level
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finaly:
  File "<stdin>", line 1
    finaly:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')    try:
  File "<stdin>", line 1
    print('finally нах!!!')    try:
    ^
IndentationError: unexpected indent
>>>         print('try')
  File "<stdin>", line 1
    print('try')
    ^
IndentationError: unexpected indent
>>>     except ValueError:
  File "<stdin>", line 1
    except ValueError:
    ^
IndentationError: unexpected indent
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finally:
  File "<stdin>", line 1
    finally:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')    try:
  File "<stdin>", line 1
    print('finally нах!!!')    try:
    ^
IndentationError: unexpected indent
>>>         print('try')
  File "<stdin>", line 1
    print('try')
    ^
IndentationError: unexpected indent
>>>     except ValueError:
  File "<stdin>", line 1
    except ValueError:
    ^
IndentationError: unexpected indent
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finally:
  File "<stdin>", line 1
    finally:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')    try:
  File "<stdin>", line 1
    print('finally нах!!!')    try:
    ^
IndentationError: unexpected indent
>>>         print('try')
  File "<stdin>", line 1
    print('try')
    ^
IndentationError: unexpected indent
>>>     except ValueError:
  File "<stdin>", line 1
    except ValueError:
    ^
IndentationError: unexpected indent
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finally:
  File "<stdin>", line 1
    finally:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')
  File "<stdin>", line 1
    print('finally нах!!!')
    ^
IndentationError: unexpected indent
>>> 
>>> 
>>> 
>>> 
>>>     try:
  File "<stdin>", line 1
    try:
    ^
IndentationError: unexpected indent
>>>         print('try')
  File "<stdin>", line 1
    print('try')
    ^
IndentationError: unexpected indent
>>>     except ValueError:
  File "<stdin>", line 1
    except ValueError:
    ^
IndentationError: unexpected indent
>>>         pass
  File "<stdin>", line 1
    pass
    ^
IndentationError: unexpected indent
>>>     else:
  File "<stdin>", line 1
    else:
    ^
IndentationError: unexpected indent
>>>         print('else')
  File "<stdin>", line 1
    print('else')
    ^
IndentationError: unexpected indent
>>>     finally:
  File "<stdin>", line 1
    finally:
    ^
IndentationError: unexpected indent
>>>         print('finally нах!!!')
  File "<stdin>", line 1
    print('finally нах!!!')
    ^
IndentationError: unexpected indent
>>> try:
...     print('try')
... except ValueError:
...     pass
... else:
...     print('else')
... finally:
...     print('finally нах!!!')
... 
try
else
finally нах!!!
>>> try:
...     3 / x
... except ZeroDivisionError:
...     print ('no')
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'x' is not defined
>>> x = 0
>>> try:
...     3 / x
... except ZeroDivisionError:
...     print ('no')
... 
no
>>> def has_args(*args):
...     print('A lot of arguments: ', args)
... 
>>> 
>>> def has_args(*args):
...     print('A lot of arguments: ', args)
... 
>>> def has_kwargs(**kwargz):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... 
>>> 
>>> def has_kwargs(**kwargz):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... 
>>>     has_kwargs(any_possible=None, values=[], you_wish=1)
  File "<stdin>", line 1
    has_kwargs(any_possible=None, values=[], you_wish=1)
    ^
IndentationError: unexpected indent
>>> def has_kwargs(**kwargs):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... 
>>> 
>>> def has_kwargs(**kwargs):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... 
>>>     has_kwargs(any_possible=None, values=[], you_wish=1)
  File "<stdin>", line 1
    has_kwargs(any_possible=None, values=[], you_wish=1)
    ^
IndentationError: unexpected indent
>>> 
>>> def has_kwargs(**kwargs):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... as_kwargs(any_possible=None, values=[], you_wish=1)
  File "<stdin>", line 4
    as_kwargs(any_possible=None, values=[], you_wish=1)
            ^
SyntaxError: invalid syntax
>>> l = [1, 2, 3]
>>> has_args(*s)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> l = [1, 2, 3]
>>> has_args(*l)
A lot of arguments:  (1, 2, 3)
>>> def has_kwargs(**kwargs):
...     print('A lot of keyword arguments', kwargs)
...     print('kwargs is a dict', type(kwargs))
... has_kwargs(any_possible=None, values=[], you_wish=1)
  File "<stdin>", line 4
    has_kwargs(any_possible=None, values=[], you_wish=1)
             ^
SyntaxError: invalid syntax
>>> has_kwargs(any_possible=None, values=[], you_wish=1)
A lot of keyword arguments {'any_possible': None, 'values': [], 'you_wish': 1}
kwargs is a dict <class 'dict'>
>>> def work(value):
...     return value * 2
... 
>>> t = [1, 2, 10]
>>> m = map(t, work)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> print(m)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'm' is not defined
>>> def work(value):
...     return value * 2
... t = [1, 2, 10]
  File "<stdin>", line 3
    t = [1, 2, 10]
    ^
SyntaxError: invalid syntax
>>> m = map(work, t)
>>> print(m)
<map object at 0x101c84e80>
>>> def work(value):
...     return value * 2
... 
>>> t = [1, 2, 10]
>>> m = map(work, t)
>>> print(m)
<map object at 0x101c84ef0>
>>> 
>>> 
>>> m1 = map(t, lambda x: x * 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> print(m1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'm1' is not defined
>>> m1 = map(lambda x: x * 2, t)
>>> print(list(m1)
... 
... 
... 
... 
... 
... 
... m1 = map(lambda x: x * 2, t)
  File "<stdin>", line 8
    m1 = map(lambda x: x * 2, t)
     ^
SyntaxError: invalid syntax
>>> print(list(m1))
[2, 4, 20]
>>> m1 = map(lambda x: x * 2, t)
>>> print(list(m1))
[2, 4, 20]
>>> print(filter([-1, -5, -9, 20, 3, 0], lambda v: v > 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not iterable
>>> rint(list(filter([-1, -5, -9, 20, 3, 0], lambda v: v > 0)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rint' is not defined
>>> print(filter(lambda v: v > 0, [-1, -5, -9, 20, 3, 0], lambda v: v > 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: filter expected 2 arguments, got 3
>>> 
>>> def call_passed_function(incoming):
...     print('Calling!')
...     incoming()
...     print('Called!')
... 
>>> def my_function():
...     print('I am a function')
... dell(my_function)
  File "<stdin>", line 3
    dell(my_function)
       ^
SyntaxError: invalid syntax
>>> print(callable(len), callable(45), callable(callable))
True False True
>>> def my_function():
...     pass
... 
>>> my_function
<function my_function at 0x101c86ae8>
>>> def return_min_function():
...     return min
... 
>>> test = return_min_function()
>>> min_value = test(4, 5, -9, 12)
>>> print('Min values is', min_value)
Min values is -9
>>> GLOBAL_VAR = 3
>>> def using_global_var(x):
...     print(x * GLOBAL_VAR)
... using_global_var(12)
  File "<stdin>", line 3
    using_global_var(12)
                   ^
SyntaxError: invalid syntax
>>> GLOBAL_VAR = 3
>>> 
>>> 
>>> def using_global_var(x):
...     print(x * GLOBAL_VAR)
... 
>>> using_global_var(12)
36
>>> def writing_to_global_var(value):
...     global GLOBAL_VAR
... 
>>>     GLOBAL_VAR = value
  File "<stdin>", line 1
    GLOBAL_VAR = value
    ^
IndentationError: unexpected indent
>>>     print('it is now', GLOBAL_VAR)
  File "<stdin>", line 1
    print('it is now', GLOBAL_VAR)
    ^
IndentationError: unexpected indent
>>> 
>>> writing_to_global_var(9)
>>> def writing_to_global_var(value):
...     global GLOBAL_VAR
...     GLOBAL_VAR = value
...     print('it is now', GLOBAL_VAR)
... writing_to_global_var(9)
  File "<stdin>", line 5
    writing_to_global_var(9)
                        ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> def outer_function(value):
...     def some_inner():
...         print('Value was', value)
...     return some_inner
... v = outer_function('some')
  File "<stdin>", line 5
    v = outer_function('some')
    ^
SyntaxError: invalid syntax
>>> def outer_function(value):
...     def some_inner():
...         print('Value was', value)
... 
>>>     return some_inner
  File "<stdin>", line 1
    return some_inner
    ^
IndentationError: unexpected indent
>>> 
>>> v = outer_function('some')
>>> print('it is a function', v, callable(v))
it is a function None False
>>> git -- version
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'git' is not defined
>>> def outer_function(value):
...     def some_inner():
...         print('Value was', value)
... 
>>>     return some_inner
  File "<stdin>", line 1
    return some_inner
    ^
IndentationError: unexpected indent
>>> 
>>> v = outer_function('some')
>>> print('it is a function', v, callable(v))
it is a function None False
>>> 
KeyboardInterrupt
>>> 
[1]+  Stopped                 Python3
chenikita:~ chenikita$ 
chenikita:~ chenikita$ git -- version
xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.
chenikita:~ chenikita$ git -- version
Unknown option: --
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
chenikita:~ chenikita$ python3
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> mkdircode
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mkdircode' is not defined
>>> mkdir
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mkdir' is not defined
>>> 
[2]+  Stopped                 python3
chenikita:~ chenikita$ mkdir
usage: mkdir [-pv] [-m mode] directory ...
chenikita:~ chenikita$ git init
Initialized empty Git repository in /Users/chenikita/.git/
chenikita:~ chenikita$ pwd
/Users/chenikita
chenikita:~ chenikita$ pwd
/Users/chenikita
chenikita:~ chenikita$ echo print('Hello')
-bash: syntax error near unexpected token `('
chenikita:~ chenikita$ echo print('Hello')git init
-bash: syntax error near unexpected token `('
chenikita:~ chenikita$ echo "print('Hello')
> test.py
> git status
> git add test.py
> 
> 
> 
> 
> -bash: unexpected EOF while looking for matching `"'
-bash: syntax error: unexpected end of file
chenikita:~ chenikita$ git init
Reinitialized existing Git repository in /Users/chenikita/.git/
chenikita:~ chenikita$ git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.CFUserTextEncoding
	.DS_Store
	.anyconnect
	.bash_history
	.bash_profile
	.bash_sessions/
	.cups/
	.dropbox/
	.python_history
	.yandex/
	Applications/
	Desktop/
	Documents/
	Downloads/
	Dropbox/
	Library/
	Movies/
	Music/
	Pictures/
	Prezi/
	Public/

nothing added to commit but untracked files present (use "git add" to track)
chenikita:~ chenikita$ git add test.py
fatal: pathspec 'test.py' did not match any files
chenikita:~ chenikita$ ls
Applications	Documents	Dropbox		Movies		Pictures	Public
Desktop		Downloads	Library		Music		Prezi
chenikita:~ chenikita$ cd code
-bash: cd: code: No such file or directory
chenikita:~ chenikita$ mkdir code
chenikita:~ chenikita$ cd code
chenikita:code chenikita$ ls
chenikita:code chenikita$ git init
Initialized empty Git repository in /Users/chenikita/code/.git/
chenikita:code chenikita$ echo "print('Hi')" > tes.py
chenikita:code chenikita$ mv tes.py test.py
chenikita:code chenikita$ git add test.py 
chenikita:code chenikita$ git commit -m 'Initial'
[master (root-commit) eb5e08d] Initial
 Committer: Никита Черкасенко <chenikita@chenikita.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
 create mode 100644 test.py
chenikita:code chenikita$ git remote add origin https://github.com/chenikita/tceh_code.git
chenikita:code chenikita$ git push -u origin master
Username for 'https://github.com': chenikita
Password for 'https://chenikita@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/chenikita/tceh_code.git/'
chenikita:code chenikita$ 
chenikita:code chenikita$ git push -u origin master
Username for 'https://github.com': chenikita
Password for 'https://chenikita@github.com': 
Counting objects: 3, done.
Writing objects: 100% (3/3), 250 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/chenikita/tceh_code.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
chenikita:code chenikita$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
chenikita:code chenikita$ git pull
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/chenikita/tceh_code
   eb5e08d..4019c46  master     -> origin/master
Updating eb5e08d..4019c46
Fast-forward
 github.py | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 github.py
chenikita:code chenikita$ subl
-bash: subl: command not found
chenikita:code chenikita$ sublime
-bash: sublime: command not found
chenikita:code chenikita$ open github.py
chenikita:code chenikita$ subl .
-bash: subl: command not found
chenikita:code chenikita$ 
chenikita:code chenikita$ python3
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> assert 3 == 3
>>> assert 3 == 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> >>> def outer_function(value):
  File "<stdin>", line 1
    >>> def outer_function(value):
     ^
SyntaxError: invalid syntax
>>> ...     def some_inner():
  File "<stdin>", line 1
    ...     def some_inner():
              ^
SyntaxError: invalid syntax
>>> ...         print('Value was', value)
  File "<stdin>", line 1
    ...         print('Value was', value)
                    ^
SyntaxError: invalid syntax
>>> ... 
Ellipsis
>>> >>>     return some_inner
  File "<stdin>", line 1
    >>>     return some_inner
     ^
SyntaxError: invalid syntax
>>>   File "<stdin>", line 1
  File "<stdin>", line 1
    File "<stdin>", line 1
    ^
IndentationError: unexpected indent
>>>     return some_inner
  File "<stdin>", line 1
    return some_inner
    ^
IndentationError: unexpected indent
>>>     ^
  File "<stdin>", line 1
    ^
    ^
IndentationError: unexpected indent
>>> IndentationError: unexpected indent
  File "<stdin>", line 1
    IndentationError: unexpected indent
                                      ^
SyntaxError: invalid syntax
>>> def outer_function(value):
...     def some_inner():
...         print('Value was', value)
... return some_inner
  File "<stdin>", line 4
    return some_inner
         ^
SyntaxError: invalid syntax
>>> def outer_function(value):
...     def some_inner():
...         print('Value was', value):
  File "<stdin>", line 3
    print('Value was', value):
                             ^
SyntaxError: invalid syntax
>>> return some_inner
  File "<stdin>", line 1
SyntaxError: 'return' outside function
>>> print(1 \ 0)
  File "<stdin>", line 1
    print(1 \ 0)
               ^
SyntaxError: unexpected character after line continuation character
>>> print(1 \ 0):
  File "<stdin>", line 1
    print(1 \ 0):
                ^
SyntaxError: unexpected character after line continuation character
>>> print(1 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> raise RuntimeError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError
>>> 
[3]+  Stopped                 python3
chenikita:code chenikita$ git init
Reinitialized existing Git repository in /Users/chenikita/code/.git/
chenikita:code chenikita$ git add lesson_3.py
fatal: pathspec 'lesson_3.py' did not match any files
chenikita:code chenikita$ save to lesson_3.py
-bash: save: command not found
chenikita:code chenikita$ 
