import xml.etree.ElementTree

e = xml.etree.ElementTree.parse('DrugBank\Abacavir.xml').getroot()
for atype in e.findall('sentence'):
    for entity in atype:
        print(entity.get('id'))
# print(e)
