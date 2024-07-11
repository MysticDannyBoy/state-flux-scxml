# 2024. 07. 11. 14:01:45, MysticDannyBoy
# Az alap kódot a ChatGPT írta.
# Én csak magyarítottam. 
import xml.etree.ElementTree as ET

# Beolvassuk a fájlt
tree = ET.parse('statechart.scxml')
root = tree.getroot()

# Access elements
for state in root.findall('state'):
    print('State ID:', state.get('id'))
    for transition in state.findall('transition'):
        print('Transition Event:', transition.get('event'))
        print('Transition Target:', transition.get('target'))