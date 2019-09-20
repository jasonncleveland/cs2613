#lang racket

(define (drop-divisible x lst)
  (filter (lambda (i)
            (not
             (and
              (eq? (modulo i x) 0)
              (> (/ i x) 1))))
          lst))

(module+ test
  (require rackunit)
  (check-equal? (drop-divisible 2 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 5 7 9))
  (check-equal? (drop-divisible 3 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 7 8 10))
  (check-equal? (drop-divisible 5 (list 2 3 4 5 6 7 8 9 10)) (list 2 3 4 5 6 7 8 9)))