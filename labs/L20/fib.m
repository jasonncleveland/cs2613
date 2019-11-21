function ret = fib(n)
    a = 0;
    b = 1;
    for i=0:n
        ret = a;
        a = a + b;
        b = ret;
    endfor
endfunction

%!assert(fib(0) == 0);
%!assert(fib(1) == 1);
%!assert(fib(2) == 1);
%!assert(fib(3) == 2);
%!assert(fib(4) == 3);
%!assert(fib(5) == 5);