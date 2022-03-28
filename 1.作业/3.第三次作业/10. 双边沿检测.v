module top_module (
    input clk,
    input [7:0] in,
    output reg [7:0] anyedge=8'b0000_0000
);

    reg [7:0] in_ori=8'b0000_0000;
    always@(posedge clk)begin
        in_ori <= in;
    end
    
    always@(posedge clk)begin
        anyedge <= in ^ in_ori;
    end
 
endmodule