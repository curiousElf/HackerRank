__author__ = 'DINUN'

"""Problem Statement

Little Bob loves chocolates, and goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?

Input Format: 
The first line contains the number of test cases T(<=1000). 
T lines follow, each of which contains three integers N, C and M

Output Format: 
Print the total number of chocolates Bob eats.

Constraints: 
2≤N≤105 
1≤C≤N 
2≤M≤N

"""

class ChocolateFeast:

    def __init__(self,_amount,_unit_cost,_free_chocs_criteria):
        self.amount = _amount
        self.unit_cost = _unit_cost
        self.free_chocs_criteria = _free_chocs_criteria

    def get_total_chocolates(self):
        """
        :return: total_chocolates
        """
        chocolates_with_wrappers = self.amount/self.unit_cost
        chocolates_without_wrappers = 0

        while chocolates_with_wrappers >= self.free_chocs_criteria:
            _free_set = chocolates_with_wrappers/self.free_chocs_criteria
            chocolates_with_wrappers -= _free_set*self.free_chocs_criteria
            chocolates_with_wrappers += _free_set
            chocolates_without_wrappers += _free_set*self.free_chocs_criteria

        return chocolates_with_wrappers+chocolates_without_wrappers

c = ChocolateFeast(14440,3,275)
print c.get_total_chocolates()

