module top_module (
    input [7:0] a, b, c, d,
    output [7:0] min);

    wire [7:0] out_t0;
    wire [7:0] out_t1;
    assign out_t0 = (a<b)?a:b; 
    assign out_t1 = (c<d)?c:d;
    assign min = (out_t0<out_t1) ? out_t0:out_t1;

endmodule