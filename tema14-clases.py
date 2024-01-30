class OperacBas:
    '''
        declaracion de propiedades, 
        constructor de la clase, 
        declaracion de metodos
    '''
    #propiedades
    num1=0
    num2=0
    res=0

    #constructor
    def __init__(self,a,b) -> None:
        self.num1=a
        self.num2=b

    def suma(self):
        self.res = self.num1 + self.num2
        print("{} + {} = {} ".format(self.num1, self.num2, self.res))


def main():
    obj=OperacBas(2,5)
    obj.suma()

if __name__=="__main__":
    main()