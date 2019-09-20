#lang racket

(define (drop-divisible x lst)
  (filter (lambda (i)
            (not
             (and
              (eq? (modulo i x) 0)
              (> (/ i x) 1))))
          lst))

(define (sieve-with divs lst)
  (define (iter div lst)
    (cond
      [(empty? div) lst]
      [else (iter (rest div) (drop-divisible (first div) lst))]))
  (iter divs lst))

(module+ test
  (require rackunit)
  (check-equal? (sieve-with '() (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 6 7 8 9 10))
  (check-equal? (sieve-with '(2 3) (list 2 3 4 5 6 7 8 9 10)) (list 2 3 5 7)))