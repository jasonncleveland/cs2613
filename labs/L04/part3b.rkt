#lang racket

(define (list-length list)
  (if (empty? list)
      0
      (+ 1 (list-length (rest list)))))

(module+ test
  (require rackunit)
  (define test-list '(1 2 3))

  (check-equal? (length test-list) (list-length test-list)))