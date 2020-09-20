import os
import tempfile
import argparse
import json


parser = argparse.ArgumentParser(prog='tools')
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    with open(storage_path, 'w+') as f:
        json.dump({}, f)
        
with open(storage_path, 'r') as f:
    data = json.load(f)
        
if args.val:
    data.setdefault(args.key, [])
    data[args.key].append(args.val)
else:
    if args.key in data and len(data[args.key]) > 0:
        print(', '.join(data[args.key]))
    else:
        print(None)


with open(storage_path, 'w') as f:
    json.dump(data, f)
