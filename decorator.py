"""Decorators homework."""

# абрамлнне *****


def stars(func):
    """Stars funcion."""
    def inner(*args, **kwargs):
        print("************")
        func(*args, **kwargs)
        print("************")
        return inner


# decorator syntax


@stars
def hello_world():
    """Hello_world funcion."""
    print("hello world!")


# The following prints:
# **********
# hello world!
# **********


hello_world()
