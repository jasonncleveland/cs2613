a = [4;4];
beta = 7.5;

%% Generating vectors
range = [-4:0.1:8];

% Compute cartesian product (grid)
[X,Y] = meshgrid(range, range);
[rows,cols] = size(X);

tic();
for i = 1:rows
  for j = 1:cols
    b = [X(i,j);Y(i,j)];
    Z(i,j) = delta(beta, a, b);
  endfor
endfor
toc()

surf(X,Y,Z);
% contourf(X,Y,Z);
