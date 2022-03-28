080497d3 <func4>:
 80497d3:	f3 0f 1e fb          	endbr32 
 80497d7:	55                   	push   %ebp
 80497d8:	89 e5                	mov    %esp,%ebp
 80497da:	83 ec 18             	sub    $0x18,%esp


 80497dd:	8b 55 0c             	mov    0xc(%ebp),%edx      //x->edx
 80497e0:	8b 45 10             	mov    0x10(%ebp),%eax     //y->eax
 80497e3:	01 d0                	add    %edx,%eax
 80497e5:	89 c2                	mov    %eax,%edx   //求和，edx=x+y
 80497e7:	c1 ea 1f             	shr    $0x1f,%edx    //31，右移取最高位用来判断x+y的正负
 80497ea:	01 d0                	add    %edx,%eax        //eax=edx+eax=x+y+sign(x+y)
 80497ec:	d1 f8                	sar    %eax             //右移eax=(x+y+sign(x+y))/2
 80497ee:	89 45 ec             	mov    %eax,-0x14(%ebp)
 80497f1:	8b 45 0c             	mov    0xc(%ebp),%eax    //x->eax
 80497f4:	3b 45 10             	cmp    0x10(%ebp),%eax   //x y比较


 80497f7:	7c 13                	jl     804980c <func4+0x39>   //x<y
 80497f9:	8b 45 10             	mov    0x10(%ebp),%eax     //y->eax
 80497fc:	8d 14 85 00 00 00 00 	lea    0x0(,%eax,4),%edx   //edx=eax*4
 8049803:	8b 45 08             	mov    0x8(%ebp),%eax
 8049806:	01 d0                	add    %edx,%eax
 8049808:	8b 00                	mov    (%eax),%eax





 
 804980a:	eb 3c                	jmp    8049848 <func4+0x75>
 804980c:	83 ec 04             	sub    $0x4,%esp
 804980f:	ff 75 ec             	pushl  -0x14(%ebp)
 8049812:	ff 75 0c             	pushl  0xc(%ebp)
 8049815:	ff 75 08             	pushl  0x8(%ebp)
 8049818:	e8 b6 ff ff ff       	call   80497d3 <func4>
 804981d:	83 c4 10             	add    $0x10,%esp
 8049820:	89 45 f0             	mov    %eax,-0x10(%ebp)
 8049823:	8b 45 ec             	mov    -0x14(%ebp),%eax
 8049826:	83 c0 01             	add    $0x1,%eax
 8049829:	83 ec 04             	sub    $0x4,%esp
 804982c:	ff 75 10             	pushl  0x10(%ebp)
 804982f:	50                   	push   %eax
 8049830:	ff 75 08             	pushl  0x8(%ebp)
 8049833:	e8 9b ff ff ff       	call   80497d3 <func4>
 8049838:	83 c4 10             	add    $0x10,%esp
 804983b:	89 45 f4             	mov    %eax,-0xc(%ebp)
 804983e:	8b 45 f4             	mov    -0xc(%ebp),%eax
 8049841:	39 45 f0             	cmp    %eax,-0x10(%ebp)
 8049844:	0f 4d 45 f0          	cmovge -0x10(%ebp),%eax
 8049848:	c9                   	leave  
 8049849:	c3                   	ret    