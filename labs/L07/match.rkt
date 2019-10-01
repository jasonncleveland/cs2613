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

(module+ test
  (check-equal? (let* ([x 5]
                       [y (- x 3)])
                  (+ y y))
                4)
  (check-equal? (let* ([x 5]
                       [y (- x 3)]
                       [y x])
                  (* y y))
                25))

(module+ test
  (check-equal? (let ([x 5])
                  (let ([y (- x 3)])
                    (+ y y)))
                4)
  (check-equal? (let ([x 5])
                  (let ([y (- x 3)])
                    (let ([y x])
                      (* y y))))
                25)