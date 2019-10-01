#lang racket
(require explorer)

(define a-list
  (list 1 (list 'foo "hello")
        (hash 'apple "red" 'sky "blue" 'violets "purple")))
(explore a-list)