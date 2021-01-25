%{/*definiciones*/
   #include<stdio.h>
%}
n	[0-9]
%%
{n}+		   {printf("<digito>");}
av		      {printf("<palabra reservada>");}
re		      {printf("<palabra reservada>");}
gd		      {printf("<palabra reservada>");}
gi		      {printf("<palabra reservada>");}
mt		      {printf("<palabra reservada>");}
ot		      {printf("<palabra reservada>");}
bp		      {printf("<palabra reservada>");}
regresa	   {printf("<palabra reservada>");}
repite		{printf("<palabra reservada>");}
%%
