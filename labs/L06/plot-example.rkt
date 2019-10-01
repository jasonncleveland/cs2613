#lang racket
(require "calculus.rkt")
(require plot)

(plot
 (list
  (function sin -2pi -2pi)
  (function (lambda (x) (deriv sin x)))))

(plot
 (list
  (function cos (/ pi 2) (/ pi 2))
  (function (lambda (x) (deriv cos x)))))