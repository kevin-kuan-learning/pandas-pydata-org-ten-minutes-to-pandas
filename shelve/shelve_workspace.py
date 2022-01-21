filename = 'shelve\\current_python_workspace.out'

with shelve.open(filename, "n") as shelf:
   for key in dir():
       try:
           shelf[key] = globals()[key]
       except TypeError:
           print("ERROR shelving: {0}".format(key))
