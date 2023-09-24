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
    msg_map = yaml.safe_load(file)

merged = {}
include = {}
ros2_includes = []

def process_message_type(msg_type):
	base_type = msg_type['type'].split('::')[-1]
	snake_case_type = re.sub(r'(?<!^)(?=[A-Z])', '_', base_type).lower()
	include_path = "/".join(msg_type['type'].split('::')[:-1]) + "/" + snake_case_type
	if include_path in include:
		return
	include[include_path] = [snake_case_type, msg_type]      

for sub in msg_map['subscriptions']:
	process_message_type(sub)

for pub in msg_map['publications']:
	process_message_type(pub)     
 
merged['subscriptions'] = msg_map['subscriptions']
merged['includes'] = include

o_file = open(output_file, 'w')
interpreter = em.Interpreter(output=o_file, globals=merged, 
                            options={em.RAW_OPT: True, em.BUFFERED_OPT: True})

try:
    interpreter.file(open(template_file))
except OSError as e:
    o_file.close()
    os.remove(output_file)
    raise

interpreter.shutdown()
o_file.close()
