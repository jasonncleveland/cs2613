function ret = fibmat(n)
    A = [1,1; 1,0];
    B = A^n;
    ret = B(1,2);
endfunction

%!assert(fibmat(0) == 0);
%!assert(fibmat(1) == 1);
%!assert(fibmat(2) == 1);
%!assert(fibmat(3) == 2);
%!assert(fibmat(4) == 3);
%!assert(fibmat(5) == 5);
%!assert(fibmat(6) == 8);
%!assert(fibmat(25) == 75025);