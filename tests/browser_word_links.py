"""Browser regression check using the real card and manager with fake HA transport.
Run separately: python tests/browser_word_links.py (requires Playwright + Chromium).
"""
import asyncio
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from test_word_links import Manager, Store, const, clock, types, datetime, links, date

ROOT=Path(__file__).resolve().parents[1]
entry=types.SimpleNamespace(options={'admin_mode': True, 'enabled_games':['word_links']})
m=Manager(types.SimpleNamespace(), entry)
asyncio.run(m.async_load())
words=links.links_for_date(date(2026,11,13))['words']

def payload():
    return dict(m.state, game_state=m.public_game_state(), admin_mode=True, hints_enabled=True, enabled_games=m.enabled_games)

calls=[]
fail_next=False

async def service(name, data):
    global fail_next
    calls.append((name,data))
    if fail_next:
        fail_next=False
        raise RuntimeError('Simulated connection failure')
    if name=='submit_link': await m.async_submit_link(data['guess'],data['date'],data['index'],data['revision'])
    elif name=='use_hint': await m.async_use_hint()
    elif name=='replay': await m.async_replay()
    elif name=='admin_switch_game': await m.async_admin_switch_game(data['game'])
    elif name=='admin_reset': await m.async_admin_reset()
    elif name=='return_to_daily': await m.async_return_to_daily()
    elif name=='reveal_answer': await m.async_reveal_answer()
    return payload()

with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':800,'height':480})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.expose_function('service',service)
    page.set_content('''<style>body{background:#142630;color:#fff;font-family:Arial;--card-background-color:#21343d;--primary-text-color:#fff;--secondary-text-color:#b4c5ce;--primary-color:#e99442;--secondary-background-color:#344954;--divider-color:#728088;--text-primary-color:#fff}daily-puzzle-card{display:block;width:420px;height:280px}</style>''')
    page.add_script_tag(path=str(ROOT/'custom_components/daily_puzzle/www/daily-puzzle-card.js'))
    page.evaluate('''()=>{
      window.card=document.createElement('daily-puzzle-card');card.setConfig({hybrid_style:true});document.body.appendChild(card);
      window.applyState=s=>{window.current=s;const states={};
       for(const [key,state,attributes] of [['status',s.status,s],['game',s.game,{}],['time_remaining','12:00:00',{}],['daily_streak',s.streak,{}],['puzzles_solved',s.puzzles_solved,{}],['no_hint_solves',s.no_hint_solves,{}]])states['sensor.daily_puzzle_'+key]={entity_id:'sensor.daily_puzzle_'+key,state,attributes};
       states['binary_sensor.daily_puzzle_completed']={entity_id:'binary_sensor.daily_puzzle_completed',state:s.completed?'on':'off',attributes:{}};
       card.hass={states,callService:async(domain,name,data)=>applyState(await window.service(name,data))};
      };
    }''')
    page.evaluate('applyState',payload())
    page.locator('#card').click()
    assert page.locator('h2').inner_text()=='Word Links'
    assert page.locator('.link-row').count()==7
    field=page.locator('#link-guess')
    field.fill('AB')
    # Unrelated HA state/countdown changes must preserve the same input DOM node.
    page.evaluate('window.savedInput=document.querySelector("#link-guess");applyState(current)')
    assert page.evaluate('savedInput===document.querySelector("#link-guess")')
    assert field.input_value()=='AB'
    page.locator('#link-hint').click()
    page.wait_for_function('current.game_state.hints_used===1')
    assert field.input_value()=='AB'
    # Service failure retains input and unlocks controls for retry.
    fail_next=True
    field.fill(words[1]);field.press('Enter')
    page.get_by_role('status').filter(has_text='Could not submit').wait_for()
    assert field.input_value()==words[1]
    assert field.is_enabled()
    field.press('Enter')
    page.wait_for_function('current.game_state.active_index===2')
    assert field.input_value()==''
    # Touch keyboard works without the native keyboard.
    for char in words[2]: page.locator(f'[data-link-key="{char}"]').click()
    page.locator('[data-link-key="ENTER"]').click()
    page.wait_for_function('current.game_state.active_index===3')
    # Minimize/reopen retains shared progress.
    page.locator('#x').click();page.locator('#card').click()
    assert page.locator('.solved-link').count()==3
    # No horizontal overflow even at narrow portrait sizes.
    for width,height in [(800,480),(480,800),(360,740),(1280,800)]:
        page.set_viewport_size({'width':width,'height':height})
        assert page.evaluate('document.querySelector(".modal").scrollWidth<=document.querySelector(".modal").clientWidth'), (width,height)
    page.set_viewport_size({'width':800,'height':480})
    page.screenshot(path='/tmp/word-links-preview.png')
    # Correct completion and saved board, then replay without duplicate credit.
    for word in words[3:]:
        field.fill(word);field.press('Enter')
        page.wait_for_function('(w)=>current.game_state.solved_words.includes(w)',arg=word)
    page.get_by_text('🎉 Puzzle complete').wait_for()
    assert page.locator('.links-saved').inner_text()==' → '.join(words)
    page.locator('#replay').click()
    page.wait_for_function('current.replay_mode===true')
    assert page.locator('.badge').inner_text().startswith('✓ Already completed today')
    # Admin switching exposes new game and restores official replay on return.
    page.locator('#admin-game').select_option('word_grid');page.locator('#admin-switch').click()
    page.wait_for_function('current.game==="word_grid"')
    page.locator('#admin-game').select_option('word_links');page.locator('#admin-switch').click()
    page.wait_for_function('current.game==="word_links"')
    assert page.locator('.link-row').count()==7
    page.locator('#admin-daily').click()
    page.wait_for_function('!current.test_mode')
    # Six incorrect answers -> reveal and retry flow.
    for i in range(6):
        field.fill('Z'*len(words[1]));field.press('Enter')
        page.wait_for_function('(n)=>current.game_state.mistakes===n',arg=i+1)
    page.locator('#reveal').click()
    page.wait_for_function('current.game_state.answer_revealed')
    assert page.locator('.links-saved').inner_text()==' → '.join(words)
    page.locator('#retry').click()
    page.wait_for_function('current.status==="not_started"')
    assert field.input_value()==''
    assert not errors, errors
    print('PASS: real Chromium card/manager flow, input stability, hints, failed service retry, touch keyboard, four viewports, completion/replay, admin, failure/reveal.')
    browser.close()
