import os
import sys
import argparse
import em
import re
import yaml

parser = argparse.ArgumentParser()

parser.add_argument('-y', '--yaml-file', dest='yaml_file', type=str, 
                    default=None, help="yaml file location")
parser.add_argument('-t', '--template-file', dest='template_file', type=str,
                    default=None, help="enter template file")
parser.add_argument("-u", "--outdir", dest='outdir', type=str,
                    help="file output dir", default=None)

if len(sys.argv) <= 1:
    parser.print_usage()
    exit(-1)

args = parser.parse_args()
template_file = os.path.join(args.template_file)
out_dir = os.path.abspath(args.outdir)

if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

output_file = os.path.join(out_dir, os.path.basename(template_file).replace(".em", ""))

with open(args.yaml_file, 'r') as file:
    msg_map = yaml.safe_load(file);

merged_em = {}
all_type_includes = []

for p in msg_map['publications']:
    base_type = p['type'].split('::')[-1]
    base_type_name_snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_',base_type).lower()
    all_type_includes.append(base_type_name_snake_case)

for s in msg_map['subscriptions']:
    base_type = s['type'].split('::')[-1]
    base_type_name_snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_',base_type).lower()
    all_type_includes.append(base_type_name_snake_case)

merged_em['subscriptions'] = msg_map['subscriptions']
merged_em['publications'] = msg_map['publications']
merged_em['type_includes'] = sorted(set(all_type_includes))

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