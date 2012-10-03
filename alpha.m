1;

source ./kernel.m
load ./data
samples_x = data(:,1);
samples_y = data(:,2);

mat_k_b_1 = kernel_matrix(1, samples_x);
mat_k_b_10 = kernel_matrix(10, samples_x);
mat_k_b_100 = kernel_matrix(100, samples_x);
mat_k_b_1000 = kernel_matrix(1000, samples_x);

alpha_b_1 = optimize(mat_k_b_1, samples_y);
alpha_b_10 = optimize(mat_k_b_10, samples_y);
alpha_b_100 = optimize(mat_k_b_100, samples_y);
alpha_b_1000 = optimize(mat_k_b_1000, samples_y);

hold off;

x = [1:length(samples_x)];

subplot(2,2,1)
bar(x, alpha_b_1);
axis([1 length(x)])
title("beta=1");

subplot(2,2,2)
bar(x, alpha_b_10);
axis([1 length(x)])
title("beta=10");

subplot(2,2,3)
bar(x, alpha_b_100);
axis([1 length(x)])
title("beta=100");

subplot(2,2,4)
bar(x, alpha_b_1000);
axis([1 length(x)])
title("beta=1000");
