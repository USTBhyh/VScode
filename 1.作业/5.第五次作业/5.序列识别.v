/*同步HDLC成帧涉及解码连续的数据流，用来寻找指示帧的开始和结束的比特流模式。
若看到6个连续的1（即，01111110）是指示帧边界的“标志”。为避免数据流意外地包含“标志”，
发送方在数据中每5个连续1之后插入一个0，接收方在接收的数据中会检测到这个0并丢弃。
因此，如果有7个或更多连续的1，说明是错误，需给出出错信号。
创建一个有限状态机来识别这三个序列：
0111110：需要丢弃一个0（disc=1）。
01111110：标记帧的开始/结束（flag=1）。
01111111 ...：错误（7或更多个1）（err=1）。
当FSM复位时，它应处于前一个输入为0时的状态。
以下是一些说明所需操作的示例波形图。*/

module top_module(
    input clk,
    input reset,    // 高电平有效
    input in,
    output  reg disc,
    output  reg flag,
    output  reg err);

reg[3:0] present_state,next_state;
parameter S0=3'b000,S1=3'b001,S2=3'b010,S3=3'b011,S4=3'b100,S5=3'b101,S6=3'b110,S7=3'b111,S8=4'b1000;
//State registers
always @(posedge clk or posedge reset)
    begin
    if(reset)
        present_state<=S0;
    else
        present_state<=next_state;
end

always @(*)
 begin
    case(present_state)
      S0:if(in)
            next_state<=S0;
         else
            next_state<=S1;
      S1:if(in)
            next_state<=S2;
         else
            next_state<=S1;
      S2:if(in)
            next_state<=S3;
         else
            next_state<=S1;
      S3:if(in)
            next_state<=S4;
         else
            next_state<=S1;
      S4:if(in)
            next_state<=S5;
         else
            next_state<=S1;
      S5:if(in)
            next_state<=S6;
         else
            next_state<=S1; 
      S6:if(in)
            next_state<=S7;
         else
            next_state<=S1;
      S7:if(in)
            next_state<=S8;
         else
            next_state<=S1; 
      S8:if(in)
            next_state<=S8;
         else
            next_state<=S1;        
      default: next_state<=S0;
    endcase
end

always @(posedge clk or posedge reset)
    begin
        if(reset) begin
            disc<=0;flag<=0;err=0;
        end
        else begin
            if((present_state == S6)&&(in==0))
                disc<=1;
            else disc<=0;
            if((present_state == S7)&&(in==0))
                flag<=1;
            else flag<=0;
            if(((present_state == S7)||(present_state == S8))&&(in==1))
                err<=1;
            else err<=0;
        end
    end
/*assign disc=((present_state==S6)&&(in==0));
assign flag=((present_state==S7)&&(in==0));
assign err=((present_state==S7)&&(in==1));*/

endmodule