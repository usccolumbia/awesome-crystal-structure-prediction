#!/usr/bin/env python3
"""Validate local integrity; does not claim external link availability or algorithm execution."""
import json,re
from pathlib import Path
from urllib.parse import urlsplit,unquote
R=Path(__file__).resolve().parents[1]
def load(n):return json.loads((R/'data'/f'{n}.json').read_text())
papers,software,benchmarks,formula=[load(n) for n in ['papers','software','benchmarks','formula_conditioning']]
keys=re.findall(r'@\w+\{([^,]+),',(R/'references.bib').read_text());assert len(keys)==len(set(keys)),'Duplicate BibTeX keys'
for records in [papers,software,benchmarks]:assert len(records)==len({x['id'] for x in records}),'Duplicate IDs'
pids={p['id'] for p in papers}
assert pids<=set(keys),'Paper missing from BibTeX'
for s in software:
 assert s['paper_ids'] and set(s['paper_ids'])<=pids,(s['id'],'paper linkage')
 if s['code_license_status']=='Open-source license verified':assert s.get('code_license') and s.get('license_url'),s['id']
 if s['pretrained_status']=='Public pretrained download':assert s.get('checkpoint_links'),s['id']
for a in formula:assert a['paper_id'] in pids and a['evidence'],a['paper_id']
for b in benchmarks:assert set(b['paper_ids'])<=pids and b['url'].startswith('https://'),b['id']
assert {b['id'] for b in benchmarks}>={'mp-20','mpts-52','cspbench','t180','t46','cspmetrics'}
# Every local Markdown link resolves to a file and, where specified, a real anchor.
for p in R.rglob('*.md'):
 for target in re.findall(r'\]\(([^\s)]+)\)',p.read_text()):
  if urlsplit(target).scheme or target.startswith('#'):continue
  name,_,frag=target.partition('#');dest=(p.parent/unquote(name)).resolve()
  assert dest.exists(),(p.name,target)
  if frag and dest.suffix=='.md':
   s=dest.read_text();heads=re.findall(r'^#+ (.+)$',s,re.M)
   anchors={re.sub(r'[^a-z0-9-]','',h.lower().replace(' ','-')) for h in heads}|set(re.findall(r'<a id="([^"]+)"',s))
   assert frag in anchors,(p.name,target,'missing anchor')
for p in [*R.glob('data/*.json'),R/'references.bib']:
 s=p.read_text();assert not re.search(r'/Users/|/scratch/|gh[pousr]_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16}',s),(p,'private path or credential pattern')
html=(R/'docs/index.html').read_text();embedded=json.loads(re.search(r'<script id="catalogue" type="application/json">(.*?)</script>',html,re.S)[1])
assert len(embedded['papers'])==len(papers) and len(embedded['software'])==len(software)
print(f'PASS: {len(papers)} papers, {len(software)} software records, {len(benchmarks)} named benchmarks, {len(keys)} unique bibliography keys; internal links and embedded data consistent.')
