import matplotlib.pyplot as plt
import knap_sack 
import time

ns     = []
random_times  = []
constant_times = []
inverse_times = []
timesr = []
min_i  = 2
max_i  = 30
n_base = 1.3 

for i in range( min_i, max_i ):
    n = int( n_base ** i )
    max_weight = n * 2

    # generate an input to the algorithm under test
    input_list = knap_sack.generate_inverse_weight_to_value(N = n, W = n)
    time_1_random = time.time()
    knap_sack.find_best_packing(input_list = input_list, max_weight = max_weight)
    time_2_random = time.time()
    time_difference_inverse = time_2_random - time_1_random

    # generate an input to the algorithm under test
    input_list = knap_sack.generate_constant_weight_input(N = n, W = n)
    time_1_random = time.time()
    knap_sack.find_best_packing(input_list = input_list, max_weight = max_weight)
    time_2_random = time.time()
    time_difference_constant = time_2_random - time_1_random

    # generate an input to the algorithm under test
    input_list = knap_sack.generate_random_item_list(n, n, n)
    time_1_random = time.time()
    knap_sack.find_best_packing(input_list = input_list, max_weight = max_weight)
    time_2_random = time.time()
    time_difference_random = time_2_random - time_1_random
    
    ns.append( n )
    inverse_times.append( time_difference_inverse )
    constant_times.append( time_difference_constant )
    random_times.append ( time_difference_random )

plt.plot( ns, random_times, "blue")
plt.plot( ns, constant_times, "green")
plt.plot( ns, inverse_times, "red" )

plt.xlabel('input size')
plt.ylabel('time (s)')
plt.title('Algorithm Timing is Fun')
plt.grid(True)
# plt.savefig("test.png")
plt.show()
