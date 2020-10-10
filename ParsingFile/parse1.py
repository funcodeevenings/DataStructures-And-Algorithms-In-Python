#Product:Version:Platform:System Requirements	
f= open("systemRequirements.txt","r")
f2=open("systemCompatibility.csv","w")
contents = f.readlines()
product,platform,version,x="PRODUCT","PLATFORM","VERSION","SYSTEM-COMPATIBILITY"
for line in contents:
    if line.__contains__("Version"):
        st= product+","+version+","+platform+","+x
        f2.write(st)
        f2.write("\n")
        x=""
        arr = line.split(":")
        product,version = ''.join(arr[0].split()),''.join(arr[2].split())
    if line.__contains__("System Requirements"):
        x=""
        arr = line.split(":")
        platform = ''.join(arr[1].split())
    if not line.__contains__("Version") and not line.__contains__("System Requirements"):
        x = x+''.join(line.split())
