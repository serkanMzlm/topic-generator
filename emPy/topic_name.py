import os
# import sys
# import argparse
import em
import re
import yaml

yaml_file = "topic_name.yml"
template_file = "topic_node.em"
output_file = "main.cpp"

with open(yaml_file, "r") as file:
    msg_map = yaml.safe_load(file)

merged_em = {}
all_surname = []

# for p in msg_map['pub']:
#     surname = p['name'].split("_")[-1]
#     surname_lower = re.sub(r'(?<!)(?=[A-Z])' + '_' + surname).lower()
#     all_surname.append(surname_lower)

merged_em['sub'] = msg_map['sub']
merged_em['pub'] = msg_map['pub']
# merged_em['pubr'] = msg_map['pub']


ofile = open(output_file, 'w')
interpreter = em.Interpreter(output=ofile, globals=merged_em, options={em.RAW_OPT: True, em.BUFFERED_OPT: True})
try:
    interpreter.file(open(template_file))
except OSError as e:
    ofile.close()
    os.remove(output_file)
    raise

interpreter.shutdown()
ofile.close()

