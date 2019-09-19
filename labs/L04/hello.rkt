(module hello-module racket
  (provide hello)
  (define (hello)
    (displayln "Hello World!"))

  (module+ test
    (require rackunit)
    (check-equal? (with-output-to-string hello) "Hello World!\n")
    (check-equal? (with-output-to-string hello) (begin (sleep 3) "Hello World!\n"))))