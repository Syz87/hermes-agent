import yaml

def flatten(d, prefix=''):
    result = {}
    for k, v in d.items():
        key = f'{prefix}.{k}' if prefix else k
        if isinstance(v, dict):
            result.update(flatten(v, key))
        else:
            result[key] = v
    return result

with open('locales/en.yaml') as f:
    en = yaml.safe_load(f)
en_flat = flatten(en)
print(f'EN total keys: {len(en_flat)}')

for loc in ['pt', 'ru', 'tr']:
    with open(f'locales/{loc}.yaml') as f:
        locale = yaml.safe_load(f)
    locale_flat = flatten(locale)
    print(f'{loc} total keys: {len(locale_flat)}')
    
    same_as_en = 0
    missing = 0
    for k, v in en_flat.items():
        if k not in locale_flat:
            missing += 1
        elif locale_flat[k] == v:
            same_as_en += 1
    print(f'  Missing: {missing}, Same as EN: {same_as_en}, Need translation: {missing + same_as_en}')
    
    # Show sections with most gaps
    sections = {}
    for k, v in en_flat.items():
        if k not in locale_flat or locale_flat.get(k) == v:
            section = k.split('.')[0]
            sections[section] = sections.get(section, 0) + 1
    for s, c in sorted(sections.items(), key=lambda x: -x[1]):
        print(f'    {s}: {c}')
    print()
