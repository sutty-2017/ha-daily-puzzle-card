// Card interaction regression tests. DOM only: does not claim layout verification.
const {JSDOM}=require('jsdom');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const dom=new JSDOM('<!DOCTYPE html><body></body>',{runScripts:'dangerously',url:'http://localhost'});
const w=dom.window;
w.eval(fs.readFileSync(path.join(__dirname,'../custom_components/daily_puzzle/www/daily-puzzle-card.js'),'utf8'));
const card=w.document.createElement('daily-puzzle-card');
card.setConfig({hybrid_style:true});w.document.body.append(card);
let state={date:'2026-11-13',game:'word_links',status:'not_started',admin_mode:true,hints_enabled:true,completed:false,
 game_state:{puzzle_id:'fixture',rows:['BIRD','H____','P____','F___','C____','R_______','T___'],active_index:1,revision:0,mistakes:0,mistake_limit:6,hints_used:0,hint_available:true,solved_words:[]}};
const words=['BIRD','HOUSE','PLANT','FOOD','CHAIN','REACTION','TIME'];
let fail=false,calls=[];
function refresh(){
 const states={};
 for(const [key,value,attributes] of [['status',state.status,state],['game',state.game,{}],['time_remaining','12:00:00',{}]])states['sensor.daily_puzzle_'+key]={entity_id:'sensor.daily_puzzle_'+key,state:value,attributes};
 states['binary_sensor.daily_puzzle_completed']={entity_id:'binary_sensor.daily_puzzle_completed',state:state.completed?'on':'off'};
 card.hass={states,callService:async(domain,name,data)=>{
  calls.push({name,data});if(fail){fail=false;throw new Error('offline')}
  let g=state.game_state;
  if(name==='submit_link'){
   g.revision++;
   if(data.guess===words[g.active_index]){
    g.solved_words.push(data.guess);g.rows[g.active_index]=data.guess;g.active_index++;g.last_result='correct';
    if(g.active_index===7){state.status='solved';state.completed=true;state.completed_board=JSON.parse(JSON.stringify(g))}
   }else{g.mistakes++;g.last_result='incorrect';if(g.mistakes===6)state.status='failed'}
  }else if(name==='use_hint'){g.hints_used++;g.rows[g.active_index]=words[g.active_index].slice(0,2)+'_'.repeat(words[g.active_index].length-2)}
  refresh();
 }};
}
const $=s=>w.document.querySelector(s);
const flush=()=>new Promise(resolve=>setImmediate(resolve));
function fill(value){$('#link-guess').value=value;$('#link-guess').dispatchEvent(new w.Event('input'))}
function enter(){ $('.link-form').dispatchEvent(new w.Event('submit',{cancelable:true})); }
(async()=>{
 refresh();card.open();
 assert.equal($('h2').textContent,'Word Links');assert.equal(w.document.querySelectorAll('.link-row').length,7);
 assert.equal($('#admin-game option[value="word_links"]').textContent,'Word Links');
 fill('ho');assert.equal($('#link-guess').value,'HO');
 const original=$('#link-guess');original.focus();refresh();
 assert.equal($('#link-guess'),original,'unrelated updates must retain input node');
 assert.equal($('#link-guess').value,'HO');
 $('#link-hint').click();await flush();
 assert.equal($('#link-guess').value,'HO','hint updates retain typed draft');
 assert.equal(w.document.activeElement,$('#link-guess'),'hint update retains focus');
 fill('HOUSE');fail=true;enter();await flush();
 assert.match($('.link-status').textContent,/Could not submit/);assert.equal($('#link-guess').value,'HOUSE');assert.equal($('#link-guess').disabled,false);
 enter();await flush();assert.equal(state.game_state.active_index,2);assert.equal($('#link-guess').value,'');
 for(const char of 'PLANT')$(`[data-link-key="${char}"]`).click();
 $('[data-link-key="ENTER"]').click();await flush();
 assert.equal(state.game_state.active_index,3);assert.equal($('#link-guess').value,'');
 card.close();card.open();assert.equal(w.document.querySelectorAll('.solved-link').length,3);
 // Another client solving the active word must discard this client's stale draft.
 fill('ZZ');state.game_state.solved_words.push('FOOD');state.game_state.rows[3]='FOOD';state.game_state.active_index=4;refresh();
 assert.equal($('#link-guess').value,'');
 for(const word of words.slice(4)){fill(word);enter();await flush()}
 assert.match($('h2').textContent,/Word Links/);assert.equal($('.links-saved').textContent,words.join(' → '));
 assert.ok($('#replay'));
 // Reveal screen includes the complete chain and shared retry controls.
 state.status='failed';state.game_state.answer_revealed=true;state.game_state.revealed_words=words;refresh();
 assert.equal($('.links-saved').textContent,words.join(' → '));assert.ok($('#retry'));
 card.close();card.remove();dom.window.close();
 console.log('PASS: DOM input stability, focus, hint, transport failure/retry, touch keyboard, remote progress, completed/revealed boards, admin selector.');
})().catch(error=>{console.error(error);dom.window.close();process.exitCode=1});
