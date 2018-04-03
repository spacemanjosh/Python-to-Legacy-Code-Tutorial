% :Description:
%    Recursive function to compute the Nth Fibonacci number.
%
% :Params:
%    n [in, required, int] : Scalar integer
%
% :Author: Josh Elliott : joshua.elliott@lasp.colorado.edu
%
% Apr 2, 2018 10:14:50 AM
function f = fibonacci(n)

    f = 0; 
    if n == 0
        f = 0
    elseif n == 1
        f = 1;
    else
        f = fibonacci(n-1) + fibonacci(n-2);
    end
end