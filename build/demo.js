(function(){
  var root=document.documentElement;
  function lum(h){h=(h||'').replace('#','');if(h.length===3)h=h.split('').map(function(c){return c+c}).join('');
    var n=parseInt(h,16);if(isNaN(n))return 1;
    var a=[n>>16&255,n>>8&255,n&255].map(function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});
    return .2126*a[0]+.7152*a[1]+.0722*a[2]}
  function on(h){return lum(h)>.45?'#111111':'#ffffff'}
  function contrast(){
    var s=getComputedStyle(root);
    ['primary','secondary','accent','surface'].forEach(function(k){
      root.style.setProperty('--on-'+k,on(s.getPropertyValue('--c-'+k).trim()))})}
  var loaded={};
  function font(name){
    if(!name||loaded[name])return;loaded[name]=1;
    var l=document.createElement('link');l.rel='stylesheet';
    l.href='https://fonts.googleapis.com/css?family='+encodeURIComponent(name).replace(/%20/g,'+')+':300,400,500,600,700,800&display=swap';
    document.head.appendChild(l)}
  var CJK=",'Noto Sans SC','Noto Serif SC',sans-serif";
  window.addEventListener('message',function(e){
    var d=e.data;if(!d||d.type!=='dl-set')return;
    if(d.vars)for(var k in d.vars)root.style.setProperty(k,d.vars[k]);
    if(d.head){font(d.head);root.style.setProperty('--f-head',"'"+d.head+"'"+CJK)}
    if(d.body){font(d.body);root.style.setProperty('--f-body',"'"+d.body+"'"+CJK)}
    contrast()});
  document.addEventListener('click',function(e){var a=e.target.closest('a');if(a&&a.getAttribute('href')==='#')e.preventDefault()});
  contrast();
  if(parent!==window)parent.postMessage({type:'dl-ready'},'*');
})();
