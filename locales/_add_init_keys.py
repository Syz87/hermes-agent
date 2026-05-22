#!/usr/bin/env python3
"""Add agent.init keys to all non-en, non-zh locale files for catalog parity."""

import glob
import os

os.chdir('/root/.hermes/hermes-agent/locales')

init_keys = {
    'initialized':           '🤖 AI Agent initialized with model: {model}',
    'initialized_bedrock_sdk': '🤖 AI Agent initialized with model: {model} (AWS Bedrock + AnthropicBedrock SDK, {region})',
    'initialized_anthropic': '🤖 AI Agent initialized with model: {model} (Anthropic native)',
    'initialized_bedrock':   '🤖 AI Agent initialized with model: {model} (AWS Bedrock, {region}{guardrails})',
    'using_entra':           '🔑 Using credentials: Microsoft Entra ID',
    'using_token':           '🔑 Using token: {token}',
    'custom_base_url':       '🔗 Using custom base URL: {url}',
    'using_api_key':         '🔑 Using API key: {key}',
    'tools_loaded':          '🛠️  Loaded {count} tools: {tools}',
    'enabled_toolsets':      '   ✅ Enabled toolsets: {toolsets}',
    'disabled_toolsets':     '   ❌ Disabled toolsets: {toolsets}',
    'no_tools':              '🛠️  No tools loaded (all tools filtered out or unavailable)',
    'ephemeral_prompt':      "🔒 Ephemeral system prompt: '{prompt}' (not saved to trajectories)",
    'prompt_caching':        '💾 Prompt caching: ENABLED ({source}, {ttl} TTL)',
    'context_limit':         '📊 Context limit: {tokens} tokens (compress at {threshold}% = {threshold_tokens})',
    'context_limit_disabled': '📊 Context limit: {tokens} tokens (auto-compression disabled)',
}

skip = {'en.yaml', 'zh.yaml'}

for f in sorted(glob.glob('*.yaml')):
    if f in skip:
        continue
    
    with open(f, 'r') as fh:
        content = fh.read()
    
    lines = content.split('\n')
    
    # Check if agent: section exists
    has_agent = '\nagent:\n' in content or content.startswith('agent:\n')
    
    if has_agent:
        # Find the line after all agent: keys (next top-level key)
        in_agent = False
        agent_end_idx = None
        for i, line in enumerate(lines):
            if line.rstrip() == 'agent:':
                in_agent = True
            elif in_agent and line and not line.startswith(' ') and not line.startswith('#') and line.strip():
                agent_end_idx = i
                break
        if agent_end_idx is None:
            agent_end_idx = len(lines)
        
        # Build init block (properly indented under agent:)
        init_lines = ['  init:']
        for k, v in init_keys.items():
            init_lines.append(f'    {k}: "{v}"')
        init_lines.append('')
        
        for j, il in enumerate(init_lines):
            lines.insert(agent_end_idx + j, il)
    else:
        # No agent: section - find insertion point (before gateway: or at end)
        insert_idx = None
        for i, line in enumerate(lines):
            if line.startswith('gateway:'):
                insert_idx = i
                break
        if insert_idx is None:
            insert_idx = len(lines)
        
        # Build full agent: section
        section_lines = ['', '# Agent init-time banner messages', 'agent:', '  init:']
        for k, v in init_keys.items():
            section_lines.append(f'    {k}: "{v}"')
        section_lines.append('')
        
        for j, sl in enumerate(section_lines):
            lines.insert(insert_idx + j, sl)
    
    with open(f, 'w') as fh:
        fh.write('\n'.join(lines))
    
    print(f'Updated {f}')
