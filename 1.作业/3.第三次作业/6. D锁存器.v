module top_module (
    input d, 
    input ena,
    output reg q);
initial q=0;
always @(ena,d) begin
    case(ena)
        1'b1:q=d;
    endcase
end

endmodule