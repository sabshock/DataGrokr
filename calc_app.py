import calculator as cal
flage = 'y'
while flage.lower()=='y':
    x, y = list(map(int,(input("Enter the numbers(x,y)")).split(",")))
    op = (input("Enter the operation to be performed ['add','sub','mul','div']:")).lower()
    func = {'add':cal.add,'sub':cal.sub,'mul':cal.mul,'div':cal.div}
    print(func[op](x,y))
    flage = input('Do you want to continue[y/n]: ')