import xml.etree.ElementTree as et

tree=et.parse("menu.xml")
root=tree.getroot()
print(root.tag)
for child in root:
    print(f"tag:{child.tag},attributes:{child.attrib}")
    for grandchild in child:
        print(f"\ttag:{grandchild.tag},attributes:{grandchild.attrib},text:{grandchild.text}")
print(len(root))     
print(len(root[0]))  