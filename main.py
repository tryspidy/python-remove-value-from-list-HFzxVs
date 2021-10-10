# Below are examples of 'remove', 'del', and 'pop' 
#   methods of removing from a python list
""" 'remove' removes the first matching value, not a specific index: """
>>> a = [0, 2, 3, 2]
>>> a.remove(2)
>>> a
[0, 3, 2]

""" 'del' removes the item at a specific index: """
>>> a = [9, 8, 7, 6]
>>> del a[1]
>>> a
[9, 7, 6]

""" 'pop' removes the item at a specific index and returns it. """
>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]

""" Their error modes are different too: """
>>> a = [4, 5, 6]
>>> a.remove(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> del a[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> a.pop(7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range