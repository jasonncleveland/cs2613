#lang racket
(require racket/math)

(module+ test
  (require rackunit)
  (define epsilon .001))

(define dx 0.001)
(define -2pi (* -2 pi))
(define 2pi (* 2 pi))

;; compute the derivative of `f` at the given point `x`
(define (deriv f x)
  (/ (- (f (+ x dx)) (f x)) dx))

;; integrate a function from 0 to x (using tail recursion)
(define (integrate f x)
  (define (loop y acc)
    (if (> y x)
        (* acc dx)
        (loop (+ y dx) (+ acc (f y)))))
  (loop 0 0))

(define (integrate2 f x)
  (* dx
     (for/fold
      ([acc 0])
      ([y (in-range 0 x dx)])
       (+ acc (f y)))))

(module+ test
  (check-= (integrate cos (/ pi 4)) (sin (/ pi 4)) epsilon)
  (define test-points (build-list 20 (lambda (x) (* 2 pi (random)))))
  (define (sin2 x) (integrate cos x))
  (define (cos2 x) (deriv sin x))
  (for ([x test-points])
    (check-= (sin2 x) (sin x) epsilon)
    (check-= (cos2 x) (cos x) epsilon))
  (for ([x test-points])
    (check-= (integrate cos x) (integrate2 cos x) epsilon)))