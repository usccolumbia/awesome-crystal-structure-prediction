#!/usr/bin/env python3
"""Build the public catalogue from version-controlled JSON; Python standard library only."""
import csv, html, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(name): return json.loads((ROOT/'data'/f'{name}.json').read_text())
def write(path,text): (ROOT/path).write_text(text.rstrip()+'\n')
def esc(s): return str(s or '').replace('|','\\|').replace('\n',' ')
def link(label,url): return f'[{esc(label)}]({url})' if url else esc(label)
def anchor(s): return re.sub(r'[^a-z0-9-]','',str(s).lower().replace(' ','-'))
papers=load('papers'); software=load('software'); categories=load('categories'); benchmarks=load('benchmarks'); formula=load('formula_conditioning')
P={p['id']:p for p in papers}; C={c['id']:c['name'] for c in categories}
S={p['id']:[s for s in software if p['id'] in s['paper_ids']] for p in papers}
def paperlinks(ids): return ' · '.join(link(str(P[i]['year'])+' '+i,P[i]['url']) for i in ids)
def sources(urls): return ' · '.join(link('source '+str(i+1),u) for i,u in enumerate(dict.fromkeys(urls)))
head=f'''<p align="center"><img src="assets/banner.svg" alt="Awesome Crystal Structure Prediction" width="100%"></p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

# Awesome Crystal Structure Prediction (CSP)

A curated directory of **algorithms, papers, source code, pretrained models, datasets, and evaluation benchmarks** for predicting periodic crystal structures. Covers inorganic and molecular crystals, classical search, learned generation, and the components that connect them.

Companion resources for *Crystal Structure Prediction from Search to Learning: A 30-Year Expedition* (survey in preparation). Related collection: [Awesome Crystal Prototype](https://github.com/usccolumbia/awesome-crystal-prototype).

**{len(papers)} literature/software-paper records · {len(software)} implementation and component entries · {len(formula)} formula-conditioning audits.** Literature window: 1996–16 October 2026. Resource checks: 16–17 October 2026. This is a curated collection, not an exhaustive census or a performance ranking. The 1996 start is a survey boundary; the founding USPEX journal papers appeared in 2006.

## Contents

- [Browse and download](#browse-and-download)
- [Algorithm categories](#algorithm-categories)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [How to interpret availability](#how-to-interpret-availability)
- [Contributing](CONTRIBUTING.md) · [Provenance](docs/provenance.md) · [BibTeX](references.bib)

## Browse and download

| Resource | What it contains |
|---|---|
| [All papers](docs/papers.md) | Category, year, publication status, method, input information, group attribution, and primary sources |
| [Software profiles](docs/software.md) | Paper/code links, license evidence, checkpoints, training data, evaluations, and limitations |
| [Benchmarks](docs/benchmarks.md) | MP-20, MPTS-52, CSPBench, T180, T46, CSPMetrics; dataset and protocol distinctions |
| [Dataset index](docs/datasets.md) | Training, reference, and evaluation resources linked to each implementation |
| [Formula-conditioning audit](docs/formula-conditioning.md) | Exact cell counts, adaptation requirements, and unconditional generation |
| [Research groups](docs/groups.md) | Paper attribution with verification sources; collaborations are retained |
| [Interactive explorer](docs/index.html) | Download/clone and open this self-contained HTML file in a browser; search and filter locally |
| [Machine-readable data](data/) | JSON and CSV catalogues; [BibTeX](references.bib) for citations |

To browse locally:

```bash
git clone https://github.com/usccolumbia/awesome-crystal-structure-prediction.git
cd awesome-crystal-structure-prediction
python3 -m http.server 8000
# Open http://localhost:8000/docs/
```

## Algorithm categories

Categories describe candidate construction or search. Learned energy evaluators, symmetry predictors, and metric packages are listed as supporting components. Hybrids retain secondary categories in the data. Each table links to detailed release evidence.
'''
readme=[head]
for cat in [1,2,3,4,5,6,7,0]:
 readme += [f'### {C[cat]}','', '| Algorithm / component | Papers | Code or access | Details |','|---|---|---|---|']
 for s in sorted((s for s in software if s['primary_category']==cat),key=lambda s:s['name'].lower()):
  access=link('Source',s.get('code_url')) if s.get('code_url') else link('Access portal',s.get('project_url')) if s.get('project_url') else 'Not verified'
  readme += [f"| **{esc(s['name'])}** | {paperlinks(s['paper_ids'])} | {access} | [Profile](docs/software.md#{s['id']}) |"]
 readme += ['']
