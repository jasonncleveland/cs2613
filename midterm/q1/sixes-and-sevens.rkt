#lang racket

(define (sixes-and-sevens lst)
  (define (helper lst divisible)
    (cond
      [(empty? lst) divisible]
      [(= 0 (modulo (first lst) 6)) (helper (rest lst) divisible)]
      [(= 0 (modulo (first lst) 7)) (helper (rest lst) divisible)]
      [else (helper (rest lst) (remove (first lst) divisible))]))
  (helper lst lst))

(module+ test
  (require rackunit)
  (check-equal? (sixes-and-sevens '(1 6 7 12)) '(6 7 12)))
