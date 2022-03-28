module top_module(
    input clk,
    input areset,    // Asynchronous reset to state B
    input in,
    output out);

reg y;
parameter A =1'b0,B=1'b1 ;
initial y=B;
always @(posedge clk)begin
    if(areset)
       y<=B;
    else begin
        case(y)
            A:if(!in) y<=B;else y<=A;
            B:if(!in) y<=A;else y<=B;
        endcase 
    end
end

assign out=y;

endmodule