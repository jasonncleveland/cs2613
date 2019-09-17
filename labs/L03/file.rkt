#lang racket/base

(define (my-+ a b)
  (if (zero? a)
      b
      (my-+ (sub1 a) (add1 b))))

(define (my-* a b)
  (cond
    [(or (zero? a) (zero? b)) 0]
    [(= a 2) (my-+ b b)] ; Not needed. Prevents needless recursive call
    [(= a 1) b] ; Not needed. Prevents needless recursive call`
    [else (my-+ b (my-* (sub1 a) b))]))

(provide my-+
         my-*)

(module+ test
  (require rackunit)
  (check-equal? (my-+ 1 1) 2 "Simple addition: 1 + 1 = 2")
  (check-equal? (my-* 0 2) 0 "Simple multiplication: 0 * 2 = 0")
  (check-equal? (my-* 2 0) 0 "Simple multiplication: 2 * 0 = 0")
  (check-equal? (my-* 1 2) 2 "Simple multiplication: 1 * 2 = 2")
  (check-equal? (my-* 2 2) 4 "Simple multiplication: 2 * 2 = 4")
  (check-equal? (my-* 4 5) 20 "Simple multiplication 4 * 5 = 20"))