readme += ['## Benchmarks and evaluation','','| Resource | Role | Paper and release |','|---|---|---|']
for b in benchmarks: readme += [f"| **{b['name']}** | {b['kind']} | {paperlinks(b['paper_ids'])} · {link('Release / code',b['url'])} |"]
readme += ['','**MPTS-52** is the correct spelling (sometimes transposed as MPST-52); 52 is an atom-count limit. **T180** and **T46** are versioned test cohorts. **CSPMetrics/CSPBenchMetrics** is a metric toolkit. Historical CSPBench targets and later T180 releases must be compared by their manifests, not by the shared number 180. See [protocol notes](docs/benchmarks.md).','', '## How to interpret availability','','- A public repository is not automatically open-source licensed; license evidence is a separate field.','- A checkpoint for a relaxation evaluator is different from a generator checkpoint. Classical algorithms can have no pretrained model by design.','- Formula prompting, reduced-formula matching, and exact per-element cell-count preservation are different capabilities.','- Paper-reported results, source inspection, and successful runtime reproduction are different evidence levels. This collection does not claim independent execution of the algorithms.','- Each entry retains dated sources. Upstream links and releases may change.','','## Citation and license','','Cite the original papers for the methods and datasets you use. This directory provides [BibTeX](references.bib) and a [repository citation](CITATION.cff); the companion survey is in preparation and has no assigned DOI here.','','Repository-authored curation and tooling are under [MIT](LICENSE), matching the related prototype collection. Linked papers, software, models, and datasets retain their own licenses.']
write('README.md','\n'.join(readme))
lines=['# Paper catalogue','',f'{len(papers)} records, grouped by primary category. All source records are in [papers.json](../data/papers.json); citations are in [references.bib](../references.bib).','']
for cat in [1,2,3,4,5,6,7,0]:
 lines += [f'## {C[cat]}','']
 for p in sorted((p for p in papers if p['primary_category']==cat),key=lambda p:(p['year'],p['title'])):
  lines += [f"<a id=\"{p['id'].lower()}\"></a>",f"### {p['year']} — {p['title']}",'',f"**{p['id']} · {p.get('publication_status','')} · {p['domain']}**",'',f"{'; '.join(p['authors'])}. *{p.get('venue','')}*. {link('Paper',p['url'])}",'',f"**Method:** {p['method']}. {p.get('workflow','')}",'',f"**Inputs:** {p.get('inputs','See paper')}"]
  if S[p['id']]:lines += ['', '**Software:** '+' · '.join(link(s['name'],'software.md#'+s['id']) for s in S[p['id']])]
  if p.get('research_groups'):lines += ['', '**Groups:** '+' · '.join(link(g['label'],g.get('source_url','')) for g in p['research_groups'])]
  lines += ['',f"**Evidence:** {p.get('evidence_read','See primary sources')}. {sources(p.get('source_urls',[]))}"]
  if p.get('limitations'):lines += ['', '**Scope:** '+p['limitations']]
  lines += ['']
write('docs/papers.md','\n'.join(lines))
lines=['# Software, model and data profiles','','Availability is recorded separately from license status and runtime validation. A missing release is marked unknown rather than inferred absent.','']
for s in sorted(software,key=lambda x:x['name'].lower()):
 lines += [f'<a id="{s["id"]}"></a>',f'## {s["name"]}','',f"**{C[s['primary_category']]} · {s['domain']} · {s['role']}**",'',paperlinks(s['paper_ids']),'',f"**Source / access:** {link('Code',s.get('code_url')) if s.get('code_url') else link('Project',s.get('project_url')) if s.get('project_url') else 'No source or access link verified'} — {s.get('access_status','Unknown')}",'',f"**License:** {s.get('code_license_status','Unknown')} {link(s.get('code_license',''),s.get('license_url',''))}",'',f"**Pretrained model:** {s.get('pretrained_status','Unknown')}"]
 for x in s.get('checkpoint_links',[]):lines += [f"- {link(x.get('label','Checkpoint'),x['url'])} — {x.get('role','')} / {x.get('access','')}"]
 for field,title in [('training_datasets','Training data'),('reference_datasets','Reference data'),('evaluation_benchmarks','Evaluation')]:
  lines += ['',f'**{title}:**']
  for d in s.get(field,[]):
   lines += ['- '+link(d.get('name',d.get('id','Resource')),d.get('url',''))+' — '+d.get('role',d.get('task',d.get('kind','')))+'. '+d.get('version_split',d.get('protocol',''))]
  if not s.get(field):lines += [s.get('training_status','Not independently verified') if field=='training_datasets' else 'No separate item verified.']
 lines += ['',s.get('notes',''),'',s.get('dataset_notes',''),'',f"**Checked:** {s.get('checked_on','Unknown')}. **Evidence:** {sources(s.get('evidence_urls',[])+s.get('availability_evidence_urls',[])+s.get('dataset_evidence_urls',[]))}",'']
