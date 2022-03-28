module top_module(
    input clk,
    input areset,    // Freshly brainwashed Lemmings walk left.
    input bump_left,
    input bump_right,
    input ground,
    input dig,
    output walk_left,
    output walk_right,
    output aaah,
    output digging );

parameter LEFT=3'b000, RIGHT=3'b001,AH_LEFT=3'b010,AH_RIGHT=3'b011,DIG_LEFT=3'b100,DIG_RIGHT=3'b101;
    reg [2:0] state, next_state;
    wire [1:0] bump; 
    
    assign bump = {bump_left,bump_right};
    
    always @(*) begin
        case(state)     // State transition logic
            LEFT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_LEFT;
            else if( dig ==1'b1 ) 
                next_state <= DIG_LEFT;    
            else if( bump == 2'b10 || bump == 2'b11)
                next_state <= RIGHT;
            else
                next_state <= LEFT;   
            end  
            RIGHT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_RIGHT;
            else if( dig ==1'b1 ) 
                next_state <= DIG_RIGHT;      
            else if( bump == 2'b01 || bump == 2'b11)
                next_state <= LEFT;
            else
                next_state <= RIGHT;   
            end 
            AH_LEFT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_LEFT;
            else
                next_state <= LEFT;   
            end    
            AH_RIGHT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_RIGHT;
            else
                next_state <= RIGHT;   
            end
            DIG_LEFT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_LEFT;
            else
                next_state <= DIG_LEFT;   
            end 
            DIG_RIGHT:begin
            if( ground ==1'b0 ) 
                next_state <= AH_RIGHT;
            else
                next_state <= DIG_RIGHT;   
            end      
        endcase
    end    

    always @(posedge clk, posedge areset) begin
        if(areset)
            state <= LEFT;
        else
            state <= next_state;// State flip-flops with asynchronous reset
    end

    // Output logic
    assign walk_left = (state == LEFT);
    assign walk_right = (state == RIGHT);
    assign aaah = ((state == AH_LEFT) || (state == AH_RIGHT));
    assign digging = ((state == DIG_LEFT) || (state == DIG_RIGHT));

endmodule