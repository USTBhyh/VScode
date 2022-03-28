module top_module(
input [31:0] a,
input [31:0] b,
output [31:0] sum);

wire cout_cin;
wire cout;
add16 stag1(a[15:0],b[15:0],0,sum[15:0],cout_cin);
add16 stag2(a[31:16],b[31:16],cout_cin,sum[31:16],cout);

endmodule


module add1 (a,b,cin,sum,cout);  
	input a,b,cin;       
	output sum,cout;               
	reg sum,cout;             
	
	always @(a or b or cin)begin
		sum = a ^ b ^ cin;
		cout = a & b |(cin&(a^b));
	end
	
endmodule