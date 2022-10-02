##CAPITULO 1, 2, 3

the_world=True;
if the_world:
    print("hello...");
a=12;
a=a*10;
print(round(2, 2));
for _ in range(5):
    print(_);

word="Ejemplo";
print("e1="+word[1:3]);

print("e2="+word[:]);
#print(word[10]);

cad=[1,7,9,10,12];
print (cad);
cad[0]=101;
print (cad);
longitud=len(cad);

print(longitud);

#fibunacci
a, b = 0,1;
print (str(a)+" - " + str(b));

serie=[];
while(a < 10):
    serie.append(a);
    print("serie:"+str(a));
    c=a;
    a=b;
    b=a+c;
    print(a, end=",");
    
    #print("-serie:"+str(b));
    #a, b = b, a+b;
print("final="+str(serie));

#fin fibunacci


exit();