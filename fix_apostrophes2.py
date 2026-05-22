#!/usr/bin/env python3
"""Fix missing apostrophes in FR YAML by direct text replacement."""
import yaml

# Read as raw text
with open('locales/fr.yaml', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements: (old, new) - these are French contractions
# that lost their apostrophes during yaml.dump
replacements = [
    # l'outil patterns
    ("de loutil", "de l'outil"),
    ("loutil `{tool}`", "l'outil `{tool}`"),
    ("dun appel doutil", "d'un appel d'outil"),
    ("doutil", "d'outil"),  # catch-all for d'outil
    
    # L'agent patterns
    ("Lagent semble", "L'agent semble"),
    ("Lagent est en cours", "L'agent est en cours"),
    ("Lagent a peut", "L'agent a peut"),
    ("Lagent est peut", "L'agent est peut"),
    
    # d'erreur patterns  
    ("derreur API", "d'erreur API"),
    
    # l'authentification
    ("lauthentification", "l'authentification"),
    
    # l'API
    ("lAPI après", "l'API après"),
    
    # des outils patterns
    ("les appels doutils", "les appels d'outils"),
    
    # l'expiration
    ("lexpiration", "l'expiration"),
    
    # d'accès
    ("daccès", "d'accès"),
    
    # l'entrée
    ("lentrée", "l'entrée"),
    
    # l'annulation
    ("lannulation", "l'annulation"),
    
    # l'ajout
    ("lajout", "l'ajout"),
    
    # l'envoi
    ("lenvoi", "l'envoi"),
    
    # l'exécution
    ("lexécution", "l'exécution"),
    
    # l'ouverture
    ("louverture", "l'ouverture"),
    
    # l'erreur
    ("lerreur", "l'erreur"),
    
    # l'image
    ("limage", "l'image"),
    
    # l'interface
    ("linterface", "l'interface"),
    
    # l'option
    ("loption", "l'option"),
    
    # l'activation
    ("lactivation", "l'activation"),
    
    # l'effacement
    ("leffacement", "l'effacement"),
    
    # l'entrée
    ("lentree", "l'entrée"),
]

for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('locales/fr.yaml', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('locales/fr.yaml', 'r', encoding='utf-8') as f:
    new_content = f.read()

print("Post-fix apostrophe counts:")
for pattern in ["l'outil", "L'agent", "d'erreur", "l'authentification", "d'outil", "l'API"]:
    count = new_content.count(pattern)
    print(f"  {pattern}: {count}")

# Also check for any remaining missing apostrophes in French-specific words
import re
# Find French words that commonly need apostrophes
french_words_needing_apostrophe = [
    (r"l[a-zéèêëàâäùûüôöîï]+", "l'"),  # l + vowel
    (r"d[a-zéèêëàâäùûüôöîï]+", "d'"),   # d + vowel  
]

# Count remaining issues
remaining_issues = []
for line_num, line in enumerate(new_content.split('\n'), 1):
    if 'loutil' in line or 'Lagent' in line or 'derreur' in line or 'lauthentification' in line:
        remaining_issues.append(f"Line {line_num}: {line[:80]}")

if remaining_issues:
    print("\n⚠️ Remaining issues:")
    for issue in remaining_issues:
        print(f"  {issue}")
else:
    print("\n✅ No remaining apostrophe issues found")
