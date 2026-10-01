const WORDS = ["CRANE","PLANT","SHORE","MUSIC","LIGHT","BREAD","CLOUD","TRAIN","HOUSE","SMILE","GRAPE","STONE"];
const GROUPS = [
  [
    {label:"Things that can be sharp", words:["KNIFE","IMAGE","TURN","CHEDDAR"]},
    {label:"Things with keys", words:["PIANO","LOCK","MAP","KEYBOARD"]},
    {label:"___ ball", words:["BASE","CRYSTAL","CURVE","DISCO"]},
    {label:"Kinds of jack", words:["BLACK","UNION","LUMBER","MONTEREY"]}
  ],
  [
    {label:"Can be broken",words:["RECORD","PROMISE","BONE","CODE"]},
    {label:"Found on a desk",words:["PEN","MOUSE","PAPER","STAPLER"]},
    {label:"Types of roll",words:["DINNER","HONOR","BARREL","CINNAMON"]},
    {label:"Go with blue",words:["BERRY","BIRD","PRINT","MOON"]}
  ]
];

function localDateKey(){const d=new Date();return [d.getFullYear(),String(d.getMonth()+1).padStart(2,"0"),String(d.getDate()).padStart(2,"0")].join("-");}
function dayNumber(){return Math.floor(new Date(localDateKey()+"T12:00:00").getTime()/86400000);}
function shuffle(items, seed){const a=[...items];let x=seed||1;for(let i=a.length-1;i>0;i--){x=(x*1664525+1013904223)>>>0;const j=x%(i+1);[a[i],a[j]]=[a[j],a[i]];}return a;}
function wordScore(answer,guess){const out=Array(5).fill("absent"), counts={};for(let i=0;i<5;i++){if(guess[i]===answer[i])out[i]="correct";else counts[answer[i]]=(counts[answer[i]]||0)+1;}for(let i=0;i<5;i++){if(out[i]==="correct")continue;if((counts[guess[i]]||0)>0){out[i]="present";counts[guess[i]]--;}}return out;}

