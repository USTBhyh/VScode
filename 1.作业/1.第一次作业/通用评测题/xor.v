 module top_module (input in1,input in2,input in3,output out);
    wire nxor12;
    assign nxor12=~(in1^in2);
    assign out= nxor12^in3;
endmodule