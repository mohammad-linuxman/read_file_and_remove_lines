
with open("menu.php" , 'r') as infile:

        i=[]
        for line in infile:
            i.append(line)

with open("menu.php" , 'w') as ifile:

        x='2115';
        y='2115';

        count=0;
        for line1 in i:
            count=count+1;
            #if line1[:-1] not in (y , x ):
            if  count not in (2115,2116) :
               ifile.write(line1)

        ifile.close()
