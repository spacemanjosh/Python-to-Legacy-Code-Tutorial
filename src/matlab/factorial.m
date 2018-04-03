% :Description:
%    Recursive function to compute the Nth factorial.
%
% :Params:
%    n [in, required, int] : Scalar integer
%
% :Author: Josh Elliott : joshua.elliott@lasp.colorado.edu
%
% Apr 2, 2018 10:14:50 AM
function f = factorial(n)
    f = 0;
    if n == 0 || n == 1
        f = 1;
    else
        f = n * factorial(n-1);
    end
end