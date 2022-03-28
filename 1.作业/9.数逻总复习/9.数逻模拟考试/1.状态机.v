module top_module (
    input clk,
    input reset,   // 高电平有效，同步复位
    input x,
    output z
);

parameter a =3'b000,b=3'b001,c=3'b010,d=3'b011,e=3'b100 ;
reg [2:0]present_state,next_state;

always @(posedge clk, posedge reset) begin
        if(reset)
            present_state <= a;
        else
            present_state <= next_state;
    end

always @(*) begin
case (present_state)
    a:
    if(x)next_state<=a;
    else next_state<=b;
    b:
    if(x)next_state<=b;
    else next_state<=e;
    c:
    if(x)next_state<=c;
    else next_state<=b;
    d:
    if(x)next_state<=b;
    else next_state<=c;
    e: 
    if(x)next_state<=d;
    else next_state<=e;
    default: next_state<=present_state;
endcase       
end

assign z=(present_state==d||present_state==d);

endmodule