#lang racket

(define (fact n)
  (cond
    [(zero? n) 1]
    [else (* n (fact (sub1 n)))]))

(module+ test
  (require rackunit)
  (check-equal? (fact 10) 3628800))