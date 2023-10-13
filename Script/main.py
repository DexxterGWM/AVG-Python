'''
    >= 6.0 - Approved
    < 6.0  - Disapproved
'''

def Calculate(self):
    return f'''\n Final average: {self.aver:.2f}\n --{
        ['Disapproved', 'Approved'][self.aprov]
    }'''

def Entry(self):
    try:
        system('cls' if 'nt' == name else 'clear')

        self.grd1 = float(input(' Grade 1: ')); assert -1 < self.grd1 < 10.1
        self.grd2 = float(input(' Grade 2: ')); assert -1 < self.grd2 < 10.1

        self.aver = (self.grd1 + self.grd2) // 2
        self.aprov = [False, True][self.aver >= 6.0]

        return True
    
    except AssertionError:
        input(' [-] Type numbers < 11 and > -1.')
    
    except Exception as err:
        input(f' [-] {type(err).__name__}: {err}.')

from os import system, name

obj = type('Obj', (object, ), {'Calculate': Calculate, 'Entry': Entry})
start = obj()

try:
    while not start.Entry():
        if start.Entry(): break
    
    print(f'''{
          start.Calculate()
    }''')
    
except KeyboardInterrupt: print()