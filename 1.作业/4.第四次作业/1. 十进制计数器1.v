module top_module (
    input clk,
    input reset,
    output reg [3:0] q);

always @(posedge clk) begin
    if(reset)
        q<=1'd1;
    else
        q<=q+1'd1;
end

endmodule