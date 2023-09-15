import os
import sys
import argparse
import em
import re
import yaml

yaml_file = "topic_names.yml"
template_file = "dynamic_topic.hpp.em"
output_file = "main.cpp"

with open(yaml_file, 'r') as file:
    msg_map = yaml.safe_load(file);

merged_em = {}
all_surname = []



merged_em['subscriptions'] = msg_map['subscriptions']
merged_em['publications'] = msg_map['publications']

o_file = open(output_file, 'w')
interpreter = em.Interpreter(output=o_file, globals=merged_em, options={em.RAW_OPT: True, em.BUFFERED_OPT: True})

try:
    interpreter.file(open(template_file))
except OSError as e:
    o_file.close()
    os.remove(output_file)
    raise

interpreter.shutdown()
o_file.close()