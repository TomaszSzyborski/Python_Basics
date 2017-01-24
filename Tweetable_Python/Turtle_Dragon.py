from turtle import*
def D(l,s,d):
 if l:rt(d);D(l-1,s/1.4,45);lt(d*2);D(l-1,s/1.4,-45);rt(d)
 else:fd(s)
D(8,600,45)