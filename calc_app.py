import calculator as cal
x, y = list(map(int,(input("Enter the numbers(x,y)")).split(",")))
op = input("Enter the operation to be performed:")
func = {'add':cal.add,'sub':cal.sub,'mul':cal.mul,'div':cal.div}
print(func[op](x,y))