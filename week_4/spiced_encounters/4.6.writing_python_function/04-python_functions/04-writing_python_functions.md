# Writing Python functions

04/04/2022

**parameters**: obligatory and default   
***args**  -  list of additional unnamed parameters   
********kwargs**  -  dict for additional named parameters     
**name space (scope)**  - variable scope of function
**docstring**  -  description of function ([commonly used styles](https://stackoverflow.com/questions/3898572/what-are-the-most-common-python-docstring-formats))

### Python function example

```{python}
def calc_price(fruit, n=4):
    ```Returns the price of fruits.```
    if fruit == 'banana':
        return 0.75 * n
    
print(calc_price('banana', 10))
```

### List and keyword parameters

```{python}
def func(*args, **kwargs):
    print(args[1])
    print(kwargs['a'])

func(1, 2, a=3, b=4)
```
