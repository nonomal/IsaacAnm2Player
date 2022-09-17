from glob import glob
from operator import indexOf
import skin_alt_gen
import tqdm
import xml.etree.ElementTree as ET

maps = skin_alt_gen.costume_maps

png_files = []

for costume_name in maps:
    m = maps[costume_name]
    for png in m.values():
        png_files.append([png.split('\\')[-1],costume_name])

tainted_anm2 = []

def parse_anm(anmpath):
    with open(anmpath, 'r',encoding='utf8') as f:
        txt = f.read()
        for png in png_files:
            if txt.find(png[0]) != -1:
                tainted_anm2.append([anmpath.split("\\")[-1],png[1]])
                break

for f in tqdm.tqdm(glob(skin_alt_gen.folder + "resources\\**\\*.anm2", recursive=True),"find resources anm2"):
    parse_anm(f)
for f in tqdm.tqdm(glob(skin_alt_gen.folder + "resources-dlc3\\**\\*.anm2", recursive=True),"find resources-dlc3 anm2"):
    parse_anm(f)

namemap = {
    "none":"n","passive":"c","familiar":"c","active":"c","trinket":"t"
}

with open(skin_alt_gen.folder + "resources-dlc3\\costumes2.xml", "r") as f:
    for ch in ET.parse(f).getroot():
        anm2path = ch.attrib["anm2path"].split('\\')[-1]
        for anm in tainted_anm2:
            if anm[0] == anm2path:
                print(f'{namemap[ch.attrib["type"]]}{ch.attrib["id"]}\t{anm[1]}')