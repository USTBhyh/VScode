module top_module(
    input clk,
    input areset,    // Freshly brainwashed Lemmings walk left.
    input bump_left,
    input bump_right,
    output  walk_left,
    output  walk_right);

    parameter LEFT=1'b0, RIGHT=1'b1;
    reg state, next_state;

    always @(*) begin
        case(state)     // State transition logic
            LEFT:begin
            if( bump_left == 1'b1 )
                next_state <= RIGHT;
            else
                next_state <= LEFT;   
            end    
            RIGHT:begin
            if( bump_right == 1'b1 )
                next_state <= LEFT;
            else
                next_state <= RIGHT;   
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

endmodule