from functools import partial


def add(sums, amount, location="total", prefix='$'):
    # @TODO: Flesh out. Would like this to add a number to a global variable
    # and then return the number for printing. The global variable can then be
    # accessed through sums.X
    if location not in sums:
        sums[location] = 0.00
    sums[location] += amount
    return "{prefix}{amount}".format(prefix=prefix, amount=float(amount))


def register_extensions(jinja_env):
    if 'sums' in jinja_env.globals or 'add' in jinja_env.globals:
        raise NotImplementedError("IDK how I'm gonna handle this one just yet...")
    sums = {}
    jinja_env.globals['sums'] = sums
    jinja_env.globals['add'] = partial(add, sums)
    return jinja_env