class DailyPuzzleCard extends HTMLElement {
  setConfig(config){this.config={title:"Daily Puzzle",hide_after:600,...config};this.render();}
  set hass(hass){this._hass=hass;this.render();}
  getCardSize(){return 6;}
  getGridOptions(){return {columns:6,min_columns:4,rows:"auto"};}
  stateObj(){return this._hass?.states?.["sensor.daily_puzzle_status"] || Object.values(this._hass?.states||{}).find(s=>s.entity_id.startsWith("sensor.")&&s.attributes?.friendly_name==="Daily Puzzle Status");}
  async save(game,state,status){if(!this._hass)return;await this._hass.callService("daily_puzzle","update_game",{game,status,game_state:state});}
  hiddenAfterSolve(s){if(s?.state!=="solved"||!s.attributes?.completed_at)return false;return Date.now()-new Date(s.attributes.completed_at).getTime()>(this.config.hide_after*1000);}
  render(){
    if(!this._hass||!this.config)return;
    const s=this.stateObj();
    if(this.hiddenAfterSolve(s)){this.innerHTML="";this.style.display="none";return;}
    this.style.display="";
    const game=(s?.attributes?.date===localDateKey()?this._hass.states["sensor.daily_puzzle_game"]?.state:null)||(dayNumber()%2?"four_of_a_kind":"word_grid");
    const state=s?.attributes?.date===localDateKey()?(s.attributes.game_state||{}):{};
    this.innerHTML=`<ha-card><style>
      .wrap{padding:16px}.head{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-bottom:16px}.title{font-size:20px;font-weight:600}.stats{font-size:13px;color:var(--secondary-text-color)}
      .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile,.key{border:0;border-radius:10px;background:var(--secondary-background-color);color:var(--primary-text-color);font-weight:700;min-height:52px;padding:8px;cursor:pointer}.tile.sel{outline:2px solid var(--primary-color)}
      .actions{display:flex;gap:8px;justify-content:center;margin-top:12px;flex-wrap:wrap}.action{border:0;border-radius:18px;padding:9px 14px;background:var(--primary-color);color:var(--text-primary-color);cursor:pointer}
      .row{display:flex;gap:6px;justify-content:center;margin:6px 0}.letter{width:42px;height:42px;display:grid;place-items:center;border:2px solid var(--divider-color);font-weight:800;font-size:20px}.correct{background:#538d4e;color:white;border-color:#538d4e}.present{background:#b59f3b;color:white;border-color:#b59f3b}.absent{background:#3a3a3c;color:white;border-color:#3a3a3c}
      input{box-sizing:border-box;width:100%;font-size:18px;padding:12px;text-transform:uppercase;background:var(--card-background-color);color:var(--primary-text-color);border:1px solid var(--divider-color);border-radius:10px}.msg{text-align:center;margin:12px 0;font-weight:600}.solved{padding:18px;text-align:center;font-size:18px}
    </style><div class="wrap"><div class="head"><div class="title">${this.config.title}</div><div class="stats">🔥 ${this._hass.states["sensor.daily_puzzle_daily_streak"]?.state??0} · 🏆 ${this._hass.states["sensor.daily_puzzle_best_daily_streak"]?.state??0}</div></div><div id="game"></div></div></ha-card>`;
    if(s?.state==="solved"){this.querySelector("#game").innerHTML='<div class="solved">🎉 Today’s puzzle solved!<br><small>This card will disappear shortly.</small></div>';return;}
    game==="word_grid"?this.renderWord(state):this.renderGroups(state);
  }
  renderWord(state){
    const answer=WORDS[dayNumber()%WORDS.length], guesses=state.guesses||[], root=this.querySelector("#game");
    root.innerHTML=guesses.map(g=>`<div class="row">${g.word.split("").map((c,i)=>`<div class="letter ${g.score[i]}">${c}</div>`).join("")}</div>`).join("")+`<div class="msg">Guess the five-letter word</div><input id="guess" maxlength="5" autocomplete="off" aria-label="Five letter guess"><div class="actions"><button class="action" id="submit">Guess</button></div>`;
    this.querySelector("#submit").addEventListener("click",async()=>{const input=this.querySelector("#guess"),g=input.value.trim().toUpperCase();if(!/^[A-Z]{5}$/.test(g)){input.setCustomValidity("Enter five letters.");input.reportValidity();return;}const score=wordScore(answer,g),next=[...guesses,{word:g,score}];await this.save("word_grid",{guesses:next},g===answer?"solved":"in_progress");});
  }
  renderGroups(state){
    const puzzle=GROUPS[dayNumber()%GROUPS.length], solved=state.solved||[], selected=new Set(), remaining=puzzle.flatMap(g=>g.words).filter(w=>!solved.includes(w)), root=this.querySelector("#game");
    root.innerHTML=solved.length?`<div class="msg">${solved.length/4} of 4 groups found</div>`:"";
    const grid=document.createElement("div");grid.className="grid";shuffle(remaining,dayNumber()).forEach(w=>{const b=document.createElement("button");b.className="tile";b.textContent=w;b.addEventListener("click",()=>{selected.has(w)?selected.delete(w):selected.size<4&&selected.add(w);b.classList.toggle("sel",selected.has(w));});grid.appendChild(b);});root.appendChild(grid);
    const actions=document.createElement("div");actions.className="actions";actions.innerHTML='<button class="action" id="submit-group">Submit 4</button>';root.appendChild(actions);
    this.querySelector("#submit-group").addEventListener("click",async()=>{if(selected.size!==4)return;const pick=[...selected], match=puzzle.find(g=>g.words.every(w=>selected.has(w)));if(!match){root.insertAdjacentHTML("beforeend",'<div class="msg">Not a group — try again.</div>');return;}const next=[...solved,...pick];await this.save("four_of_a_kind",{solved:next},next.length===16?"solved":"in_progress");});
  }
}
customElements.define("daily-puzzle-card",DailyPuzzleCard);
window.customCards=window.customCards||[];
window.customCards.push({type:"daily-puzzle-card",name:"Daily Puzzle",description:"A shared daily word puzzle for your household.",documentationURL:"https://github.com/sutty-2017/ha-daily-puzzle-card"});
