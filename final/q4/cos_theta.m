## useage: values = cos_theta(VEC, MAT)
##
## VEC = 1 x n matrix (row vector)
## MAT = m x n
##
## Calculate the cosine of the angle between VEC and
## each row of MAT
function values = cos_theta (vec, mat)
  # values = dot(vec, mat) / (norm(vec) * norm(mat))
  [rows, cols] = size(mat);
  for i = 1: rows
    cur_row = mat(i, 1:cols);
    values(i, 1) = dot(vec,cur_row) / (norm(vec) * norm(cur_row));
  endfor
endfunction

%!test "unit vectors"
%!shared S,v,expected
%! S = [1,0;0,1];
%! v = [1/sqrt(2), 1/sqrt(2)];
%! expected = [1/sqrt(2);1/sqrt(2)];
%! assert(cos_theta(v,S),expected,eps)

%!test "scale vec"
%! assert(cos_theta(2*v,S),expected,eps)

%!test "scale set"
%! assert(cos_theta(v,3*S),expected,eps)

%!test "scale both"
%! assert(cos_theta(7*v,3*S),expected,eps)

%!test "different norms in set"
%! S2 = [1,1,1; 2,2,2; 3,3,3];
%! v2 = [1,0,1];
%! assert(cos_theta(v2,S2),sqrt(2)/sqrt(3)*ones(3,1),eps)
