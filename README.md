For this weekend's honor assignment you will write an implementation of the knapsack problem, following the textbook's description in section 6.4.

Your implementation should return the subset of items that represent any optimal solution to the problem instance. This can be a list, array, set, whatever. It should also print the optimal value.

In addition to the knapsack implementation, there are three more tasks:

First, write at least 3 small, nontrivial test cases and verify by hand that your implementation returns an optimal set.

Second, write two different input generators that take "N" and "W" as inputs, and produce problem instances of the specified size. You will then test your generators on a range of input sizes. The goal is for the different input generators to exhibit different scaling in some interesting way. You may not be able to get a "big-O" difference for this algorithm, but it should be possible to at least find a consistent constant factor difference based on the shape of the input data.

Here is a very simple example input generator:

def knapsackInputAllBig( N, W ):
    items = []
    for i in range( N ):
        items.append( ( 1, W ) )
    return items
This code is building a list of length N, where each item in the list is a tuple where the first element is the value of the item and the second is the weight.

Finally, you should write a short text document that explains your two input generators and why your knapsack implementation performs differently on inputs from the two generators.

Upload your implementation code (including all testing code), whatever relevant graphs you make and your text document.

Submit to this assignment by Monday morning.
