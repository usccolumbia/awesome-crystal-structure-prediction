// Run the actual explorer script against a minimal DOM; not a rendering test.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..'),html=fs.readFileSync(path.join(root,'docs/index.html'),'utf8'),D=JSON.parse(html.match(/<script id="catalogue" type="application\/json">([\s\S]*?)<\/script>/)[1]);
class Element {constructor(){this.value='';this.children=[];this.textContent='';this.events={}}append(...xs){this.children.push(...xs)}replaceChildren(...xs){this.children=[...xs]}addEventListener(k,f){this.events[k]=f}}
const els={};for(const id of ['catalogue','q','kind','category','domain','group','license','weights','formula','prior','reset','count','results','more'])els[id]=new Element();els.catalogue.textContent=JSON.stringify(D);els.kind.value='software';
const ctx=vm.createContext({document:{getElementById:id=>{assert(els[id],id);return els[id]},createElement:()=>new Element()},console});
vm.runInContext([...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].at(-1)[1],ctx);const run=s=>vm.runInContext(s,ctx);
function reset(){els.reset.onclick()}
let cases=0;
for(const kind of ['papers','software']){
 els.kind.value=kind;reset();assert.equal(run('D[$("kind").value].filter(r=>matches(r,$("kind").value)).length'),D[kind].length);
 for(const f of D.priors.features){els.prior.value=f.id;const expected=D[kind].filter(r=>(r.structural_priors||[]).includes(f.id));assert.equal(run('D[$("kind").value].filter(r=>matches(r,$("kind").value)).length'),expected.length);cases++;
  els.license.value='open';const licensed=expected.filter(r=>kind==='software'?r.code_license_status==='Open-source license verified':D.software.some(s=>s.paper_ids.includes(r.id)&&s.code_license_status==='Open-source license verified'));assert.equal(run('D[$("kind").value].filter(r=>matches(r,$("kind").value)).length'),licensed.length);cases++;els.license.value='';
 }
 reset();assert.equal(els.prior.value,'');els.q.value='zzzz-no-such-entry';run('render()');assert.match(els.count.textContent,/^0 /);reset();
}
els.kind.value='software';els.q.value='MAGUS';run('render()');assert.match(els.count.textContent,/^1 /);els.license.value='open';run('render()');assert.match(els.count.textContent,/^0 /);reset();
for(const f of D.priors.profiles)for(const kind of ['software','papers'])for(const id of f[kind==='papers'?'paper_ids':'software_ids']){const r=D[kind].find(x=>x.id===id);assert(r,id);ctx.record=r;ctx.kind=kind;assert(run('card(record,kind)').children.length>0);cases++}
console.log(`PASS: explorer script, ${cases} profile/filter cases, reset and empty states; browser rendering not tested.`);
