#lang scribble/manual

Title: Scribble Demo
Date: 2019-09-17T00:00:00
Tags: DONE

@(define (hello) "hello")

@(define (todo hdr . lst) (list (bold hdr) (apply itemlist (map item lst))))

@hello{}
@todo["Shopping" "cheese" "fish" "shuriken"]
