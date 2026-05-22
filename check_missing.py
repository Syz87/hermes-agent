#!/usr/bin/env python3
"""Check missing keys in all locale files vs en.yaml"""
import yaml
import glob

def flatten(d, p=''):
    items = {}
    for k, v in d.items():
        key = f'{p}.{k}' if p else k
        if isinstance(v, dict):
            items.update(flatten(v, key))
        else:
            items[key] = v
    return items

with open('locales/en.yaml') as f:
    en = yaml.safe_load(f)
en_flat = flatten(en)

for f in sorted(glob.glob('locales/*.yaml')):
    if 'en.yaml' in f:
        continue
    with open(f) as fh:
        lang = yaml.safe_load(fh)
    lang_flat = flatten(lang)
    missing = set(en_flat.keys()) - set(lang_flat.keys())
    extra = set(lang_flat.keys()) - set(en_flat.keys())
    if missing or extra:
        print(f'=== {f}: missing={len(missing)} extra={len(extra)} ===')
        for m in sorted(missing):
            print(f'  MISSING: {m}')
    else:
        print(f'{f}: OK')
