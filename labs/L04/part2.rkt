#lang slideshow

(define (series mk)
  (hc-append 4 (mk 5) (mk 10) (mk 20)))

(define (series2 mk)
  (hc-append 4 (map mk '(5 10 20))))

(define (series3 mk)
  (apply hc-append 1 (build-list 100 mk)))