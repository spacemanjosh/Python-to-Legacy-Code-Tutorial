; docformat = 'rst'
;+
; :Description:
;    Recursive function to compute the Nth Fibonacci number.
;
; :Params:
;    N [in, required, int] : Scalar integer
;
; :Author: Josh Elliott : joshua.elliott@lasp.colorado.edu
;
; Apr 2, 2018 10:14:50 AM
;-
function fibonacci, N
  compile_opt idl2
  
  if (N eq 0) then begin
    fib = 0
  endif else if (N eq 1) then begin
    fib = 1
  endif else begin
    fib = fibonacci(N-1) + fibonacci(N-2)
  endelse
  
  return, fib
end
