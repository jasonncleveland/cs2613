#lang slideshow

(define (rainbow p)
  (define (color-mapper color-list)
  (cond
    [(empty? color-list) empty]
    [else (cons (colorize p (first color-list))
                (color-mapper (rest color-list)))]))
  (color-mapper (list "red" "orange" "yellow" "green" "blue" "purple")))