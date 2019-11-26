a = [4;4];
beta = 7.5;
range = [-4:0.1:8];
[X,Y] = meshgrid(range, range);

f = @(x,y)(delta(beta, a, [x;y]));
tic();
Z = arrayfun(f, X, Y);
toc()

surf(X,Y,Z);