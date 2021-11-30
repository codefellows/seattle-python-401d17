# Overview of Reversing List

```python
def reverse_list_a(things):
    return things[::-1]

def reverse_list_b(things):
    things.reverse()
    return things

def reverse_list_c(things):
    return list(reversed(things))

def reverse_list_d(things):
    reverse_list = []
    for thing in reversed(things):
        reverse_list.append(thing)
    return reverse_list

def reverse_list_e(things):
    reverse_list = []
    for thing in things:
        reverse_list.insert(0,thing)
    return reverse_list

result = reverse_list_a(["a","b","c"])
print(result)

result = reverse_list_b(["a","b","c"])
print(result)

result = reverse_list_c(["a","b","c"])
print(result)

result = reverse_list_d(["a","b","c"])
print(result)

result = reverse_list_e(["a","b","c"])
print(result)
```
