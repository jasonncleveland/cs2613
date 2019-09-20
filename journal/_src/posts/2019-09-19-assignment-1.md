    Title: Assignment 1 Journal
    Date: 2019-09-20T00:00:00
    Tags: DONE

## Question 1

Question 1 tasks us with creating a function drop-divisible that takes a number and a list. The output of the function is all numbers that are non-trivially divisible by the number.

For my solution I used the higher order function `filter`. I used `filter` by having it run a lambda function against the provided list. This lambda function checks whether the result of the list item modulo the divisor is 0. If the result is 0 it then checks if the number is not equal to the divisor. If both of these conditions are met it returns false to tell filter to not include that item. The tricky part of this question was figuring out the expression needed to filter the list.

```racket
(define (drop-divisible x lst)
  (filter (lambda (i)
            (not
              (and
                (eq? (modulo i x) 0)
                (> (/ i x) 1))))
          lst))
```

## Question 2

Question 2 asked us to build on the function created in question 1 and use it as part of a new function, sieve-with. This new function takes in a list of divisors and uses recursion to remove all items that are divisble by any item in the given divisors list.

This one caught me up for a while. The question asked for recursion but I wasn't sure how to properly use it. I ended up using *tail recursion* and created a helper function that recursively iterated over each divisor and called drop-divisible with it.

```racket
(define (sieve-with divs lst)
  (define (iter div lst)
    (cond
      [(empty? div) lst]
      [else (iter (rest div) (drop-divisible (first div) lst))]))
  (iter divs lst))
```

## Question 3

Question 3 tasked us with combining the functions built in question 1 and question 2 to create a new function, sieve. The sieve function takes in a single number and determines all prime numbers up to, and including the given number.

This function was fairly straight-forward. The only trouble I encountered with it was creating the lists to pass to sieve-with. Passing a list containing 0 would raise an error and including 1 in the list would display it in the prime number list. Since neither 0 nor 1 are prime numbers, I chose to modify the list to start at 2. This solved both of the aforementioned problems.

```racket
(define (sieve x)
  (sieve-with (range 2 x) (range 2 x)))
``` 

## Question 4

The final question in this assignment revolves around testing. The task is to take the function *sieve* and evaluate it against Racket's math function `prime?`.

To do this I created a test module that imported `math/number-theory`. This gave me access to the `prime?` function. After that was imported I needed to set up a `check-equal` test with *sieve* on one side and *prime* on the other. Since `prime?` only checks one number, I needed to wrap it in a filter call on the range from 1 -> 100,000. Running this test took a while but ultimately succeeded!

```racket
(module+ test
  (require rackunit)
  (require math/number-theory)
  (check-equal? (sieve 100000) (filter prime? (range 1 100000))))
```
