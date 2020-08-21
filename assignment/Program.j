.class public Program
.super java/lang/Object
.method public <init>()V
aload_0
invokenonvirtual java/lang/Object/<init>()V
return
.end method
.method public static main([Ljava/lang/String;)V
.limit locals 2
.limit stack 1024
new java/util/Scanner
dup
getstatic java/lang/System.in Ljava/io/InputStream;
invokespecial java/util/Scanner.<init>(Ljava/io/InputStream;)V
astore 0
sipush 2
istore 1
iload 1
sipush 3
if_icmpge l1
iload 1
sipush 2
if_icmpge l3
sipush 1
istore 1
l3:
sipush 4
istore 1
l4:
l1:
iload 1
sipush 9
if_icmple l5
iload 1
sipush 8
if_icmple l7
iload 1
sipush 0
if_icmpeq l9
sipush 0
istore 1
l9:
sipush 1
istore 1
l10:
l7:
sipush 2
istore 1
l8:
l5:
sipush 3
istore 1
l6:
l2:
return
.end method
