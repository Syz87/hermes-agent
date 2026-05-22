#!/usr/bin/env python3
"""Fix apostrophes in FR YAML and re-dump properly."""
import yaml

class ApostropheSafeDumper(yaml.SafeDumper):
    """YAML dumper that properly handles apostrophes in strings."""
    pass

def apostrophe_representer(dumper, data):
    """Represent strings with apostrophes using double quotes."""
    if isinstance(data, str) and "'" in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

ApostropheSafeDumper.add_representer(str, apostrophe_representer)

# Read the current FR file as raw text and fix apostrophes
with open('locales/fr.yaml', 'r', encoding='utf-8') as f:
    content = f.read()

# Read as YAML to get the structure
fr = yaml.safe_load(content)

# Write with the safe dumper that handles apostrophes
with open('locales/fr.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(fr, f, Dumper=ApostropheSafeDumper, default_flow_style=False, 
              allow_unicode=True, sort_keys=False, width=120)

# Verify
with open('locales/fr.yaml', 'r', encoding='utf-8') as f:
    new_content = f.read()

l_outil_no_apostrophe = new_content.count("loutil")
l_outil_with_apostrophe = new_content.count("l'outil")
l_agent_no_apostrophe = new_content.count("Lagent")
l_agent_with_apostrophe = new_content.count("L'agent")
d_outils_no_apostrophe = new_content.count("doutil")
d_outils_with_apostrophe = new_content.count("d'outil")

print(f"After fix:")
print(f"  loutil without apostrophe: {l_outil_no_apostrophe} (was 2)")
print(f"  l'outil with apostrophe: {l_outil_with_apostrophe} (was 0)")
print(f"  Lagent without apostrophe: {l_agent_no_apostrophe} (was 4)")
print(f"  L'agent with apostrophe: {l_agent_with_apostrophe} (was 7)")
print(f"  doutil without apostrophe: {d_outils_no_apostrophe} (was 9)")
print(f"  d'outil with apostrophe: {d_outils_with_apostrophe} (was 2)")

# Also check German
with open('locales/de.yaml', 'r', encoding='utf-8') as f:
    de_content = f.read()

de_l_outil = de_content.count("loutil")
de_l_outil_apost = de_content.count("l'outil")
print(f"\nGerman apostrophe check:")
print(f"  loutil without: {de_l_outil}")
print(f"  l'outil with: {de_l_outil_apost}")
