module counter(
    input clk,              //时钟信号
    input rst,              //重置控制信号
    output clk_bps          //时钟信号间隔（计数周期）
    );
        reg [13:0]cnt_first,cnt_second;
        always @(posedge clk or posedge rst)    //clk上升沿或者rst上升沿
            if(rst)         //rst==1
                cnt_first<=14'd0;
            else if(cnt_first==14'd10000)       //14‘10000——十进制数10000
                cnt_first<=14'd0;
            else
                cnt_first<=cnt_first +1'b1;     //二进制寄存器cnt_first加一位二进制数1
        always @(posedge clk or posedge rst)    //clk上升沿或者rst上升沿
            if(rst)         //rst==1
                cnt_second<=14'd0;
            else if(cnt_second ==14'd10000)
                cnt_second<=14'd0;
            else if(cnt_first==14'd10000)
                cnt_second<=cnt_second+1'b1;    //二进制寄存器cnt_second加一位二进制数1
        assign clk_bps=cnt_second==14'd10000 ? 1'b1 : 1'b0;   //给clk_bps赋值（根据cnt_second的值） 
endmodule