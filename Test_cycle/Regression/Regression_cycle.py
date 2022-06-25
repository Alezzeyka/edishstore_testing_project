from Test_cases.CP_T1 import CP_T1
from Test_cases.CP_T2 import CP_T2


class Regression_cycle():
    regression_tests = []

    t1 = CP_T1()
    regression_tests.append(t1)

    t2 = CP_T2()
    regression_tests.append(t2)
