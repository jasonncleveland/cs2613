#lang racket
(require explorer)
(require json)

(define (read-json-file file-name)
  (with-input-from-file file-name read-json))

(define (visualize-json-file file-name)
  (explore (read-json-file file-name)))

(define (collect-status file-name)
  (map (lambda (error-hash)
         (hash-ref error-hash 'status))
       (hash-ref (read-json-file file-name) 'errors)))

(module+ test
  (require rackunit)
  (check-equal? (collect-status "errors.json") '("403" "422" "500")))