module top_module (
    input clk,
    input reset,
    input shift_ena,
    input count_ena,
    input data,
    output reg [3:0] q);

always @(posedge clk) begin
    if(reset)
        q<=0;
    else begin
        if(shift_ena)begin
            q[0]<=data;
            q[3:1]<=q[2:0];
        end
        else if (count_ena) begin
            q<=q-1;
        end
        else
        q<=q;
    end
end

endmodule