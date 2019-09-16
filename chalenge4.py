# 1
def f():
    """
    これは入力した値を２乗する関数です
    整数を入力してください
    """
    x = input("type number")
    x = int(x)
    print(x ** 2)

f()

# 2
def f():
    """
    彼女の名前を入力すると愛の告白が行われます
    """
    x = input("type youre GF:")
    print("I love " + x)

f()

# 3
def f(a, b, c, d=10, f=100):
    """
    return 10 if any number input
    :param a b c :int.
    """
    x = a + b + c
    y = x * d
    z = x * f
    print(z / y)

f(1, 2, 3)

# 4
def divide(x):
    return x / 2
    


def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)    
    
print(z)

# 5
def strings(x):
    try:
        return float(x)
    except ValueError:
        print("str cannot type")

strings("hina")

# 6
