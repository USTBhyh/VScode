module top_module(
input [31:0] a,
input [31:0] b,
output [31:0] sum );

wire cout;
wire cout1,cout2;
wire [15:0]sum1;
wire [15:0]sum2;
add16 stag1(a[15:0],b[15:0],0,sum[15:0],cout);
add16 stag2(a[31:16],b[31:16],0,sum1[15:0],cout1);
add16 stag3(a[31:16],b[31:16],1,sum2[15:0],cout2);
sel2to1 stag4(sum1,sum2,cout,sum[31:16]);

endmodule

module sel2to1(
input [15:0]sum1,
input [15:0]sum2,
input sel,
output reg [15:0]sum
);

always @(*) begin
    case(sel)
        1'b0:sum=sum1;
        1'b1:sum=sum2;
    endcase
end

endmodule