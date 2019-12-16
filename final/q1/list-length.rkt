#lang racket

(provide list-length)

(define (list-length lst)
  (define (helper lst sum)
    (cond
      [(empty? lst) sum]
      [else (helper (rest lst) (add1 sum))]))
  (helper lst 0))