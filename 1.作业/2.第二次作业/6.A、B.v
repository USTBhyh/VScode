 module top_module (
    input x, 
    input y, 
    output z);

   wire a,b,z1,z2,z3,z4;

    A IA1(x,y,z1);
    B IB1(x,y,z2);
    A IA2(x,y,z3);
    B IB2(x,y,z4);

    or(a,z1,z2);
    and(b,z3,z4);
    xor(z,a,b);

 endmodule