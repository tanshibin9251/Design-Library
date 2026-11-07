(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  function toast(m){var t=$('#toast');t.textContent=m;t.classList.add('on');clearTimeout(toast._t);toast._t=setTimeout(function(){t.classList.remove('on')},1600)}
  function copy(txt,msg){
    var done=function(){toast(msg||'已复制')};
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(txt).then(done,fb)}else fb();
    function fb(){var a=document.createElement('textarea');a.value=txt;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy');done()}catch(e){toast('复制失败，请手动选取')}a.remove()}}
  window.dlCopy=copy;

  /* 代码块复制 */
  $$('.codeblock').forEach(function(b){var btn=$('.cp',b);if(btn)btn.addEventListener('click',function(){copy($('pre',b).textContent,'代码已复制')})});

  /* 筛选 chips（data-filter-group） */
  $$('[data-chips]').forEach(function(box){
    var target=$(box.getAttribute('data-chips'));
    $$('.chip',box).forEach(function(ch){ch.addEventListener('click',function(){
      $$('.chip',box).forEach(function(c){c.classList.remove('on')});ch.classList.add('on');
      var v=ch.getAttribute('data-v');
      $$('[data-g]',target).forEach(function(it){var g=it.getAttribute('data-g').split(' ');it.style.display=(v==='all'||g.indexOf(v)>-1)?'':'none'});
      $$('[data-sec]',target).forEach(function(s){var any=$$('[data-g]',s).some(function(i){return i.style.display!=='none'});s.style.display=any?'':'none'})})})});

  /* 搜索 */
  var data=null,ov=$('#sov'),inp=$('#sq'),res=$('#sres'),act=-1;
  function load(cb){if(data)return cb();fetch('/assets/search.json').then(function(r){return r.json()}).then(function(j){data=j;cb()}).catch(function(){data=[];cb()})}
  var KN={style:'风格',kit:'整站',part:'零件',effect:'效果',guide:'指南'};
  function render(q){
    q=q.trim().toLowerCase();var out=[];
    (data||[]).forEach(function(d){var h=(d.t+' '+d.d+' '+d.k+' '+(d.g||'')).toLowerCase();if(!q||q.split(/\s+/).every(function(w){return h.indexOf(w)>-1}))out.push(d)});
    res.innerHTML=out.length?out.slice(0,40).map(function(d){return '<a href="'+d.u+'"><span class="k">'+(KN[d.k]||d.k)+'</span>'+d.t+'<small>'+(d.d||'')+'</small></a>'}).join(''):'<p>没有结果</p>';act=-1}
  function open(){ov.classList.add('on');load(function(){render(inp.value)});setTimeout(function(){inp.focus()},30)}
  function close(){ov.classList.remove('on')}
  $$('[data-search]').forEach(function(b){b.addEventListener('click',open)});
  ov.addEventListener('click',function(e){if(e.target===ov)close()});
  inp.addEventListener('input',function(){render(inp.value)});
  document.addEventListener('keydown',function(e){
    var typing=/INPUT|TEXTAREA|SELECT/.test((document.activeElement||{}).tagName);
    if((e.key==='/'&&!typing)||((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')){e.preventDefault();open()}
    else if(e.key==='Escape')close();
    else if(ov.classList.contains('on')&&(e.key==='ArrowDown'||e.key==='ArrowUp'||e.key==='Enter')){
      var l=$$('a',res);if(!l.length)return;
      if(e.key==='Enter'){if(act>-1)location.href=l[act].href;else location.href=l[0].href;return}
      e.preventDefault();act=(act+(e.key==='ArrowDown'?1:-1)+l.length)%l.length;l.forEach(function(a,i){a.classList.toggle('act',i===act)});l[act].scrollIntoView({block:'nearest'})}});

  /* 风格母版：实时定制面板 */
  var S=window.STYLE;if(!S)return;
  var frame=$('#demo'),KEYS=['primary','secondary','text','accent','surface','border'];
  var LAB={primary:'Primary 主色',secondary:'Secondary 副色',text:'Text 正文',accent:'Accent 强调',surface:'Surface 底色',border:'Border 分隔线'};
  var FONTS={'无衬线':['Inter','Poppins','Montserrat','Work Sans','Source Sans 3','Lato','Mulish','Nunito','DM Sans','Manrope','Archivo','Open Sans','Roboto','Plus Jakarta Sans','Outfit','Raleway','Noto Sans SC'],
    '衬线':['Playfair Display','Fraunces','Cormorant Garamond','EB Garamond','Libre Baskerville','Source Serif 4','Crimson Pro','Lora','Merriweather','DM Serif Display','Noto Serif SC'],
    '展示':['Anton','Bebas Neue','Oswald','Abril Fatface','Space Grotesk','Syne']};
  var PRESETS=[['Ocean','#0b3b5c','#1d5f8a','#1b2733','#0ea5e9','#f5f9fc','#d9e6f0'],['Forest','#14532d','#3f6212','#1c2a21','#65a30d','#f6faf3','#dbe7d3'],['Sunset','#7c2d12','#9a3412','#2b1c14','#f97316','#fff7ed','#fbd9bd'],['Berry','#581c87','#86198f','#2a1633','#db2777','#fdf4ff','#ead1f2'],['Mono','#111111','#3f3f46','#18181b','#111111','#fafafa','#e4e4e7'],['Gold','#1c1917','#44403c','#292524','#b8860b','#faf7f0','#e7dfcb'],['Sky','#1e40af','#3730a3','#1e293b','#2563eb','#f8fafc','#dbe4f3'],['Rose','#881337','#9f1239','#3b1220','#e11d48','#fff1f2','#fbd5dc']];
  var TK=S.tok||{};function px(v,d){var m=/([\d.]+)px/.exec(v||'');return m?parseFloat(m[1]):d}
  var st={};function reset(){KEYS.forEach(function(k){st[k]=S.colors[k]});st.head=S.fonts.head;st.body=S.fonts.body;st.scale=100;st.radius=px(TK.radius,8);st.pad=100}reset();
  function sizes(){var k=st.scale/100;return {h1:Math.round(px(TK.h1,56)*k)+'px',h2:Math.round(px(TK.h2,40)*k)+'px',h3:Math.round(px(TK.h3,22)*k)+'px',h1big:Math.round(px(TK.h1big||TK.h1,56)*k)+'px',body:Math.round(px(TK.fsb,16)*k)+'px',radius:st.radius+'px',pad:Math.round(px(TK.pad,88)*st.pad/100)+'px'}}

  var cp=$('#colors');
  KEYS.forEach(function(k){var r=document.createElement('div');r.className='crow';
    r.innerHTML='<input type="color" data-k="'+k+'"><span>'+LAB[k]+'</span><input type="text" data-t="'+k+'" maxlength="7" spellcheck="false">';cp.appendChild(r)});
  function fontSel(id,key){var s=$(id),opts='<optgroup label="本模板默认">'+[S.fonts[key]].map(function(f){return '<option>'+f+'</option>'}).join('')+'</optgroup>';
    for(var g in FONTS)opts+='<optgroup label="'+g+'">'+FONTS[g].map(function(f){return '<option>'+f+'</option>'}).join('')+'</optgroup>';s.innerHTML=opts;
    s.addEventListener('change',function(){st[key]=s.value;push()});return s}
  var sh=fontSel('#fhead','head'),sb=fontSel('#fbody','body');
  var pr=$('#presets');PRESETS.forEach(function(p){var b=document.createElement('button');b.className='pre';b.title=p[0];b.type='button';
    b.innerHTML=p.slice(1).map(function(c){return '<i style="background:'+c+'"></i>'}).join('');
    b.addEventListener('click',function(){KEYS.forEach(function(k,i){st[k]=p[i+1]});sync();push()});pr.appendChild(b)});

  function lum(h){h=h.replace('#','');var n=parseInt(h,16);var a=[n>>16&255,n>>8&255,n&255].map(function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
  function ratio(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
  function sync(){KEYS.forEach(function(k){$('[data-k='+k+']').value=st[k];$('[data-t='+k+']').value=st[k]});sh.value=st.head;sb.value=st.body;$('#scale').value=st.scale;$('#radius').value=st.radius;$('#pad').value=st.pad;$('#v-scale').textContent=st.scale+'%';$('#v-radius').textContent=st.radius+'px';$('#v-pad').textContent=st.pad+'%';
    var r1=ratio(st.text,st.surface),r2=ratio(st.primary,st.surface);
    function f(r){return '<b class="'+(r>=4.5?'good':'bad')+'">'+r.toFixed(1)+':1'+(r>=4.5?' ✓':' ✗')+'</b>'}
    $('#ratio').innerHTML='对比度 · 正文/底色 '+f(r1)+' · 主色/底色 '+f(r2)}
  function push(){
    var v={};KEYS.forEach(function(k){v['--c-'+k]=st[k]});var z=sizes();v['--h1']=z.h1;v['--h2']=z.h2;v['--h3']=z.h3;v['--h1big']=z.h1big;v['--fs-body']=z.body;v['--radius']=z.radius;v['--pad']=z.pad;
    if(frame.contentWindow)frame.contentWindow.postMessage({type:'dl-set',vars:v,head:st.head,body:st.body},'*');
    sync()}
  cp.addEventListener('input',function(e){var k=e.target.getAttribute('data-k'),t=e.target.getAttribute('data-t');
    if(k){st[k]=e.target.value;push()}
    else if(t&&/^#[0-9a-fA-F]{6}$/.test(e.target.value)){st[t]=e.target.value;push()}});
  window.addEventListener('message',function(e){if(e.data&&e.data.type==='dl-ready')push()});
  [['scale','scale'],['radius','radius'],['pad','pad']].forEach(function(a){$('#'+a[0]).addEventListener('input',function(e){st[a[1]]=parseFloat(e.target.value);push()})});
  $('#reset').addEventListener('click',function(){reset();push();toast('已恢复默认')});
  $$('.dev').forEach(function(b){b.addEventListener('click',function(){$$('.dev').forEach(function(x){x.classList.remove('on')});b.classList.add('on');frame.style.width=b.getAttribute('data-w')})});

  /* 导出 */
  function elementor(){
    var l=['# Elementor › Site Settings › Global Colors','Primary    '+st.primary,'Secondary  '+st.secondary,'Text       '+st.text,'Accent     '+st.accent,'+ Custom: Surface '+st.surface,'+ Custom: Border  '+st.border,'','# Elementor › Site Settings › Global Fonts'];
    S.fontspec.forEach(function(f){var fam=f.role.indexOf('Heading')>-1?st.head:(f.role==='Body'?st.body:(f.family===S.fonts.head?st.head:st.body));
      l.push(f.role.padEnd(20)+fam+' · '+f.weight+' · '+f.size)});l.push('','# 示例页实际用的形状与字号（上面 Global Fonts 的字号是母版原始 brand kit 值，偏保守）：圆角 '+sizes().radius+'　标题 H1 '+sizes().h1+' / H2 '+sizes().h2+' / H3 '+sizes().h3+'　正文 '+sizes().body);return l.join('\n')}
  function css(){var z=sizes(),g='https://fonts.googleapis.com/css?family='+[st.head,st.body,'Noto Sans SC'].filter(function(v,i,a){return a.indexOf(v)===i}).map(function(f){return f.replace(/ /g,'+')+':400,500,600,700'}).join('|')+'&display=swap';
    return '/* Google Fonts: '+g+' */\n:root{\n'+KEYS.map(function(k){return '  --'+k+': '+st[k]+';'}).join('\n')+"\n  --font-heading: '"+st.head+"', 'Noto Sans SC', sans-serif;\n  --font-body: '"+st.body+"', 'Noto Sans SC', sans-serif;\n  --fs-h1: "+z.h1+";\n  --fs-h2: "+z.h2+";\n  --fs-h3: "+z.h3+";\n  --fs-body: "+z.body+";\n  --radius: "+z.radius+";\n  --section-pad: "+z.pad+";\n}"}
  function json(){var c={};KEYS.forEach(function(k){c[k]=st[k]});return JSON.stringify({template:S.slug,colors:c,fonts:{heading:st.head,body:st.body},sizes:(function(){var z=sizes();return {h1:z.h1,h2:z.h2,h3:z.h3,body:z.body}})(),radius:sizes().radius,section_pad:sizes().pad,googleFonts:[st.head,st.body].filter(function(v,i,a){return a.indexOf(v)===i})},null,2)}
  $('#cp-el').addEventListener('click',function(){copy(elementor(),'已复制 Elementor 全局色/字体')});
  $('#cp-css').addEventListener('click',function(){copy(css(),'已复制 CSS 变量')});
  $('#cp-json').addEventListener('click',function(){copy(json(),'已复制 JSON')});
  frame.addEventListener('load',push);sync();
})();
