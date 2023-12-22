def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    # No solution
    if sum(gas) < sum(cost):
        return -1

    gas_in_tank, start_indx = 0, 0
    for i in range(len(gas)):
        gas_in_tank += gas[i] - cost[i]  # gas in tank += gained - spent
        if gas_in_tank < 0:  # if trip not possible
            gas_in_tank = 0  # reset gas in tank
            start_indx = i + 1  # starting not possible from <=i
    return start_indx


gas = [5, 8, 2, 8]
cost = [6, 5, 6, 6]
print(canCompleteCircuit(gas, cost))
