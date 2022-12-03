function jyxl(k1,k2,k0) 
k=k1:-k0-1;
kk=-k0:k2;
n=length(k);
nn=length(kk);
u=zeros(1,n);
uu=ones(1,nn);
stem(kk,uu,'filled')
hold on
stem(k,u,'filled')
hold off
axis([k1,k2,0,1.5])
title('单位阶跃序列')

