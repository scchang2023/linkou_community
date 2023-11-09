import xml.etree.ElementTree as et

tree=et.parse("部落圖書資訊站.xml")
root=tree.getroot()
for lib in root.findall("DataA53000000A-000034-002"):
    LibraryName=lib.find("LibraryName").text
    County=lib.find("County").text
    Countryside=lib.find("Countryside").text
    print(LibraryName,County,Countryside)
    
  
# tree=et.parse("weatherReport1.xml")
# root=tree.getroot()
# xmlns="{urn:cwb:gov:tw:cwbcommon:0.1}"
# for location in root.iter(xmlns+"location"):
#     print(location.find(xmlns+"locationName").text)
#     for ti in location.iter(xmlns+"time"):
#         print(ti.find(xmlns+"dataTime").text,end=" ")
#         for ev in ti.iter(xmlns+"elementValue"):
#             print(ev.find(xmlns+"value").text,end="")
#         print()