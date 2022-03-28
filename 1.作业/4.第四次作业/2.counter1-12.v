module top_module (
    input clk,
    input reset,
    input enable,
    output reg [3:0] Q
);

always @(posedge clk) begin
    if(reset)
        Q<=1'd1;
    if(enable && !reset)begin
    if(Q==4'b1100)
        Q<=1'd1;
    else
        Q<=Q+1'd1;
    end

end

endmodule