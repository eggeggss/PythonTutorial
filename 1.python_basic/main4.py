

def SumDict(**kwargs):
    #print(kwargs)
    print("數學",kwargs.get("math",None))
    print("英文",kwargs.get("english",None))
    print("國語",kwargs.get("chinese",None))
    print("xxx",kwargs.get("xxxx",None))


def Sum(math,english):
    print(math+english)

#Sum(math=90,english=100)

SumDict(math=90,english=100,chinese=90,ab=10,bc=10)
