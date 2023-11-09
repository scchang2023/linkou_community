import xml.etree.ElementTree as et

tree=et.parse("country_data.xml")
root=tree.getroot()
for rank in root.iter("rank"):
    new_rank=int(rank.text)+1
    rank.text=str(new_rank)
    rank.set("updated","yes")
tree.write("country_data-output.xml",encoding="utf-8")
