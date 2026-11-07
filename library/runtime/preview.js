(function(){
  var root=document.documentElement,PTON=!!window.PTON;
  function lum(h){h=(h||'').replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');var n=parseInt(h,16);if(isNaN(n))return 1;var a=[n>>16&255,n>>8&255,n&255].map(function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*a[0]+.7152*a[1]+.0722*a[2]}
  function on(h){return lum(h)>.45?'#111111':'#ffffff'}
  function contrast(){var s=getComputedStyle(root);['primary','secondary','accent','surface'].forEach(function(k){root.style.setProperty('--on-'+k,on(s.getPropertyValue('--c-'+k).trim()))});document.body.classList.toggle('dk',lum(s.getPropertyValue('--c-surface').trim())<.25)}
  var loaded={};
  function font(n){if(!n||loaded[n])return;loaded[n]=1;var l=document.createElement('link');l.rel='stylesheet';l.href='https://fonts.googleapis.com/css?family='+encodeURIComponent(n).replace(/%20/g,'+')+':300,400,500,600,700,800&display=swap';document.head.appendChild(l)}
  var CJK=",'Noto Sans SC','Noto Serif SC',sans-serif";
  function swap(slug){
    var ms=[].slice.call(document.querySelectorAll('main[data-page]'));
    var m=ms.filter(function(x){return x.getAttribute('data-page')===slug})[0];
    if(!m){m=ms.filter(function(x){return x.getAttribute('data-page')==='404'})[0]||ms[0]}
    ms.forEach(function(x){x.classList.remove('on')});m.classList.add('on');
    [].forEach.call(document.querySelectorAll('details[open]'),function(d){d.open=false});
    window.scrollTo(0,0);return m.getAttribute('data-page')}
  var cur=null;
  function show(slug,silent,instant){
    var done=function(){cur=swap(slug);if(!silent&&parent!==window)parent.postMessage({type:'dl-page',page:cur},'*')};
    if(PTON&&!instant&&cur!==null&&document.startViewTransition){try{document.startViewTransition(done)}catch(e){done()}}else done()}
  addEventListener('message',function(e){var d=e.data;if(!d)return;
    if(d.type==='dl-goto'){show(d.page,true);return}
    if(d.type==='dl-pt-demo'){var o=cur==='home'?'about':'home',back=cur;show(o,true);setTimeout(function(){show(back,true)},(d.ms||600)+1500);return}
    if(d.type!=='dl-set')return;
    if(d.vars)for(var k in d.vars)root.style.setProperty(k,d.vars[k]);
    if(d.head){font(d.head);root.style.setProperty('--f-head',"'"+d.head+"'"+CJK)}
    if(d.body){font(d.body);root.style.setProperty('--f-body',"'"+d.body+"'"+CJK)}
    if(typeof d.ptcss==='string'){var el=document.getElementById('ptcss');if(el)el.textContent=d.ptcss;PTON=d.ptcss.length>0}
    contrast()});
  document.addEventListener('click',function(e){var a=e.target.closest('a');if(!a)return;var h=a.getAttribute('href')||'';
    if(h==='#'){e.preventDefault();return}
    if(h.indexOf('#/')===0){e.preventDefault();show(h.slice(2))}});
  show(window.START||'home',true,true);contrast();
  if(parent!==window)parent.postMessage({type:'dl-ready'},'*');
})();
