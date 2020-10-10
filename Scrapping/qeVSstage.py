
fqe=open("pluginUpdatesQE.csv","r")
fstage=open("pluginUpdatesStage.csv","r")
fqs=open("pluginQEvsStage.csv","w")
for line1,line2 in zip(fqe,fstage):
    str = line1.strip()+","+line2.strip()
    fqs.write(str)
    fqs.write("\n")