module top_module (
    input clk,
    input w, R, E, L,
    output reg Q
);

initial Q=0;
wire out1,out2;
sel2to1 stag1(w,Q,E,out1);
sel2to1 stag2(R,out1,L,out2);
always @(posedge clk) begin
    Q<=out2;
end

endmodule


module sel2to1 (
    input in1,
    input in2,
    input sel,
    output out
);

assign  out=sel?in1:in2;//(in1&sel)|(b&(~sel));

endmodule

