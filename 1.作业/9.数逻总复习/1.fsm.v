module top_module(
    input clk,
    input areset,    // Asynchronous reset to state B
    input in,
    output out);

parameter A =0,B=1 ;
reg present_state,next_state;

always @(posedge clk,posedge areset) begin
    if(areset)
        present_state<=B;
    else
        present_state<=next_state;
end

always @(in) begin
    case(present_state) 
        A:if(in) next_state<=A;else next_state<=B;
        B:if(in) next_state<=B;else next_state<=A;    
    endcase
end

assign out=present_state;

endmodule