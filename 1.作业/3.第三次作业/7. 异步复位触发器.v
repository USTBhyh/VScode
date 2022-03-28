module top_module (
    input clk,
    input d, 
    input ar,   // asynchronous reset
    output reg q);


/*always @(posedge clk) begin
    if(ar==0)
        q<=d;
end

always @(*) begin
    if(ar==1)
        q=0;
end*/

always @(posedge clk,posedge ar) begin
    if(ar)
        q<=0;
    else
        q<=d;
end

endmodule