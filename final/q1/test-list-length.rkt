#lang racket
(require "list-length.rkt")

(module+ test
  (require rackunit)

  ; Test an empty list returns a length of 0
  (check-equal? (list-length '()) 0 "An empty list has a length of 0")
  ; Test normal lists return correct length
  (check-equal? (list-length '(1)) 1 "A list with 1 element has a length of 1")
  (check-equal? (list-length '(1 2 3 4 5 6)) 6 "A list with 6 elements has a length of 6")
  ; Test a list of lists returns the length of the outer list
  (check-equal? (list-length '('(1 2 3) '(4 5 6))) 2 "A list of lists only counts the outer list"))
