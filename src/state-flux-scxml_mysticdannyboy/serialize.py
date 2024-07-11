# 2024. 07. 11. 14:01:45, MysticDannyBoy
# Az alap kódot a ChatGPT írta.
# Én csak magyarítottam. 
import xml.etree.ElementTree as ET

# Létrehozzuk az SCXML struktúrát
scxml = ET.Element('scxml', version='1.0')
state = ET.SubElement(scxml, 'state', id='state1')
transition = ET.SubElement(state, 'transition', event='event1', target='state2')

# Serialize to string
scxml_string = ET.tostring(scxml, encoding='unicode')

# Write to file
with open('statechart.scxml', 'w') as f:
    f.write(scxml_string)