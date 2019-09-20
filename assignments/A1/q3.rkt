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

(define (sieve x)
  ; 0 and 1 are never prime numbers so skip and start at 2
  ; If x is less than 2 both will be empty lists
  (sieve-with (range 2 x) (range 2 x)))

(module+ test
  (require rackunit)
  (check-equal? (sieve 0) (list))
  (check-equal? (sieve 1) (list))
  (check-equal? (sieve 10) (list 2 3 5 7)))