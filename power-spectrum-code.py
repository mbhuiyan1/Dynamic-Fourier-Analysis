import numpy as np;


def getIndicesAsList(v,a_range):
	indicesList=[];
	for i in xrange(0,len(v)):
		if a_range[0]<=v[i] and v[i]<=a_range[1]:
			indicesList.append(i);
	return indicesList;


def getPercentageOfSelectedCells(z,validRowIndices,validColIndices):
	
	#print validRowIndices;
	#print validColIndices;
	z2=z[validRowIndices,:];
	z3=z2[:,validColIndices];
	return 100.0*np.sum(z3)/np.sum(z);
	
	
#main method

##########################(0-2000)
print "\n time for (0-2000)\n";
#parameter settings
x_range=[0,2];
y_range=[0,2000];


#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[2.0000001,4];
y_range=[0,2000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[4.0000001,6];
y_range=[0,2000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[6.0000001,8];
y_range=[0,2000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[8.0000001,10];
y_range=[0,2000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";


##########################(2000-4000)
print "\n time for (2001-4000) \n";
#parameter settings
x_range=[0,2];
y_range=[2001,4000];


#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[2.0000001,4];
y_range=[2001,4000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[4.0000001,6];
y_range=[2001,4000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[6.0000001,8];
y_range=[2001,4000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[8.0000001,10];
y_range=[2001,4000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";


##########################(4001-6000)
print "\n time for (4001-6000) \n";
#parameter settings
x_range=[0,2];
y_range=[4001,6000];


#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[2.0000001,4];
y_range=[4001,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[4.0000001,6];
y_range=[4001,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[6.0000001,8];
y_range=[4001,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[8.0000001,10];
y_range=[4001,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";


##########################(0-6000)
print " \n time for (0-6000) \n ";
#parameter settings
x_range=[0,2];
y_range=[0,6000];


#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[2.0000001,4];
y_range=[0,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[4.0000001,6];
y_range=[0,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[6.0000001,8];
y_range=[0,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";

x_range=[8.0000001,10];
y_range=[0,6000];
#reading input files
z=np.genfromtxt("z.csv",delimiter=',',skip_header=1);
z=z[:,1:];

x=np.genfromtxt("x.csv",delimiter=',',skip_header=1);
x=x[:,1];


y=np.genfromtxt("y.csv",delimiter=',',skip_header=1);
y=y[:,1];

#end reading files


validRowIndices=getIndicesAsList(x,x_range);
validColIndices=getIndicesAsList(y,y_range);

print getPercentageOfSelectedCells(z,validRowIndices,validColIndices),"%";











