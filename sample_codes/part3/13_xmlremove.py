import xml.etree.ElementTree as et

tree=et.parse("country_data.xml")
root=tree.getroot()
for country in root.findall("country"):
    rank=int(country.find("rank").text)
    if rank>50:
        root.remove(country)
tree.write("country_data_remove.xml",encoding="utf-8")
