#### *args allows a function to accept any number of positional arguments.

###### args is a tuple.


def total_sum(*args):
    print(sum(args))

total_sum(1, 2, 3)      # 6
total_sum(5, 10, 15)    # 30
