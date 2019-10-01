#lang racket
(define (my-map f lst)
  (match lst
    ['() '()]
    [(cons head tail) (cons (f head)
                            (my-map f tail))]))

(module+ test
  (require rackunit)
  (check-equal? (my-map sub1 '(1 2 3)) '(0 1 2)))

(define (my-map2 f lst)
  (match lst
    ['() '()]
    [(list head tail ...) (cons (f head)
                                (my-map2 f tail))]))