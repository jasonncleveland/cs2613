function ctimeit(func, argument, reps)
    times = zeros(reps, 1);

    for i=1:reps
      start = cputime();
      func(argument);
      times(i) = cputime() - start;
    end

    times = sort(times);
    fprintf ('%s\tmedian=%.3fms mean=%.3fms total=%.3fms\n',func2str(func), median(times)*1000,
             mean(times)*1000, sum(times)*1000);
endfunction