module top_module(
    input in,
    input [1:0] state,
    output reg [1:0] next_state,
    output out);

parameter A = 2'b00,B = 2'b01,C = 2'b10,D = 2'b11;
always @(*)begin
    case (state)
        A:if(in) next_state<=B;else next_state<=A;
        B:if(!in) next_state<=C;else next_state<=B;
        C:if(in) next_state<=D;else next_state<=A;
        D:if(in) next_state<=B;else next_state<=C;
        default: next_state<=state;
endcase
end

assign out=(state==D)?1:0;

endmodule