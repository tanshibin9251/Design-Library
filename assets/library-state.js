/* Small, independently checked data helpers; no DOM or network access. */
(function(root){
 'use strict';
 const kinds=new Set(['template','effect','transition','graphic','asset']);
 const validItem=x=>typeof x==='string'&&x.length<=180&&/^[a-z]+:[a-z0-9-]+$/.test(x)&&kinds.has(x.split(':')[0]);
 const cleanItems=xs=>[...new Set(xs.filter(validItem))];
 function validate(value){
  if(!value||value.version!==1||!Array.isArray(value.projects)||!value.projects.length||value.projects.length>30)throw Error('Expected a Design Library backup with 1–30 projects.');
  const ids=new Set();
  const projects=value.projects.map(p=>{
   if(!p||typeof p.id!=='string'||!/^[a-zA-Z0-9_-]{1,90}$/.test(p.id)||ids.has(p.id)||typeof p.name!=='string'||!p.name.trim()||p.name.length>80||!Array.isArray(p.items)||p.items.length>1000||p.items.some(x=>!validItem(x))||typeof p.notes!=='string'||p.notes.length>4000)throw Error('Invalid project names, notes or item IDs.');
   ids.add(p.id);return{id:p.id,name:p.name.trim(),items:cleanItems(p.items),notes:p.notes};
  });
  if(!ids.has(value.active))throw Error('The active project is missing.');
  return{version:1,active:value.active,projects};
 }
 function migrate(raw,legacy){
  try{return validate(JSON.parse(raw))}catch(e){return{version:1,active:'default',projects:[{id:'default',name:'My first project',items:cleanItems(Array.isArray(legacy)?legacy:[]),notes:''}]}}
 }
 function merge(current,incoming,stamp){
  const base=validate(current),added=validate(incoming);
  const fingerprint=p=>JSON.stringify([p.name,p.notes,[...p.items].sort()]);
  const existing=new Set(base.projects.map(fingerprint));
  const fresh=added.projects.filter(p=>{const key=fingerprint(p);if(existing.has(key))return false;existing.add(key);return true});
  if(base.projects.length+fresh.length>30)throw Error('A maximum of 30 projects can be stored.');
  const ids=new Set(base.projects.map(p=>p.id));
  fresh.forEach((p,i)=>{let id='import-'+stamp+'-'+i;while(ids.has(id))id+='x';ids.add(id);base.projects.push({...p,id,items:[...p.items]})});
  return base;
 }
 const canCompare=(width,device)=>width>820&&device==='desktop';
 const api={validate,migrate,merge,canCompare};
 if(typeof module!=='undefined'&&module.exports)module.exports=api;
 else root.DLState=api;
})(typeof window==='undefined'?globalThis:window);
