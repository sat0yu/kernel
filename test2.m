source kernel.m
load data
samples_x = data(:,1);
samples_y = data(:,2);

x = [-3:0.05:3]';

y1 = optimized_regression(1, data, x);
y10 = optimized_regression(10, data, x);
y100 = optimized_regression(100, data, x);
y1000 = optimized_regression(1000, data, x);

hold off

subplot(2,2,1)
plot(x,y1,'b', samples_x,samples_y,'r*')
axis([-3 3 -10 10])

subplot(2,2,2)
plot(x,y10,'b', samples_x,samples_y,'r*')
axis([-3 3 -10 10])

subplot(2,2,3)
plot(x,y100,'b', samples_x,samples_y,'r*')
axis([-3 3 -10 10])

subplot(2,2,4)
plot(x,y1000,'b', samples_x,samples_y,'r*')
axis([-3 3 -10 10])
