1;

function k = gauss(beta, x1, x2)
  x = x1 - x2;
  k = exp(-beta * x^2);
endfunction

function mat_k = kernel_matrix(beta, vec_x)
  mat_k = [];
  for x1 = vec_x'
    line = [];
    for x2 = vec_x'
      line = [line gauss(beta, x1, x2)];
    end
    mat_k = [mat_k; line];
  end
endfunction

function r = square_error(vec_alpha, mat_k, vec_y)
  vec_error = vec_y - mat_k * vec_alpha;
  r = vec_error' * vec_error; 
endfunction

function best_alpha = optimize(mat_k, vec_y)
  best_alpha = inv(mat_k)  * vec_y;
endfunction

function vec_y = optimized_regression(beta, samples_x_y, vec_x)
  vec_samples_x = samples_x_y(:,1);
  vec_samples_y = samples_x_y(:,2);
  
  mat_kernel = kernel_matrix(beta, vec_samples_x);
  alpha = optimize(mat_kernel, vec_samples_y)
  
  vec_y = [];
  for x = vec_x'
    vec_kernel = [];
    for xi = vec_samples_x'
      vec_kernel = [vec_kernel; gauss(beta, xi, x)];
    end
    vec_y = [vec_y; alpha' * vec_kernel];
  end
endfunction
