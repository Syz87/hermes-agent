#!/usr/bin/env python3
"""Check and fix apostrophes in French YAML file."""
import yaml
import re

with open('locales/fr.yaml', 'r', encoding='utf-8') as f:
    content = f.read()

# Count occurrences
l_outil_no_apostrophe = content.count("loutil")
l_outil_with_apostrophe = content.count("l'outil")
l_agent_no_apostrophe = content.count("Lagent")
l_agent_with_apostrophe = content.count("L'agent")
l_error_no_apostrophe = content.count("derreur")
l_error_with_apostrophe = content.count("d'erreur")
l_auth_no_apostrophe = content.count("lauthentification")
l_auth_with_apostrophe = content.count("l'authentification")
l_do_no_apostrophe = content.count("do")
d_outils_no_apostrophe = content.count("doutil")
d_outils_with_apostrophe = content.count("d'outil")

print(f"loutil without apostrophe: {l_outil_no_apostrophe}")
print(f"l'outil with apostrophe: {l_outil_with_apostrophe}")
print(f"Lagent without apostrophe: {l_agent_no_apostrophe}")
print(f"L'agent with apostrophe: {l_agent_with_apostrophe}")
print(f"derreur without apostrophe: {l_error_no_apostrophe}")
print(f"d'erreur with apostrophe: {l_error_with_apostrophe}")
print(f"lauthentification without apostrophe: {l_auth_no_apostrophe}")
print(f"l'authentification with apostrophe: {l_auth_with_apostrophe}")
print(f"doutil without apostrophe: {d_outils_no_apostrophe}")
print(f"d'outil with apostrophe: {d_outils_with_apostrophe}")
