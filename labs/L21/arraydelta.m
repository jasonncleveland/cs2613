function ret = arraydelta(beta, a, X, Y)
  ret = beta*(a(1).*X+ a(2).*Y) - (beta-1)*(X.^2 + Y.^2);
endfunction

%!test
%! a = rand(2, 1);
%! X = [2,2;2,2]
%! Y = [-1,-1;-1,-1]
%! assert(arraydelta(0,a,X,Y), [5,5;5,5], eps)

%!test
%! a = rand(2,1);
%! beta= rand*6;
%! X = rand(10, 10);
%! Y = rand(10, 10);
%! assert(arraydelta(beta, a, X, Y), arrayfun(@(x,y)(delta(beta,a,[x;y])), X, Y), eps)
