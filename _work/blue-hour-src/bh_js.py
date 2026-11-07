JS = r"""
(function(){
'use strict';
var D=document,W=window,RM=!!(W.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches),COARSE=!!(W.matchMedia&&matchMedia('(pointer:coarse)').matches);
function $(s,r){return(r||D).querySelector(s)}function $$(s,r){return[].slice.call((r||D).querySelectorAll(s))}
function cl(v,a,b){if(a===undefined){a=0;b=1}return v<a?a:v>b?b:v}
function ez3(t){return 1-Math.pow(1-t,3)}function eio(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}function eq(t){return t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2}
var UN=0;function uid(s){UN++;return s.replace(/id="(ap-[a-z0-9]+)"/g,'id="$1x'+UN+'"').replace(/url\(#(ap-[a-z0-9]+)\)/g,'url(#$1x'+UN+')').replace(/href="#(ap-[a-z0-9]+)"/g,'href="#$1x'+UN+'"')}
function active(){return $('main[data-page].on')||$('main')||D.body}
var ups=[],raf=0,vel={y:W.scrollY||0,v:0};
function frame(){raf=0;var y=W.scrollY||0;vel.v+=((y-vel.y)*.9-vel.v)*.35;vel.y=y;if(Math.abs(vel.v)<.05)vel.v=0;var vh=W.innerHeight||800,busy=vel.v!==0;
 head(y,vh);ups.forEach(function(u){if(u(vh)===true)busy=true});if(busy)req()}
function req(){if(!raf)raf=requestAnimationFrame(frame)}

/* ── header, menu, nav state ── */
function head(y,vh){var t=$('.bh-top');if(!t)return;t.classList.toggle('is-s',y>24);var m=Math.max(1,D.documentElement.scrollHeight-vh);t.style.setProperty('--bp',cl(y/m).toFixed(3))}
function navSync(root){var s=$('[data-nav]',root),k=s&&s.getAttribute('data-nav');$$('.bh-nav a').forEach(function(a){var on=a.getAttribute('data-k')===k;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')})}
function menu(){var b=$('.bh-burger'),n=$('.bh-nav');if(!b||b.__m)return;b.__m=1;
 function set(o){b.setAttribute('aria-expanded',o);n.classList.toggle('open',o)}
 b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
 n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
 D.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)})}

/* ── 1 split lines ── */
function mSl(root){if(RM)return null;var els=$$('[data-sl]',root),lines=[];
 els.forEach(function(e){if(e.__t===undefined)e.__t=e.textContent.replace(/\s+/g,' ').trim();e.textContent='';
  var sr=D.createElement('span');sr.className='sl-sr';sr.textContent=e.__t;e.appendChild(sr);
  var box=D.createElement('span');box.setAttribute('aria-hidden','true');e.appendChild(box);
  var ws=e.__t.split(' '),sp=ws.map(function(w,i){var s=D.createElement('span');s.textContent=w+(i<ws.length-1?' ':'');box.appendChild(s);return s});
  var rows=[],top=null;sp.forEach(function(s){var t=s.offsetTop;if(top===null||Math.abs(t-top)>3){rows.push([]);top=t}rows[rows.length-1].push(s.textContent)});
  box.textContent='';
  rows.forEach(function(r){var m=D.createElement('span');m.className='sl-l';var i=D.createElement('span');i.className='sl-i';i.textContent=r.join('').replace(/\s+$/,'');m.appendChild(i);box.appendChild(m);lines.push(i)})});
 return function(vh){lines.forEach(function(i){var r=i.parentNode.getBoundingClientRect();i.style.setProperty('--l',ez3(cl((vh*.94-r.top)/(vh*.16))).toFixed(3))})}}

/* ── 2 scene stack ── */
function mSs(root){var sec=$('[data-ss]',root);if(!sec||RM)return null;
 var sc=$$('.ss-s',sec),N=sc.length,rail=$('.ss-rail',sec),bar=$('.ss-bar',sec);sec.parentNode.classList.add('ss-on');
 if(!sec.__ss){sec.__ss=1;sc.forEach(function(s,i){var b=D.createElement('button');b.type='button';b.textContent='0'+(i+1);b.setAttribute('aria-label','Scene '+(i+1)+': '+$('h3',s).textContent);
  b.onclick=function(){var r=sec.getBoundingClientRect(),tot=r.height-W.innerHeight;W.scrollTo({top:W.scrollY+r.top+(i+.5)/N*tot,behavior:'smooth'})};rail.appendChild(b)})}
 var btns=$$('button',rail);
 return function(vh){var r=sec.getBoundingClientRect(),tot=Math.max(1,r.height-vh),p=cl(-r.top/tot),q=p*N,act=Math.min(N-1,Math.floor(q));
  sc.forEach(function(s,i){var e=i?cl((q-i+.6)/.6):1,tin=i?cl((q-i)/.25):1,tout=i<N-1?cl((i+1-q)/.25):1,v=Math.min(tin,tout),t=$('.ss-t',s);
   $('.ss-art',s).style.setProperty('--e',e.toFixed(3));t.style.setProperty('--v',v.toFixed(3));t.style.setProperty('--y',((1-tin)*28-(1-tout)*28).toFixed(1));t.style.visibility=v<.03?'hidden':'visible'});
  btns.forEach(function(b,i){if(i===act)b.setAttribute('aria-current','true');else b.removeAttribute('aria-current')});bar.style.setProperty('--bp',p.toFixed(3))}}

/* ── 3 zoom pin ── */
function mZp(root){var sec=$('[data-zp]',root);if(!sec||RM)return null;sec.parentNode.classList.add('zp-on');sec.classList.add('zp-live');
 return function(vh){var r=sec.getBoundingClientRect(),tot=Math.max(1,r.height-vh),p=cl(-r.top/tot);
  sec.style.setProperty('--z',ez3(cl(p/.5)).toFixed(3));sec.style.setProperty('--o',cl((p-.42)/.2).toFixed(3));sec.style.setProperty('--c',ez3(cl((p-.7)/.28)).toFixed(3))}}

/* ── 4 zoom tunnel ── */
function mZt(root){var sec=$('[data-zt]',root);if(!sec||RM)return null;var fr=$$('.zt-f',sec),N=fr.length,K=2.1;sec.parentNode.classList.add('zt-on');
 return function(vh){var r=sec.getBoundingClientRect(),tot=Math.max(1,r.height-vh),p=cl(-r.top/tot),q=p*(N-1);
  fr.forEach(function(f,i){var s=Math.pow(K,q-i),o=cl((s-.2)/.22);if(i<N-1)o=Math.min(o,cl((3.4-s)/1.2));
   f.style.setProperty('--s',s.toFixed(4));f.style.setProperty('--o',o.toFixed(3));f.style.zIndex=N-i;f.style.visibility=o<.01?'hidden':'visible'});
  sec.style.setProperty('--ti',cl(1-q*2.2).toFixed(2))}}

/* ── 5 number morph ── */
function mNm(root){var sec=$('[data-nm]',root);if(!sec||RM)return null;
 var poly=$('polygon',sec),svg=$('.nm-svg',sec),nn=$('[data-nn]',sec),ns=$('[data-ns]',sec),labs=$$('.nm-l',sec),dots=$$('.nm-dots i',sec);
 var VAL=(sec.getAttribute('data-vals')||'12,48,150,1200').split(',').map(Number),SUF=(sec.getAttribute('data-suf')||'+,+,+,h').split(','),COL=['var(--c-primary)','var(--c-accent)','var(--c-secondary)','var(--c-primary)'],M=90,N=VAL.length,PI=Math.PI;
 function mod(a,b){return((a%b)+b)%b}
 var SH=[function(){return .9},function(t){var c=Math.abs(Math.cos(t)),s=Math.abs(Math.sin(t));return .68/Math.pow(Math.pow(c,10)+Math.pow(s,10),.1)},function(t){return .475/Math.cos(mod(t+PI/2,2*PI/3)-PI/3)},function(t){var u=mod(t+PI/2,2*PI/5)/(PI/5),tr=u<1?u:2-u;return .95-.55*tr}];
 var RAD=SH.map(function(f){var a=[];for(var k=0;k<M;k++)a.push(f(k/M*2*PI-PI/2));return a});
 sec.parentNode.classList.add('nm-on');
 return function(vh){var r=sec.getBoundingClientRect(),tot=Math.max(1,r.height-vh),p=cl(-r.top/tot),q=p*(N-1),i=Math.min(N-2,Math.floor(q)),t=eio(q-i),j=i+1,a=RAD[i],b=RAD[j],o=[];
  for(var k=0;k<M;k++){var th=k/M*2*PI-PI/2,rr=(a[k]+(b[k]-a[k])*t)*100;o.push((rr*Math.cos(th)).toFixed(1)+','+(rr*Math.sin(th)).toFixed(1))}
  poly.setAttribute('points',o.join(' '));svg.style.transform='rotate('+(q*40).toFixed(1)+'deg)';
  sec.style.setProperty('--ca',COL[i]);sec.style.setProperty('--cb',COL[j]);sec.style.setProperty('--k',t.toFixed(3));
  nn.textContent=Math.round(VAL[i]+(VAL[j]-VAL[i])*t).toLocaleString('en-US');ns.textContent=t<.5?SUF[i]:SUF[j];
  labs.forEach(function(l,s){l.style.setProperty('--v',cl(1-Math.abs(q-s)*3).toFixed(2))});dots.forEach(function(d,s){d.classList.toggle('on',s===Math.round(q))})}}

/* ── 6 path draw ── */
function mPd(root){var wrap=$('[data-pd]',root);if(!wrap||RM)return null;
 var svg=$('svg',wrap),bg=$('.pd-bg',wrap),fg=$('.pd-fg',wrap),items=$$('.pd-i',wrap),dots=items.map(function(i){return $('.pd-dot',i)}),L=0,samp=[],P=[];
 wrap.parentNode.classList.add('pd-live');
 var wr=wrap.getBoundingClientRect(),W0=wrap.offsetWidth,H0=wrap.offsetHeight;svg.setAttribute('viewBox','0 0 '+W0+' '+H0);
 P=dots.map(function(d){var r=d.getBoundingClientRect();return{x:r.left-wr.left+r.width/2,y:r.top-wr.top+r.height/2}});
 var d='M'+P[0].x+' 0 L'+P[0].x+' '+P[0].y;for(var i=1;i<P.length;i++){var a=P[i-1],b=P[i],m=(a.y+b.y)/2;d+=' C'+a.x+' '+m+' '+b.x+' '+m+' '+b.x+' '+b.y}
 bg.setAttribute('d',d);fg.setAttribute('d',d);L=fg.getTotalLength();fg.style.strokeDasharray=L+' '+L;
 for(var s=0;s<=240;s++){var pt=fg.getPointAtLength(L*s/240);samp.push([L*s/240,pt.y])}
 function lenAt(y){var lo=0,hi=samp.length-1;if(y<=samp[0][1])return 0;if(y>=samp[hi][1])return L;while(hi-lo>1){var m=(lo+hi)>>1;if(samp[m][1]<y)lo=m;else hi=m}return samp[lo][0]+(samp[hi][0]-samp[lo][0])*((y-samp[lo][1])/Math.max(1e-6,samp[hi][1]-samp[lo][1]))}
 return function(vh){var r=wrap.getBoundingClientRect(),head=vh*.62-r.top;fg.style.strokeDashoffset=(L-lenAt(head)).toFixed(1);items.forEach(function(it,i){it.classList.toggle('on',head>=P[i].y-4)})}}

/* ── 7 clip reveal ── */
function mCr(root){var els=$$('[data-cr]',root);if(!els.length||RM)return null;
 return function(vh){els.forEach(function(el){var r=el.getBoundingClientRect(),e=ez3(cl((vh*.92-r.top)/(vh*.55+r.height*.2)));el.style.setProperty('--p',e.toFixed(3));el.classList.toggle('cr-open',e>.995)})}}

/* ── 8 velocity skew ── */
function mVs(root){var list=$('[data-vs]',root);if(!list||RM)return null;if(list.__sk===undefined)list.__sk=0;
 return function(){var t=Math.max(-9,Math.min(9,vel.v*-.14));list.__sk+=(t-list.__sk)*.14;if(Math.abs(list.__sk)<.02&&Math.abs(vel.v)<.1)list.__sk=0;list.style.setProperty('--sk',list.__sk.toFixed(3));return list.__sk!==0}}

/* ── 9 rgb split ── */
function mRs(root){var tiles=$$('[data-rs]',root);if(!tiles.length||RM)return null;
 tiles.forEach(function(t){if(t.__rs)return;t.__rs=1;var svg=$('.rs-base',t).innerHTML;
  ['r','g','b'].forEach(function(c){var l=D.createElement('div');l.className='rs-l rs-'+c;l.setAttribute('aria-hidden','true');l.innerHTML=uid(svg);t.appendChild(l)});
  t.classList.add('rs-on');t.__vx=0;t.addEventListener('pointermove',function(e){if(e.pointerType==='touch')return;t.__vx=Math.max(-22,Math.min(22,t.__vx+(e.movementX||0)*.7));req()})});
 return function(){var busy=false,vy=Math.max(-26,Math.min(26,vel.v));tiles.forEach(function(t){t.__vx*=.88;if(Math.abs(t.__vx)<.05)t.__vx=0;else busy=true;t.style.setProperty('--vy',vy.toFixed(1));t.style.setProperty('--vx',t.__vx.toFixed(1))});return busy}}

/* ── 10 strip slices ── */
function mSp(root){var els=$$('[data-sp]',root),N=8;if(!els.length||RM)return null;
 els.forEach(function(el){if(el.__sp)return;el.__sp=1;var art=$('.ap-art',el),svg=art.innerHTML,w=D.createElement('div');w.className='sp-strips';w.setAttribute('aria-hidden','true');
  for(var i=0;i<N;i++){var s=D.createElement('div');s.className='sp-s';s.style.setProperty('--i',i);var n=D.createElement('div');n.className='sp-in';n.innerHTML=uid(svg);s.appendChild(n);w.appendChild(s)}
  el.appendChild(w);el.classList.add('sp-on');art.setAttribute('aria-hidden','true');el.setAttribute('role','img');el.setAttribute('aria-label',art.getAttribute('aria-label')||'')});
 return function(vh){els.forEach(function(el){var r=el.getBoundingClientRect();el.style.setProperty('--p',eq(cl((vh*.96-r.top)/(vh*.75))).toFixed(3))})}}

/* ── 11 mask text ── */
function mMt(root){var els=$$('[data-mt]',root);if(!els.length||RM)return null;
 return function(vh){els.forEach(function(el){var r=el.getBoundingClientRect();el.style.setProperty('--mp',cl((vh-r.top)/(vh+r.height)).toFixed(3))})}}

/* ── 12 text scramble ── */
var G='!<>-_\\/[]{}=+*^?#%&';function RC(){return G.charAt(Math.floor(Math.random()*G.length))}
function scRun(el){if(el.__raf)cancelAnimationFrame(el.__raf);var cs=el.__c,t0=performance.now(),dur=700+cs.length*16;
 cs.forEach(function(o){o.el.style.width='';o.el.textContent=o.ch;o.el.classList.remove('sc-u')});
 cs.forEach(function(o){o.w=o.el.getBoundingClientRect().width;o.s=Math.random()*dur*.4;o.e=o.s+dur*.45+Math.random()*dur*.2;o.last=0;o.fin=false});
 function f(now){var t=now-t0,done=true;cs.forEach(function(o){if(o.fin)return;
  if(t>=o.e){o.fin=true;o.el.textContent=o.ch;o.el.classList.remove('sc-u');o.el.style.width=''}
  else{done=false;if(!o.el.classList.contains('sc-u')){o.el.classList.add('sc-u');o.el.style.width=o.w+'px'}if(now-o.last>55){o.el.textContent=RC();o.last=now}}});
  el.__raf=done?0:requestAnimationFrame(f)}
 el.__raf=requestAnimationFrame(f)}
function mSc(root){if(RM)return;$$('[data-sc]',root).forEach(function(el){if(el.__c)return;var t=el.textContent.replace(/\s+/g,' ').trim();el.textContent='';
  var sr=D.createElement('span');sr.className='sc-sr';sr.textContent=t;el.appendChild(sr);var box=D.createElement('span');box.setAttribute('aria-hidden','true');el.appendChild(box);el.__c=[];
  t.split(' ').forEach(function(w,wi){if(wi)box.appendChild(D.createTextNode(' '));var ws=D.createElement('span');ws.className='sc-w';w.split('').forEach(function(ch){var c=D.createElement('span');c.className='sc-c';c.textContent=ch;ws.appendChild(c);el.__c.push({el:c,ch:ch})});box.appendChild(ws)});
  if('IntersectionObserver' in W){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){io.disconnect();scRun(el)}})},{threshold:.4});io.observe(el)}});
 $$('[data-sc-row]',root).forEach(function(a){if(a.__sr)return;a.__sr=1;var t=$('[data-sc]',a);if(!t||!t.__c)return;a.addEventListener('pointerenter',function(e){if(e.pointerType!=='touch')scRun(t)});a.addEventListener('focus',function(){scRun(t)})})}

/* ── 13 pointer fill ── */
function pfGeom(b,e){var r=b.getBoundingClientRect(),x=e?e.clientX-r.left:r.width/2,y=e?e.clientY-r.top:r.height/2;x=Math.max(0,Math.min(r.width,x));y=Math.max(0,Math.min(r.height,y));
 b.style.setProperty('--x',x+'px');b.style.setProperty('--y',y+'px');b.style.setProperty('--r',Math.hypot(Math.max(x,r.width-x),Math.max(y,r.height-y))+'px')}
function mPf(){$$('.pf').forEach(function(b){if(b.__pf)return;b.__pf=1;var t=0;
 function inn(e){pfGeom(b,e);b.classList.add('is-in')}function out(e){clearTimeout(t);pfGeom(b,e);b.classList.remove('is-in');b.style.transform=''}
 b.addEventListener('pointerenter',function(e){if(e.pointerType!=='touch')inn(e)});b.addEventListener('pointerleave',function(e){if(e.pointerType!=='touch')out(e)});
 b.addEventListener('pointermove',function(e){if(RM||e.pointerType==='touch')return;var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.12).toFixed(1)+'px,'+((e.clientY-r.top-r.height/2)*.2).toFixed(1)+'px)'});
 b.addEventListener('pointerdown',function(e){if(e.pointerType!=='touch')return;inn(e);clearTimeout(t);t=setTimeout(function(){out(null)},650)});
 b.addEventListener('focus',function(){if(b.matches(':focus-visible'))inn(null)});b.addEventListener('blur',function(){out(null)})})}

/* ── 14 image-follow list ── */
function mCf(root){$$('[data-cf]',root).forEach(function(blk){if(blk.__cf)return;blk.__cf=1;
 var list=$('.cf-list',blk),rows=$$('.cf-row',blk),fl=$('.cf-float',blk),arts=$$('.cf-a',fl);
 if(COARSE){rows.forEach(function(r,i){$('.cf-inline',r).appendChild(arts[i].cloneNode(true));r.addEventListener('click',function(e){if(!r.classList.contains('is-open')){e.preventDefault();rows.forEach(function(o){o.classList.remove('is-open')});r.classList.add('is-open')}})});return}
 var x=0,y=0,tx=0,ty=0,on=false,rf=0;
 function tick(){rf=0;var k=RM?1:.16,nx=x+(tx-x)*k,ny=y+(ty-y)*k,vx=nx-x;x=nx;y=ny;fl.style.transform='translate3d('+x.toFixed(1)+'px,'+y.toFixed(1)+'px,0) translate(-50%,-50%) rotate('+(RM?0:Math.max(-12,Math.min(12,vx*.5))).toFixed(2)+'deg)';if(on)rf=requestAnimationFrame(tick)}
 function show(i,snap){if(snap||!on){x=tx;y=ty}arts.forEach(function(a,k){a.classList.toggle('on',k===i)});rows.forEach(function(r,k){r.classList.toggle('is-on',k===i)});list.classList.add('cf-act');fl.classList.add('on');on=true;if(!rf)rf=requestAnimationFrame(tick)}
 function hide(){on=false;fl.classList.remove('on');list.classList.remove('cf-act');rows.forEach(function(r){r.classList.remove('is-on')})}
 rows.forEach(function(r,i){r.addEventListener('pointerenter',function(e){if(e.pointerType==='touch')return;tx=e.clientX;ty=e.clientY;show(i)});
  r.addEventListener('focus',function(){var b=r.getBoundingClientRect();tx=b.left+b.width*.74;ty=b.top+b.height/2;show(i,true)});r.addEventListener('blur',hide)});
 list.addEventListener('pointermove',function(e){if(e.pointerType==='touch')return;tx=e.clientX;ty=e.clientY});list.addEventListener('pointerleave',hide)})}

/* ── 15 liquid distort (WebGL, falls back to the drawn picture) ── */
var VS='attribute vec2 p;varying vec2 v;void main(){v=p*.5+.5;gl_Position=vec4(p,0.,1.);}';
var FS='precision mediump float;uniform sampler2D t;uniform vec2 m,sc;uniform float s,tm,asp;varying vec2 v;void main(){vec2 d=v-m;d.x*=asp;float r=length(d);float f=smoothstep(.55,0.,r);float w=sin(r*26.-tm*5.)*f;vec2 dir=r>.0001?d/r:vec2(0.);dir.x/=asp;vec2 u=v+dir*(w*.022*s)-(v-m)*f*.10*s;vec2 c=(u-.5)*sc+.5;float k=.006*s*f;gl_FragColor=vec4(texture2D(t,c+dir*k).r,texture2D(t,c).g,texture2D(t,c-dir*k).b,1.);}';
var VARS=['--c-primary','--c-secondary','--c-text','--c-accent','--c-surface','--c-border'];
function mLd(root){if(RM)return;$$('[data-ld]',root).forEach(function(el){if(el.__ld)return;el.__ld=1;
 var svg=$('svg',el);if(!svg)return;var cv=D.createElement('canvas');cv.setAttribute('aria-hidden','true');var gl=cv.getContext('webgl',{premultipliedAlpha:false,antialias:false});if(!gl)return;
 function sh(ty,src){var o=gl.createShader(ty);gl.shaderSource(o,src);gl.compileShader(o);return gl.getShaderParameter(o,gl.COMPILE_STATUS)?o:null}
 var vs=sh(gl.VERTEX_SHADER,VS),fs=sh(gl.FRAGMENT_SHADER,FS);if(!vs||!fs)return;var pr=gl.createProgram();gl.attachShader(pr,vs);gl.attachShader(pr,fs);gl.linkProgram(pr);if(!gl.getProgramParameter(pr,gl.LINK_STATUS))return;gl.useProgram(pr);
 var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);var lp=gl.getAttribLocation(pr,'p');gl.enableVertexAttribArray(lp);gl.vertexAttribPointer(lp,2,gl.FLOAT,false,0,0);
 var U={};['t','m','sc','s','tm','asp'].forEach(function(n){U[n]=gl.getUniformLocation(pr,n)});
 var cs=getComputedStyle(el),c=svg.cloneNode(true);c.setAttribute('xmlns','http://www.w3.org/2000/svg');c.setAttribute('width','800');c.setAttribute('height','1000');
 var st=D.createElementNS('http://www.w3.org/2000/svg','style');st.textContent='svg{'+VARS.map(function(n){return n+':'+cs.getPropertyValue(n).trim()}).join(';')+'}';c.insertBefore(st,c.firstChild);
 var im=new Image();im.onload=function(){start(im)};im.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(c));
 function start(img){var tx=gl.createTexture();gl.bindTexture(gl.TEXTURE_2D,tx);gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL,true);try{gl.texImage2D(gl.TEXTURE_2D,0,gl.RGBA,gl.RGBA,gl.UNSIGNED_BYTE,img)}catch(e){return}
  [[gl.TEXTURE_MIN_FILTER,gl.LINEAR],[gl.TEXTURE_MAG_FILTER,gl.LINEAR],[gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE],[gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE]].forEach(function(a){gl.texParameteri(gl.TEXTURE_2D,a[0],a[1])});
  el.appendChild(cv);var mx=.5,my=.5,s=0,tm=0,rf=0,last=0,Wd=0,Ht=0,down=false;
  function size(){var r=el.getBoundingClientRect(),d=Math.min(W.devicePixelRatio||1,2);Wd=Math.max(2,Math.round(r.width*d));Ht=Math.max(2,Math.round(r.height*d));if(cv.width!==Wd||cv.height!==Ht){cv.width=Wd;cv.height=Ht}gl.viewport(0,0,Wd,Ht)}
  function draw(){var a=Wd/Ht,ia=.8,scl=a>ia?[1,ia/a]:[a/ia,1];gl.uniform1i(U.t,0);gl.uniform2f(U.m,mx,my);gl.uniform2f(U.sc,scl[0],scl[1]);gl.uniform1f(U.s,s);gl.uniform1f(U.tm,tm);gl.uniform1f(U.asp,a);gl.drawArrays(gl.TRIANGLE_STRIP,0,4)}
  function tick(now){rf=0;var dt=Math.min(.05,(now-last)/1000||.016);last=now;tm+=dt;s*=Math.pow(.04,dt);if(s<.004)s=0;size();draw();if(s>0||down)rf=requestAnimationFrame(tick)}
  function kick(){if(!rf){last=performance.now();rf=requestAnimationFrame(tick)}}
  function pos(e){var r=el.getBoundingClientRect();return[(e.clientX-r.left)/r.width,1-(e.clientY-r.top)/r.height]}
  el.addEventListener('pointermove',function(e){var p=pos(e),dx=p[0]-mx,dy=p[1]-my;mx=p[0];my=p[1];s=Math.min(1,Math.max(s,Math.sqrt(dx*dx+dy*dy)*14+(down?.5:0)));kick()});
  el.addEventListener('pointerdown',function(e){var p=pos(e);mx=p[0];my=p[1];s=1;down=true;tm=0;kick()});W.addEventListener('pointerup',function(){down=false});el.addEventListener('pointerleave',function(){down=false});
  size();draw();el.classList.add('ld-ready');if(W.ResizeObserver)new ResizeObserver(function(){size();draw()}).observe(el)}})}

/* ── small UI: filters, print picker, forms ── */
function ui(root){
 $$('[data-filter]',root).forEach(function(box){if(box.__f)return;box.__f=1;var chips=$$('.bh-chip',box),tgt=$(box.getAttribute('data-filter'),root)||root,n=$('[data-count]',root);
  chips.forEach(function(c){c.addEventListener('click',function(){chips.forEach(function(o){o.setAttribute('aria-pressed',o===c)});var f=c.getAttribute('data-f'),k=0;
   $$('[data-s]',tgt).forEach(function(it){var show=f==='all'||it.getAttribute('data-s').split(' ').indexOf(f)>-1;it.hidden=!show;if(show)k++});if(n)n.textContent=k})})});
 var pk=$('[data-picker]',root);if(pk&&!pk.__p){pk.__p=1;var size=1,fin=0;
  function price(){$$('[data-base]',root).forEach(function(el){var b=+el.getAttribute('data-base');el.textContent='RM '+Math.round(b*size+fin).toLocaleString('en-US')})}
  $$('input[name=sz]',pk).forEach(function(i){i.addEventListener('change',function(){size=+i.value;price()})});$$('input[name=fn]',pk).forEach(function(i){i.addEventListener('change',function(){fin=+i.value;price()})});
  $$('[data-add]',root).forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var o=b.textContent;b.textContent='Added to your list';setTimeout(function(){b.textContent=o},1600)})});price()}
 $$('form[data-form]',root).forEach(function(f){if(f.__fm)return;f.__fm=1;f.addEventListener('submit',function(e){e.preventDefault();var ok=$('.bh-ok',f.parentNode);if(ok){ok.classList.add('on');ok.focus&&ok.focus()}f.reset()})});
 $$('[data-top]',root).forEach(function(a){if(a.__t)return;a.__t=1;a.addEventListener('click',function(e){e.preventDefault();W.scrollTo({top:0,behavior:RM?'auto':'smooth'})})})}

/* ── boot ── */
var mo=null,rt=0;
function watch(){if(mo||!W.MutationObserver)return;var ms=$$('main[data-page]');if(!ms.length)return;mo=new MutationObserver(function(){clearTimeout(rt);rt=setTimeout(init,30)});ms.forEach(function(m){mo.observe(m,{attributes:true,attributeFilter:['class']})})}
function init(){var root=active();ups=[];watch();
 [mSl,mSs,mZp,mZt,mNm,mPd,mCr,mVs,mRs,mSp,mMt].forEach(function(m){try{var u=m(root);if(u)ups.push(u)}catch(e){}});
 try{mSc(root);mPf();mCf(root);mLd(root);ui(root);menu()}catch(e){}
 navSync(root);req()}
W.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(init,180)});
W.addEventListener('scroll',req,{passive:true});
D.addEventListener('DOMContentLoaded',init);if(D.readyState!=='loading')init();
if(D.fonts&&D.fonts.ready)D.fonts.ready.then(function(){setTimeout(init,50)});
})();
"""
