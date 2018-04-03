function edge_detect, file
  compile_opt idl2
  
  read_jpeg, file, img
  dim = img.DIM
  for i=0, 2 do begin
    img[i,*,*] = sobel(reform(img[i,*,*], dim[1], dim[2]))
  endfor
  return, img
end
