# Command-line interfaces

## `sys.argv`

​	Allows to access CLI command with arguments   
​	`argv[0]` is the script name

## `argparse` module

​	**Positional arguments**: 	
```{python}
parser.add_argument("name", help="help text", type=int)
```

​	**Optional arguments**:
If argument is present, it is set to `True`

```{python}
parser.add_argument("-short", "--long", help="help text", action="store_true")
```

Only some choices are allowed and shown in help text

```{python}
parser.add_argument("-short", "--long", help="help text", choices=[0, 1, 2])
```

Count the presence of the argument and use `default`

```{python}
parser.add_argument("-short", "--long", help="help text", action="count", default=0)
```
