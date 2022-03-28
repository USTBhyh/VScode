0804984a <phase_4>:
 804984a:	f3 0f 1e fb          	endbr32 
 804984e:	55                   	push   %ebp
 804984f:	89 e5                	mov    %esp,%ebp
 8049851:	57                   	push   %edi
 8049852:	56                   	push   %esi
 8049853:	53                   	push   %ebx
 8049854:	81 ec ec 00 00 00    	sub    $0xec,%esp   236


 804985a:	8b 45 08             	mov    0x8(%ebp),%eax
 804985d:	89 85 14 ff ff ff    	mov    %eax,-0xec(%ebp)
 8049863:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax


 8049869:	89 45 e4             	mov    %eax,-0x1c(%ebp)
 804986c:	31 c0                	xor    %eax,%eax


 804986e:	8d 85 24 ff ff ff    	lea    -0xdc(%ebp),%eax
 8049874:	bb 40 b2 04 08       	mov    $0x804b240,%ebx     “2”密码地址//  50
 8049879:	ba 30 00 00 00       	mov    $0x30,%edx           //48

？？？
 804987e:	89 c7                	mov    %eax,%edi
 8049880:	89 de                	mov    %ebx,%esi
 8049882:	89 d1                	mov    %edx,%ecx
 8049884:	f3 a5                	rep movsl %ds:(%esi),%es:(%edi)


 8049886:	8d 85 1c ff ff ff    	lea    -0xe4(%ebp),%eax    //num2
 804988c:	50                   	push   %eax
 804988d:	8d 85 18 ff ff ff    	lea    -0xe8(%ebp),%eax    //num1
 8049893:	50                   	push   %eax
 8049894:	68 fc b1 04 08       	push   $0x804b1fc       输入两个整数
 8049899:	ff b5 14 ff ff ff   	pushl  -0xec(%ebp)
 804989f:	e8 4c f9 ff ff       	call   80491f0 <__isoc99_sscanf@plt>
 80498a4:	83 c4 10             	add    $0x10,%esp      
 80498a7:	89 85 20 ff ff ff    	mov    %eax,-0xe0(%ebp)
 80498ad:	83 bd 20 ff ff ff 02 	cmpl   $0x2,-0xe0(%ebp)   eax和2比较 
 80498b4:	74 0f                	je     80498c5 <phase_4+0x7b> 如果eax==2就跳
 80498b6:	e8 42 08 00 00       	call   804a0fd <explode_bomb>
 80498bb:	b8 00 00 00 00       	mov    $0x0,%eax   
 80498c0:	e9 bc 00 00 00       	jmp    8049981 <phase_4+0x137>


 80498c5:	8b 95 1c ff ff ff    	mov    -0xe4(%ebp),%edx     //num2
 80498cb:	8b 85 18 ff ff ff    	mov    -0xe8(%ebp),%eax     //num1
 80498d1:	83 ec 04             	sub    $0x4,%esp  //esp-4
 80498d4:	52                   	push   %edx
 80498d5:	50                   	push   %eax


 80498d6:	8d 85 24 ff ff ff    	lea    -0xdc(%ebp),%eax       //50    
 80498dc:	50                   	push   %eax
 80498dd:	e8 f1 fe ff ff       	call   80497d3 <func4>  //调用函数


 80498e2:	83 c4 10             	add    $0x10,%esp   //esp+10
 80498e5:	3d b3 00 00 00       	cmp    $0xb3,%eax              //==179      b 4
 80498ea:	74 0f                	je     80498fb <phase_4+0xb1>
 80498ec:	e8 0c 08 00 00       	call   804a0fd <explode_bomb>
 80498f1:	b8 00 00 00 00       	mov    $0x0,%eax
 80498f6:	e9 86 00 00 00       	jmp    8049981 <phase_4+0x137>


 80498fb:	8b 85 18 ff ff ff    	mov    -0xe8(%ebp),%eax   //num1
 8049901:	85 c0                	test   %eax,%eax 
 8049903:	7e 36                	jle    804993b <phase_4+0xf1>  <=
 8049905:	8b 85 1c ff ff ff    	mov    -0xe4(%ebp),%eax  
 804990b:	8b 95 18 ff ff ff    	mov    -0xe8(%ebp),%edx
 8049911:	83 ea 01             	sub    $0x1,%edx        //num1-1              48-1=47
 8049914:	83 ec 04             	sub    $0x4,%esp
 8049917:	50                   	push   %eax   //num2
 8049918:	52                   	push   %edx   //num1-1


 8049919:	8d 85 24 ff ff ff    	lea    -0xdc(%ebp),%eax
 804991f:	50                   	push   %eax
 8049920:	e8 ae fe ff ff       	call   80497d3 <func4>
 8049925:	83 c4 10             	add    $0x10,%esp
 8049928:	3d b3 00 00 00       	cmp    $0xb3,%eax  179
 804992d:	75 0c                	jne    804993b <phase_4+0xf1>     //!=179
 804992f:	e8 c9 07 00 00       	call   804a0fd <explode_bomb>
 8049934:	b8 00 00 00 00       	mov    $0x0,%eax
 8049939:	eb 46                	jmp    8049981 <phase_4+0x137>


 804993b:	8b 85 1c ff ff ff    	mov    -0xe4(%ebp),%eax     //num2
 8049941:	83 f8 2e             	cmp    $0x2e,%eax    //46
 8049944:	7f 36                	jg     804997c <phase_4+0x132>   //num2>46跳转


 8049946:	8b 85 1c ff ff ff    	mov    -0xe4(%ebp),%eax     //num2
 804994c:	8d 50 01             	lea    0x1(%eax),%edx           //-0xe5(%ebp)
 804994f:	8b 85 18 ff ff ff    	mov    -0xe8(%ebp),%eax      //num1
 8049955:	83 ec 04             	sub    $0x4,%esp
 8049958:	52                   	push   %edx
 8049959:	50                   	push   %eax
 804995a:	8d 85 24 ff ff ff    	lea    -0xdc(%ebp),%eax
 8049960:	50                   	push   %eax
 8049961:	e8 6d fe ff ff       	call   80497d3 <func4>  //-0xdc(%ebp)


 8049966:	83 c4 10             	add    $0x10,%esp
 8049969:	3d b3 00 00 00       	cmp    $0xb3,%eax    //179
 804996e:	75 0c                	jne    804997c <phase_4+0x132>  //!179
 8049970:	e8 88 07 00 00       	call   804a0fd <explode_bomb>
 8049975:	b8 00 00 00 00       	mov    $0x0,%eax
 804997a:	eb 05                	jmp    8049981 <phase_4+0x137>


 804997c:	b8 01 00 00 00       	mov    $0x1,%eax   // ==1
 8049981:	8b 4d e4             	mov    -0x1c(%ebp),%ecx

 //堆栈金丝雀
 8049984:	65 33 0d 14 00 00 00 	xor    %gs:0x14,%ecx
 804998b:	74 05                	je     8049992 <phase_4+0x148>
 804998d:	e8 fe f7 ff ff       	call   8049190 <__stack_chk_fail@plt>
 8049992:	8d 65 f4             	lea    -0xc(%ebp),%esp
 8049995:	5b                   	pop    %ebx
 8049996:	5e                   	pop    %esi
 8049997:	5f                   	pop    %edi
 8049998:	5d                   	pop    %ebp
 8049999:	c3                   	ret    
