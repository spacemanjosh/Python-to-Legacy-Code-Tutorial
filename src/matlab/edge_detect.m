% :Description:
%    Read and image file and perform edge detection.
%
% :Params:
%    file1 [in, required, string] : Scalar string
%
% :Author: Josh Elliott : joshua.elliott@lasp.colorado.edu
%
% Apr 2, 2018 10:14:50 AM
function img = edge_detect(file1)
    
    img = imread(file1);
    img = img(:,:,1)
    img = edge(img, 'sobel');
    
end