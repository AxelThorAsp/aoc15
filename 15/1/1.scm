(use-modules (ice-9 rdelim))
(define user-input 
  (read-lines
    (current-input-port)))
(define line (string->list user-input))

(define (close-paren? char)
  (eq? char #\)))

(define (resolve x)
  (if(close-paren? x)
    -1
    1))

(define (parse x xs f p)
  (if (= f -1)
    p
    (if (close-paren? x)
      (parse (car xs) (cdr xs) (- f 1) (+ p 1))
      (parse (car xs) (cdr xs) (+ f 1) (+ p 1)))))

(define (parse-help xs)
  (parse (car xs) (cdr xs) 0 0))

(display (parse-help line))
(newline)

