module top_module (
input a,
input b,
input c,
input d,
output q );

assign q = (a&~c)|(a&~d)|(~a&b&d)|(~a&c&b)|(a&~b&c&d);

endmodule
