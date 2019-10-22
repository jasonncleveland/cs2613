#lang racket
(require "sixes-and-sevens.rkt")

(module+ test
  (require rackunit)

  ; Test that an empty list is handled properly and returns no multiples
  (check-equal? (sixes-and-sevens '()) '() "Nothing given, no multiples")
  ; Test that zero is a multiple of six and seven
  (check-equal? (sixes-and-sevens '(0)) '(0) "Zero is a multiple of six and seven")
  ; Test that a list containing no multiples of six or seven
  (check-equal? (sixes-and-sevens '(1 2 3 4 5)) '() "No multiples of six or seven")
  ; Test that a list containing a multiple of six and seven only appears once in the result
  (check-equal? (sixes-and-sevens '(42)) '(42) "Divisor of six and seven only appears once"))