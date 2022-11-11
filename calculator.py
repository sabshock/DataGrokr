def add(x,y):
    return x + y


def sub(x,y):
    return x - y


def mul(x,y):
    return x * y


def div(x,y):
    if y == 0:
        raise ValueError("Zero can't be divded by any number")
    return x/y

x, y = list(map(int,(input("Enter the numbers(x,y)")).split(",")))
op = input("Enter the operation to be performed:")
func = {'add':add,'sub':sub,'mul':mul,'div':div}
print(func[op](x,y))