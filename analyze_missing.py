import yaml

with open('locales/en.yaml') as f:
    en = yaml.safe_load(f)
with open('locales/ja.yaml') as f:
    ja = yaml.safe_load(f)
with open('locales/ko.yaml') as f:
    ko = yaml.safe_load(f)

def flatten(d, prefix=''):
    items = {}
    for k, v in d.items():
        key = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict):
            items.update(flatten(v, key))
        else:
            items[key] = v
    return items

en_flat = flatten(en)
ja_flat = flatten(ja)
ko_flat = flatten(ko)

print(f'Total EN keys: {len(en_flat)}')
print(f'Total JA keys: {len(ja_flat)}')
print(f'Total KO keys: {len(ko_flat)}')

def find_missing(en_f, locale_f, locale_name):
    missing = []
    same_as_en = []
    for k, v in en_f.items():
        if k not in locale_f:
            missing.append(k)
        elif locale_f[k] == v:
            same_as_en.append(k)
    print(f'\n{locale_name}:')
    print(f'  Missing keys: {len(missing)}')
    print(f'  Same as English (untranslated): {len(same_as_en)}')
    print(f'  Total to translate: {len(missing) + len(same_as_en)}')
    return missing, same_as_en

ja_missing, ja_same = find_missing(en_flat, ja_flat, 'JA')
ko_missing, ko_same = find_missing(en_flat, ko_flat, 'KO')

print('\n=== JA Missing Keys ===')
for k in ja_missing:
    print(f'  MISSING: {k}')

print('\n=== JA Same as EN (untranslated) ===')
for k in ja_same:
    print(f'  SAME: {k} = {repr(en_flat[k][:80])}')

print('\n=== KO Missing Keys ===')
for k in ko_missing:
    print(f'  MISSING: {k}')

print('\n=== KO Same as EN (untranslated) ===')
for k in ko_same:
    print(f'  SAME: {k} = {repr(en_flat[k][:80])}')