write('docs/software.md','\n'.join(lines))
lines=['# Benchmarks and evaluation','','Named benchmark datasets, test cohorts, benchmark studies, and metric toolkits solve different evaluation problems.','']
for b in benchmarks:
 lines += [f"## {b['name']}",'',f"**Type:** {b['kind']}",'',paperlinks(b['paper_ids']),'',link('Versioned release / code',b['url']),'',b['protocol']]
 for k in ['original_data_url','framework_url']:
  if b.get(k):lines+=['',link(k.replace('_',' ').title(),b[k])]
 lines+=['']
lines+=['## Comparison checklist','','Record the exact split or cohort manifest, supplied cell counts/symmetry, number of candidates, matcher and tolerances, relaxation and ranking model, compute budget, failed targets, and training exposure. Keep structure recovery, space-group agreement, energy ranking, and physical stability as separate measurements.','','Other benchmark and dataset links, including molecular blind tests, are retained in the [dataset index](datasets.md) and individual [software profiles](software.md).']
write('docs/benchmarks.md','\n'.join(lines))
lines=['# Training datasets and evaluation resources','','Entries retain each implementation’s role and protocol rather than merging datasets that share a name.','', '| Implementation | Role | Resource | Protocol / version |','|---|---|---|---|']
for s in software:
 for field,label in [('training_datasets','Training'),('reference_datasets','Reference'),('evaluation_benchmarks','Evaluation')]:
  for d in s.get(field,[]):lines += [f"| {link(s['name'],'software.md#'+s['id'])} | {label}: {esc(d.get('role',d.get('kind','')))} | {link(d.get('name','Resource'),d.get('url',''))} | {esc(d.get('version_split',d.get('protocol','')))} |"]
write('docs/datasets.md','\n'.join(lines))
lines=['# Exact formula conditioning','','An interface audit of 42 generative or hybrid workflows. These are source-qualified capabilities, not runtime tests. Exact cell counts are stronger than reduced-formula ratios or soft prompts.','']
for a in formula:
 lines += [f"## {a['model_name']}",'',link(a['title'],a['paper_url']),'',f"**{a['label']}** — {a.get('support_scope','')}",'',a.get('mechanism',''),'',f"**Conditions:** {', '.join(a.get('documented_conditions',[]))}",'',f"**Adaptation:** {a.get('adaptation_required','See evidence')}",'',a.get('caveat',''),'']
 for e in a.get('evidence',[]):lines += ['- '+link(e.get('source_type','Source'),e['url'])+': '+e.get('locator','')+' — '+e.get('observation','')]
 lines += ['']
write('docs/formula-conditioning.md','\n'.join(lines))
groups={}
for p in papers:
 for g in p.get('research_groups',[]):groups.setdefault(g['label'],[]).append((p,g))
lines=['# Research groups and collaborations','','Labels attribute papers to named authors or documented collaborations. They are not claims of exclusive ownership of an algorithm.','']
for name,items in sorted(groups.items()):
 lines += ['## '+name,'']
 for p,g in items:lines += [f"- {link(p['title'],p['url'])} ({p['year']}) — {C[p['primary_category']]}. {link('Attribution source',g.get('source_url',''))}"]
 lines+=['']
write('docs/groups.md','\n'.join(lines))
for name,records,fields in [('papers',papers,['id','year','title','method','domain','primary_category','publication_status','doi','url']),('software',software,['id','name','primary_category','domain','code_url','project_url','code_license_status','pretrained_status','paper_ids']),('benchmarks',benchmarks,['id','name','kind','url','protocol','paper_ids'])]:
 with (ROOT/'data'/f'{name}.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for d in records:w.writerow({k:('; '.join(map(str,d[k])) if isinstance(d.get(k),list) else d.get(k,'')) for k in fields})
payload={'papers':papers,'software':software,'categories':categories,'benchmarks':benchmarks,'formula':formula}
template=(ROOT/'scripts/explorer.html').read_text();write('docs/index.html',template.replace('__DATA__',json.dumps(payload,ensure_ascii=False).replace('</','<\\/')))
print(f'Built {len(papers)} papers, {len(software)} implementations, {len(benchmarks)} named benchmark resources.')
