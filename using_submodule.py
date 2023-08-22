# This uses a module/class/method that lives in the main repo.
from util.addition-operation import MyAdditionOperation
myAdd = MyAdditionOperation(2)
r1 = myAdd.add_numbers(7, 8)
print('The result of my_addition is: ', r1)

from submodule.multiplication_operation import MyAdditionOperation
myMult = MyAdditionOperation(3)
r2 = myMult.multiply_numbers(3, 7)
print('Te result of my_multiplication is:', r2)
