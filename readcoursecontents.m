file='Course14.txt';

fid=fopen(file,'r');
TEXT=fscanf(fid,'%c');
fclose(fid);


%%
a=regexp(TEXT,'XP');
b=[0 regexp(TEXT,'\n')];

c=cell(length(a),2);

for i=1:length(c)
   d=b(b<a(i)); 
   e=b(b>a(i));
   d2=d(end-2);
   e2=d(end);
   d=d(end);
   e=e(1);
   c{i,1}=TEXT(d+1:e-1);
   c{i,2}=TEXT(d2+2:e2-1);
end

A=strcmp('100 XP',c(:,1));
c=c(A,:);
for i=1:size(c,1)
   a=regexp(c{i,2},'\s');
   c{i,2}(a)='_';
   a=regexp(c{i,2},'[a-zA-Z0-9_]');
   WEP=num2str(i);
   if length(WEP)==1
      WEP=['0',WEP]; 
   end
   WEP=['E',WEP,'_'];
   c{i,2}=[WEP,c{i,2}(a),'.py'];
end

%%
%p='/Users/David/Dropbox/Python3/git/Datacamp/';
p='/Volumes/Data/Dropbox/Python3/git/Datacamp/';
%%
for i=1:size(c,1)
    fid=fopen([p,'Interactive_Data_Visualization_with_Bokeh/',c{i,2}],'w+');
    fclose(fid);
end
