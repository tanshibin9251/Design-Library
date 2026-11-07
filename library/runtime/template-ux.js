/* Runs in previews AND exported files. No requests, credentials or submissions. */
(function(){
 'use strict';
 function start(){
  var root=document.querySelector('[data-dl-template]');if(!root)return;
  document.querySelectorAll('[data-dl-demo-form]').forEach(function(form,index){
   if(form.dataset.dlBound)return;form.dataset.dlBound='1';
   var note=document.createElement('p');note.className='dl-form-note';note.textContent='Interactive demo · Nothing is sent. Use sample details only. No account, booking or payment will be created.';form.prepend(note);
   var result=document.createElement('p');result.className='dl-feedback';result.setAttribute('role','status');result.setAttribute('aria-live','polite');result.hidden=true;form.append(result);
   form.querySelectorAll('input,textarea,select').forEach(function(input,i){
    if(!input.name)input.name='demo-'+index+'-'+i;
    var label=input.closest('label'),text=(label?label.textContent:input.placeholder||'').toLowerCase();
    if(/name|email|message|date|time/.test(text)&&!/optional/.test(text))input.required=true;
    if(input.type==='password')input.autocomplete='new-password';
    if(/card number|cvc|expiry/.test(text)){input.disabled=true;input.placeholder='Disabled in demo';}
   });
   function submit(e){if(e)e.preventDefault();if(!form.reportValidity())return;result.hidden=false;result.textContent='Demo complete. Your entries passed the browser checks. Nothing was sent, charged, booked or stored.';}
   form.addEventListener('submit',submit);
   if(!form.querySelector('[type="submit"],button:not([type])')){var buttons=form.querySelectorAll('button[type="button"]');if(buttons.length===1)buttons[0].addEventListener('click',submit);}
  });
  document.querySelectorAll('.dl-visual img').forEach(function(img){img.addEventListener('error',function(){img.parentElement.classList.add('dl-photo-failed')});if(img.complete&&!img.naturalWidth)img.parentElement.classList.add('dl-photo-failed')});
  document.querySelectorAll('.shoptop').forEach(function(top){
   var grid=top.nextElementSibling;if(!grid||!grid.matches('.products'))return;
   var cards=Array.from(grid.children),chips=Array.from(top.querySelectorAll('.chip')),sort=top.querySelector('select'),category='All';
   var empty=document.createElement('p');empty.className='dl-filter-empty';empty.textContent='No sample items match this category. Choose All to see the collection.';empty.hidden=true;grid.after(empty);
   function update(){var shown=0;cards.forEach(function(card){var tag=card.querySelector('small');card.hidden=category!=='All'&&(!tag||tag.textContent.trim()!==category);if(!card.hidden)shown++});empty.hidden=shown!==0;var count=top.querySelector('.sort span');if(count)count.textContent=shown+' sample items';}
   chips.forEach(function(chip){chip.type='button';chip.setAttribute('aria-pressed',chip.classList.contains('on'));chip.addEventListener('click',function(){category=chip.textContent.trim();chips.forEach(function(c){c.classList.toggle('on',c===chip);c.setAttribute('aria-pressed',c===chip)});update()})});
   if(sort){sort.setAttribute('aria-label','Sort sample items');Array.from(sort.options).forEach(function(o){if(/newest/i.test(o.textContent))o.textContent='Reverse featured'});sort.addEventListener('change',function(){var ordered=cards.slice();if(sort.selectedIndex===1||sort.selectedIndex===2){ordered.sort(function(a,b){function price(c){var p=c.querySelector('.price');return Number((p?p.textContent:'').replace(/[^0-9.]/g,''))||0}return price(a)-price(b)});if(sort.selectedIndex===2)ordered.reverse()}else if(sort.selectedIndex===3)ordered.reverse();ordered.forEach(function(card){grid.append(card)})})}
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('.burger[open],.dl-mobile[open],.nav details[open]').forEach(function(menu){menu.open=false;var summary=menu.querySelector('summary');if(summary)summary.focus()})});
  document.addEventListener('click',function(e){var a=e.target.closest('.dl-mobile a,.bmenu a');if(a){var menu=a.closest('details');if(menu)menu.open=false;}});
  document.querySelectorAll('.more>a[href="#"]').forEach(function(a){a.setAttribute('role','button');a.setAttribute('aria-expanded','false');function set(open){a.parentElement.classList.toggle('dl-menu-open',open);a.setAttribute('aria-expanded',open)}function toggle(e){e.preventDefault();set(a.getAttribute('aria-expanded')!=='true')}a.addEventListener('click',toggle);a.addEventListener('keydown',function(e){if(e.key===' ')toggle(e)});a.parentElement.addEventListener('mouseenter',function(){set(true)});a.parentElement.addEventListener('mouseleave',function(){if(!a.parentElement.contains(document.activeElement))set(false)})});
  document.addEventListener('click',function(e){var a=e.target.closest('a[href="#"]');if(!a||e.defaultPrevented||a.onclick||a.closest('.more'))return;e.preventDefault();var note=a.parentElement.querySelector(':scope>.dl-missing-link');if(!note){note=document.createElement('p');note.className='dl-feedback dl-missing-link';note.setAttribute('role','status');a.after(note)}note.textContent='Demonstration link. Add the real destination before launching this site.'});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')document.querySelectorAll('.dl-menu-open').forEach(function(menu){menu.classList.remove('dl-menu-open');var a=menu.querySelector(':scope>a');if(a){a.setAttribute('aria-expanded','false');a.focus()}})});
  document.querySelectorAll('.dl-skip').forEach(function(link){link.addEventListener('click',function(e){e.preventDefault();var target=document.querySelector('main.on [data-dl-content],main:not([data-page]) [data-dl-content]');if(target){target.focus();target.scrollIntoView({block:'start'})}})});
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
})();
