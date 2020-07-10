from detect_cycle import *
file=open("schedule.txt","r");

lock=[];
dependencies=[];
size=file.readline();

for each in file:
    line=each[0];
    for word in each.split():
        if(word.startswith("X") or word.startswith("S")):
            lock.append(str(word[0]+str(line)+str(word[1:])));


for i in range(len(lock)):
    for j in range(i,len(lock)):
        if lock[i][1]!=lock[j][1] and lock[i][4]==lock[j][4] and lock[i][2]=='+' and lock[j][2]=="+":
            if lock[i][0]=="S" and lock[j][0]=="S":
                continue;
            dependencies.append((int(lock[i][1]),int(lock[j][1])));



V = int(size)
adj = [[] for i in range(V)]

for i in dependencies:
    addEdge(adj,int(i[0]),int(i[1]))


if isCyclicDisconnected(adj, V):
    print("system is in deadlock")
else:
    print("system is deadlock free")
