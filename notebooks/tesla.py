#import libraries

import statistics
# include data

A_rank = [0.8, 0.4, 1.2, 3.7, 2.6, 5.8, 6.4]
B_rank = [0.8, 0.4, 1.2, 3.7, 2.6, 5.8, 7.8]

# calculate stadistics

mean = statistics.covariance(A_rank, B_rank)
median = statistics.median(A_rank)
lr = statistics.linear_regression(A_rank, B_rank)
std = statistics.stdev(A_rank)

# print

print(std)
print(mean)
print(median)
print(lr)
