#lang racket

(module+ test
  (require rackunit))

(define ht (hash "apple" 'red "banana" 'yellow))

(module+ test
  (check-equal? (hash-ref ht "apple") 'red))

(define ht2 (hash-set ht "coconut" 'brown))

(module+ test
  (check-equal? (hash-ref ht2 "coconut") 'brown)
  (check-exn exn:fail? (lambda () (hash-ref ht "coconut"))))

(define (census . lst)
  (define (helper lst acc-hash)
    (cond
      [(empty? lst) (hash->list acc-hash)]
      [else
       (let* ([key (first lst)]
              [current (hash-ref acc-hash key 0)])
         (helper (rest lst) (hash-set acc-hash key (add1 current))))]))
  (helper lst (hash)))

(module+ test
  (check-equal?
   (sort (census 1 2 3 1 2) #:key car <) '((1 . 2) (2 . 2) (3 . 1)))
  (check-equal?
   (sort (census "aardvark" "dingo" "buffalo" "buffalo" "bear") #:key car string<?)
         '(("aardvark" . 1) ("bear" . 1) ("buffalo" . 2) ("dingo" . 1))))