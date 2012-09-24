source kernel.m
load data
x = [-2:0.1:2]';
y = optimized_regression(1, data, x);
plot(x,y)
