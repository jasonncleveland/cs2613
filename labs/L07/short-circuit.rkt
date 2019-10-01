#lang racket
(define-syntax-rule (And a b)
  (if b a #f))

(module+ test
  (require rackunit)
  (define (die)
    (error 'die "don't run this"))

  (check-equal? (And (die) #f) #f)
  (check-exn exn:fail? (lambda () (and (die) #f))))