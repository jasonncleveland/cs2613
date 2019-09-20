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
  (require math/number-theory)
  (check-equal? (sieve 5) (filter prime? (range 1 5)))
  (check-equal? (sieve 100000) (filter prime? (range 1 100000))))