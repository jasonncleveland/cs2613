function bench
    timeit(@fib, 42, 100000)
    timeit(@fibmat, 42, 100000)
endfunction