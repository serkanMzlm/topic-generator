import os
import sys
import argparse
import em
import re
import yaml

parser = argparse.ArgumentParser()

parser.add_argument('-y', '--yaml-file', dest='yaml_file', type=str, 
                    default=None, help="yaml file location")
parser.add_argument('-t', '--template-declaration', dest='declaration_file', type=str,
                    default=None, help="enter template declaration file")
parser.add_argument('-T', '--template-definition', dest='definition_file', type=str,
                    default=None, help="enter template definition file")
parser.add_argument("-u", "--outdir-declaration", dest='declaration_outdir', type=str,
                    help="file output declaration dir", default=None)
parser.add_argument("-U", "--outdir-definition", dest='definition_outdir', type=str,
                    help="file output definition dir", default=None)

if len(sys.argv) <= 1:
    parser.print_usage()
    exit(-1)

args = parser.parse_args()
declaration_file = os.path.join(args.declaration_file)
declaration_dir  = os.path.abspath(args.declaration_outdir)

definition_file  = os.path.join(args.definition_file)
definition_dir   = os.path.abspath(args.definition_outdir)

if not os.path.isdir(declaration_dir):
    os.makedirs(declaration_dir)

if not os.path.isdir(definition_dir):
    os.makedirs(definition_dir)

output_declaration_file = os.path.join(declaration_dir, os.path.basename(declaration_file).replace(".em", ""))
output_definition_file  = os.path.join(definition_dir, os.path.basename(definition_file).replace(".em", ""))

with open(args.yaml_file, 'r') as file:
    msg_map = yaml.safe_load(file)

merged = {}

include = {}
pub = {}
sub = {}
          
def process_message_type(msg_type):
    base_type = msg_type['type'].split('::')[-1]
    snake_case_type = re.sub(r'(?<!^)(?=[A-Z])', '_', base_type).lower()
    include_path = "/".join(msg_type['type'].split('::')[:-1]) + "/" + snake_case_type
    if include_path not in include:
        include[include_path] = [snake_case_type, msg_type] 
    return snake_case_type 


for sub_ in msg_map['subscriptions']:
	# sub[process_message_type(sub_)] = [msg_map['subscriptions'], sub_]
	sub[process_message_type(sub_)] =  sub_

for pub_ in msg_map['publications']:
    pub[process_message_type(pub_)] =  pub_

merged['includes']      = include
merged['subscriptions'] = sub
merged['publications']  = pub

merged2 = merged

o_dec_file = open(output_declaration_file, 'w')
o_def_file = open(output_definition_file, 'w')

interpreter_dec = em.Interpreter(output=o_dec_file, globals=merged, 
                            options={em.RAW_OPT: True, em.BUFFERED_OPT: True})
interpreter_def = em.Interpreter(output=o_def_file, options={em.RAW_OPT: True, 
                                                             em.BUFFERED_OPT: True})

try:
    interpreter_dec.file(open(declaration_file))
except OSError as e:
    o_dec_file.close()
    os.remove(output_declaration_file)
    raise


try:
    interpreter_def.file(open(definition_file))
except OSError as e:
    o_def_file.close()
    os.remove(output_definition_file)
    raise

interpreter_dec.shutdown()
interpreter_def.shutdown()
o_dec_file.close()
o_def_file.close()
