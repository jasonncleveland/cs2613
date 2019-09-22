#lang racket

(module+ test
  (require rackunit))

(define (odds-evens lst)
  (cond
    [(empty? lst) (list 0 0)]
    [(odd? (first lst)) (map + '(1 0) (odds-evens (rest lst)))]
    [(even? (first lst)) (map + '(0 1) (odds-evens (rest lst)))]))

(define (odds-evens2 lst)
  (define (helper lst odds evens)
    (cond
      [(empty? lst) (list odds evens)]
      [(odd? (first lst)) (helper (rest lst) (add1 odds) evens)]
      [(even? (first lst)) (helper (rest lst) odds (add1 evens))]))
  (helper lst 0 0))

(module+ test
  (check-equal? (odds-evens (list 3 2 1 1 2 3 4 5 5 6)) (list 6 4))
  (define random-list (build-list 100 (lambda (x) (random 1 100))))
  (check-equal? (odds-evens2 (list 3 2 1 1 2 3 4 5 5 6)) (list 6 4))
  (check-equal? (odds-evens random-list) (odds-evens2 random-list)))
