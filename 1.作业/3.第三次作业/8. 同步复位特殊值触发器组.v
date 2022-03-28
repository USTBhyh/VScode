module top_module (
    input clk,
    input reset,
    input [7:0] d,
    output reg [7:0] q
);

always @(negedge clk) begin
    if(!reset)
        q<=d;
    else
        q=8'b0011_0100;
end

endmodule