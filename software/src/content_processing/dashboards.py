"""Dashboard generation logic.

Refactored from software/scripts/generate_dashboards.py.
"""

import json
import random
import re
from html import escape
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from src.batch_processing.utils import extract_course_info_from_path as extract_course_info, prettify_name

THEMES = {
    "ai-philosophy":         {"accent": "#38bdf8", "gradient": "135deg, #0ea5e9, #6366f1"},
    "ai-101":                {"accent": "#22d3ee", "gradient": "135deg, #06b6d4, #8b5cf6"},
    "ai-401":                {"accent": "#a78bfa", "gradient": "135deg, #8b5cf6, #ec4899"},
    "ai-es":                 {"accent": "#4ade80", "gradient": "135deg, #22c55e, #06b6d4"},
    "ai-family":             {"accent": "#fb923c", "gradient": "135deg, #f97316, #eab308"},
    "ai-hs":                 {"accent": "#818cf8", "gradient": "135deg, #6366f1, #a855f7"},
    "ai-ms":                 {"accent": "#2dd4bf", "gradient": "135deg, #14b8a6, #3b82f6"},
    "ai-embodied":           {"accent": "#fb7185", "gradient": "135deg, #f43f5e, #a855f7"},
    "ai-organizations":      {"accent": "#fbbf24", "gradient": "135deg, #f59e0b, #ef4444"},
    "ai-robotics":           {"accent": "#34d399", "gradient": "135deg, #10b981, #0ea5e9"},
}
DEFAULT_THEME = {"accent": "#38bdf8", "gradient": "135deg, #6366f1, #a855f7"}

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>__PAGE_TITLE__</title>
    <style>
        :root {
            --accent: __ACCENT__;
            --accent-glow: __ACCENT__22;
            --bg: #0f172a;
            --card: #1e293b;
            --border: #334155;
            --text: #e2e8f0;
            --muted: #94a3b8;
            --dim: #64748b;
            --green: #22c55e;
            --red: #ef4444;
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { font-family:'Segoe UI',system-ui,-apple-system,sans-serif; background:var(--bg); color:var(--text); line-height:1.6; }

        /* Hero */
        .hero { background:linear-gradient(__GRADIENT__); padding:48px 24px 36px; text-align:center; }
        .hero h1 { font-size:2rem; color:#fff; margin-bottom:8px; }
        .hero .sub { font-size:1.1rem; color:rgba(255,255,255,.85); margin-bottom:12px; }
        .hero .tag { display:inline-block; background:rgba(255,255,255,.2); color:#fff; padding:4px 14px; border-radius:20px; font-size:.8rem; backdrop-filter:blur(4px); }

        /* Nav */
        .nav { display:flex; justify-content:center; gap:6px; flex-wrap:wrap; padding:14px 24px; background:#1a2332; border-bottom:1px solid var(--border); }
        .nav a { color:var(--muted); text-decoration:none; font-size:.85rem; padding:6px 14px; border:1px solid var(--border); border-radius:8px; transition:all .2s; }
        .nav a:hover,.nav a.active { color:var(--accent); border-color:var(--accent); background:var(--accent-glow); }

        .content { max-width:1100px; margin:0 auto; padding:24px; }
        .stitle { color:var(--accent); font-size:1.25rem; margin:32px 0 16px; padding-bottom:8px; border-bottom:2px solid var(--border); }
        .stitle:first-child { margin-top:0; }

        /* Cards */
        .cgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; }
        .concept-card { background:var(--card); padding:20px; border-radius:12px; border:1px solid var(--border); cursor:pointer; transition:transform .2s,border-color .2s; }
        .concept-card:hover { transform:translateY(-2px); border-color:var(--accent); }
        .concept-card h3 { display:flex; justify-content:space-between; align-items:center; font-size:1rem; margin-bottom:8px; }
        .concept-card h3 .toggle { font-size:1.2rem; color:var(--dim); transition:transform .3s; }
        .concept-card.open h3 .toggle { transform:rotate(45deg); }
        .concept-card .brief { color:var(--muted); font-size:.9rem; }
        .concept-card .detail { display:none; color:var(--muted); font-size:.85rem; margin-top:12px; padding-top:12px; border-top:1px solid var(--border); line-height:1.7; }
        .concept-card.open .detail { display:block; }
        .meter { background:var(--border); border-radius:8px; height:6px; overflow:hidden; margin-top:14px; }
        .meter-fill { height:100%; border-radius:8px; background:linear-gradient(90deg,var(--accent),__ACCENT__88); transition:width 1s ease; }
        .meter-label { color:var(--dim); font-size:.7rem; margin-top:4px; }

        /* Quiz */
        .quiz-box { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .qprog { color:var(--dim); font-size:.85rem; margin-bottom:12px; }
        .qq { font-size:1rem; margin-bottom:16px; font-weight:500; }
        .qbtn { background:rgba(255,255,255,.03); color:var(--text); border:1px solid var(--border); padding:12px 16px; border-radius:10px; cursor:pointer; display:block; width:100%; text-align:left; margin:6px 0; transition:all .2s; font-size:.9rem; }
        .qbtn:hover:not(:disabled) { background:rgba(255,255,255,.08); border-color:var(--accent); }
        .qbtn.correct { background:#166534; border-color:var(--green); color:#bbf7d0; }
        .qbtn.wrong { background:#7f1d1d; border-color:var(--red); color:#fecaca; }
        .qbtn:disabled { cursor:default; opacity:.85; }
        .qexp { margin-top:12px; padding:12px; border-radius:10px; font-size:.9rem; display:none; animation:fadeIn .3s; }
        @keyframes fadeIn { from{opacity:0;transform:translateY(4px)} to{opacity:1;transform:translateY(0)} }
        .qnav { display:flex; gap:8px; margin-top:16px; }
        .qnav button { background:rgba(255,255,255,.05); color:var(--text); border:1px solid var(--border); padding:8px 18px; border-radius:8px; cursor:pointer; transition:all .2s; font-size:.85rem; }
        .qnav button:hover:not(:disabled) { border-color:var(--accent); color:var(--accent); }
        .qnav button:disabled { opacity:.3; cursor:default; }
        #score-box { display:none; margin-top:16px; padding:20px; background:rgba(0,0,0,.2); border-radius:12px; text-align:center; animation:fadeIn .5s; }

        /* Checklist */
        .cklist { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .cklist label { display:flex; align-items:flex-start; gap:10px; padding:8px 0; color:var(--muted); font-size:.9rem; cursor:pointer; transition:color .2s; }
        .cklist label:hover { color:var(--text); }
        .cklist input[type=checkbox] { margin-top:3px; accent-color:var(--accent); width:18px; height:18px; flex-shrink:0; }
        .cklist .done { color:var(--accent); text-decoration:line-through; opacity:.7; }
        .pbar { background:var(--border); border-radius:8px; height:8px; overflow:hidden; margin-top:16px; }
        .pfill { height:100%; border-radius:8px; background:var(--accent); transition:width .5s ease; width:0; }
        .ptxt { color:var(--dim); font-size:.8rem; margin-top:6px; }

        /* Module nav */
        .mnav { background:var(--card); padding:24px; border-radius:12px; border:1px solid var(--border); }
        .mgrid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:10px; }
        .module-link { display:block; padding:14px; background:var(--bg); border:1px solid var(--border); border-radius:10px; color:var(--muted); text-decoration:none; font-size:.85rem; transition:all .2s; }
        .module-link:hover { border-color:var(--accent); color:var(--accent); transform:translateY(-1px); }
        .module-link.current { border-color:var(--accent); background:var(--accent-glow); }
        .module-link strong { display:block; color:var(--text); margin-bottom:2px; font-size:.9rem; }
        .module-link.current strong { color:var(--accent); }

        footer { margin-top:48px; padding:24px; text-align:center; color:var(--dim); font-size:.8rem; border-top:1px solid var(--border); }
        @media(max-width:600px) { .hero h1{font-size:1.5rem;} .cgrid,.mgrid{grid-template-columns:1fr;} .content{padding:16px;} }
    </style>
</head>
<body>
    <div class="hero">
        <h1>__HERO_TITLE__</h1>
        <p class="sub">__HERO_SUBTITLE__</p>
        <span class="tag">__COURSE_TAG__</span>
    </div>

    <nav class="nav">
        <a href="module.md">Lecture</a>
        <a href="questions.md">Questions</a>
        <a href="practice_quiz.md">Quiz</a>
        <a href="lab.md">Lab</a>
        <a class="active" href="#">Dashboard</a>
    </nav>

    <div class="content">
        <h2 class="stitle">Key Concepts</h2>
        <div class="cgrid">
__CONCEPT_CARDS__
        </div>

        <h2 class="stitle">Self-Assessment Quiz</h2>
        <div class="quiz-box">
            <div class="qprog" id="qprog">Question 1 of __QUIZ_COUNT__</div>
            <div id="qc"></div>
            <div class="qnav">
                <button id="pbtn" onclick="prevQ()" disabled>&larr; Previous</button>
                <button id="nbtn" onclick="nextQ()">Next &rarr;</button>
            </div>
            <div id="score-box"></div>
        </div>

        <h2 class="stitle">Learning Objectives</h2>
        <div class="cklist" id="cklist">
__OBJECTIVE_ITEMS__
            <div class="pbar"><div class="pfill" id="pfill"></div></div>
            <p class="ptxt" id="ptxt">0 of __OBJ_COUNT__ complete</p>
        </div>

        <h2 class="stitle">Module Navigation</h2>
        <div class="mnav">
            <div class="mgrid">
__MODULE_LINKS__
            </div>
        </div>
    </div>

    <footer>Active Inference Institute &mdash; __FOOTER_TEXT__</footer>

    <script>
    /* Concept cards */
    document.querySelectorAll('.concept-card').forEach(function(c){
        c.addEventListener('click',function(){c.classList.toggle('open');});
    });

    /* Quiz engine */
    var Q=__QUIZ_JSON__;
    var ci=0,ans=new Array(Q.length).fill(null),sc=0;

    function renderQ(){
        var q=Q[ci],done=ans[ci]!==null;
        var h='<p class="qq"><strong>Q'+(ci+1)+'.</strong> '+q.q+'</p>';
        q.opts.forEach(function(o,i){
            var c='qbtn';
            if(done){if(i===q.correct)c+=' correct';else if(i===ans[ci])c+=' wrong';}
            h+='<button class="'+c+'" onclick="pickA('+i+')" '+(done?'disabled':'')+'>'+String.fromCharCode(65+i)+') '+o+'</button>';
        });
        if(done){
            var ok=ans[ci]===q.correct;
            h+='<div class="qexp" style="display:block;background:'+(ok?'#166534':'#7f1d1d')+';">'+(ok?'Correct! ':'Incorrect. ')+q.explain+'</div>';
        }
        document.getElementById('qc').innerHTML=h;
        document.getElementById('qprog').textContent='Question '+(ci+1)+' of '+Q.length;
        document.getElementById('pbtn').disabled=ci===0;
        document.getElementById('nbtn').textContent=ci===Q.length-1?'See Score':'Next \u2192';
    }

    function pickA(i){
        if(ans[ci]!==null)return;
        ans[ci]=i;
        if(i===Q[ci].correct)sc++;
        renderQ();
    }

    function nextQ(){
        if(ci<Q.length-1){ci++;renderQ();}
        else{
            var pct=Math.round(sc/Q.length*100);
            var d=document.getElementById('score-box');
            d.style.display='block';
            d.innerHTML='<h3 style="color:'+(pct>=60?'var(--green)':'var(--red)')+'">'+sc+'/'+Q.length+' ('+pct+'%)</h3><p style="color:var(--muted);margin-top:8px">'+(pct>=80?'Excellent understanding of the material!':pct>=60?'Good foundation. Review the concepts you missed.':'Consider re-reading the module before moving on.')+'</p>';
        }
    }

    function prevQ(){if(ci>0){ci--;renderQ();}}

    /* Checklist with localStorage */
    var SK='__STORAGE_KEY__';
    var QK=SK+'_quiz';
    function initCL(){
        var saved=JSON.parse(localStorage.getItem(SK)||'[]');
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        boxes.forEach(function(cb,i){
            if(saved[i])cb.checked=true;
            if(cb.checked)cb.parentElement.classList.add('done');
            cb.addEventListener('change',function(){
                cb.parentElement.classList.toggle('done',cb.checked);
                saveCL();updProg();
            });
        });
        updProg();
    }
    function saveCL(){
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        localStorage.setItem(SK,JSON.stringify(Array.from(boxes).map(function(c){return c.checked;})));
    }
    function updProg(){
        var boxes=document.querySelectorAll('#cklist input[type=checkbox]');
        var n=boxes.length,done=Array.from(boxes).filter(function(c){return c.checked;}).length;
        document.getElementById('pfill').style.width=(n?done/n*100:0)+'%';
        document.getElementById('ptxt').textContent=done+' of '+n+' complete';
    }

    /* Quiz persistence */
    function saveQuiz(){
        localStorage.setItem(QK,JSON.stringify({ci:ci,ans:ans,sc:sc}));
    }
    function loadQuiz(){
        try{
            var d=JSON.parse(localStorage.getItem(QK));
            if(d&&d.ans&&d.ans.length===Q.length){
                ci=d.ci||0;ans=d.ans;sc=d.sc||0;
            }
        }catch(e){}
    }
    /* Patch pickA to persist */
    var _origPickA=pickA;
    pickA=function(i){_origPickA(i);saveQuiz();};

    /* Init */
    document.addEventListener('DOMContentLoaded',function(){
        document.querySelectorAll('.meter-fill').forEach(function(f){
            var w=f.style.width;f.style.width='0%';
            setTimeout(function(){f.style.width=w;},200);
        });
        loadQuiz();
        renderQ();
        initCL();
    });
    </script>
</body>
</html>"""


GENERIC_WRONG = [
    "A purely theoretical construct with no practical application in this field.",
    "An outdated concept that has been replaced by newer research.",
    "A term borrowed from an unrelated discipline with a different meaning here.",
    "A secondary detail not covered in this module.",
    "The mathematical inverse of the primary concept discussed.",
]


def get_theme(course_id: str) -> Dict[str, str]:
    if course_id.startswith("ai-"):
        return THEMES.get(course_id, THEMES["ai-philosophy"])
    return DEFAULT_THEME


def parse_module_md(module_dir: Path) -> Dict[str, Any]:
    path = module_dir / "module.md"
    if not path.exists():
        return {"title": "", "subtitle": "", "overview": "",
                "objectives": [], "key_concepts": [], "core_sections": [], "summary": ""}
    text = path.read_text(encoding="utf-8")
    data = {"title": "", "subtitle": "", "overview": "",
            "objectives": [], "key_concepts": [], "core_sections": [], "summary": ""}

    lines = text.split("\n")

    # Title (first H1)
    for ln in lines:
        if ln.startswith("# "):
            data["title"] = ln[2:].strip()
            break

    # Subtitle (first H2 that isn't a known section header)
    skip_kw = {"overview", "introduction", "learning", "key ", "core", "lesson",
               "summary", "reference", "further", "example", "contents", "activity"}
    found_title = False
    for ln in lines:
        if ln.startswith("# "):
            found_title = True
            continue
        if found_title and ln.startswith("## "):
            heading = ln[3:].strip().lower()
            if not any(kw in heading for kw in skip_kw):
                data["subtitle"] = ln[3:].strip()
                break

    # Split into sections
    sections: Dict[str, str] = {}
    cur_key = ""
    cur_lines: List[str] = []
    for ln in lines:
        if ln.startswith("## "):
            if cur_key:
                sections[cur_key] = "\n".join(cur_lines).strip()
            cur_key = ln[3:].strip().lower()
            cur_lines = []
        else:
            cur_lines.append(ln)
    if cur_key:
        sections[cur_key] = "\n".join(cur_lines).strip()

    # Overview / introduction
    for k in ("overview", "introduction"):
        if k in sections:
            data["overview"] = sections[k]
            break

    # Learning objectives / goals
    for k in sections:
        if "learning" in k and ("objective" in k or "goal" in k):
            for m in re.finditer(r"^\d+\.\s*(.+)$", sections[k], re.MULTILINE):
                obj = re.sub(r"\*\*([^*]+)\*\*", r"\1", m.group(1).strip())
                data["objectives"].append(obj)
            break

    # Key concepts / vocabulary
    for k in sections:
        if "key" in k and ("concept" in k or "vocab" in k or "term" in k):
            concept_text = sections[k]
            # Try full pattern: - **name** — definition (separator on same line)
            for m in re.finditer(
                r"-\s*\*\*([^*]+)\*\*[ \t]*[-\u2014:][ \t]+(.+?)(?=\n-|\n\n|\Z)",
                concept_text, re.DOTALL,
            ):
                name = m.group(1).strip()
                defn = m.group(2).strip().replace("\n", " ")
                defn = re.sub(r"\*\*([^*]+)\*\*", r"\1", defn)
                data["key_concepts"].append((name, defn))
            # Fallback: bare terms - **name** (no definition)
            if not data["key_concepts"]:
                for m in re.finditer(r"-\s*\*\*([^*]+)\*\*", concept_text):
                    name = m.group(1).strip()
                    data["key_concepts"].append(
                        (name, f"A key concept in {data['title'] or 'this module'}.")
                    )
            break

    # Core concept subsections (for expanded card detail)
    for k in sections:
        if any(kw in k for kw in ("core concept", "lesson content")):
            for sub in re.split(r"^###\s+", sections[k], flags=re.MULTILINE)[1:]:
                parts = sub.strip().split("\n", 1)
                heading = parts[0].strip()
                body = parts[1].strip() if len(parts) > 1 else ""
                body = re.sub(r"\*\*([^*]+)\*\*", r"\1", body)
                body = re.sub(r"\*([^*]+)\*", r"\1", body)
                data["core_sections"].append((heading, body[:300]))
            break

    # Summary
    if "summary" in sections:
        data["summary"] = sections["summary"]

    return data


def parse_practice_quiz(module_dir: Path) -> List[Dict[str, Any]]:
    path = module_dir / "practice_quiz.md"
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8")

    # Answer key — supports both bare "1. A" and bold markdown "1. **A** -- explanation"
    answer_key: Dict[int, int] = {}
    answer_explanations: Dict[int, str] = {}
    key_match = re.search(r"Answer\s*Key([\s\S]*?)$", text, re.IGNORECASE)
    if key_match:
        key_text = key_match.group(1)
        # Pattern 1: "1. **A** -- explanation" (bold letter with separator)
        for m in re.finditer(
            r"(\d+)\.\s*\*\*([A-D])\*\*\s*[-—:]+\s*(.+)",
            key_text,
        ):
            q_num = int(m.group(1))
            answer_key[q_num] = ord(m.group(2).upper()) - ord("A")
            answer_explanations[q_num] = m.group(3).strip()
        # Pattern 2: bare "1. A" (no bold, no explanation)
        if not answer_key:
            for m in re.finditer(r"(\d+)\.\s*([A-D])\b", key_text):
                q_num = int(m.group(1))
                if q_num not in answer_key:
                    answer_key[q_num] = ord(m.group(2).upper()) - ord("A")

    # Isolate Part A
    part_a = text
    pa = re.search(r"Part\s*A[:\s]*(?:Multiple\s*Choice)?([\s\S]*?)(?:Part\s*B|\Z)", text, re.I)
    if pa:
        part_a = pa.group(1)

    # Split on question numbers
    blocks = re.split(r"(?:^|\n)\s*(?:\*\*|###\s*)(\d+)\.", part_a)
    questions: List[Dict[str, Any]] = []
    for i in range(1, len(blocks) - 1, 2):
        q_num = int(blocks[i])
        q_text_block = blocks[i + 1].strip()
        q_lines = q_text_block.split("\n")
        question = q_lines[0].strip().rstrip("*").strip()

        options: List[str] = []
        for ln in q_lines[1:]:
            om = re.match(r"^\s*-?\s*([A-D])\)\s*(.+)", ln.strip())
            if om:
                options.append(om.group(2).strip().rstrip("."))

        if options and question:
            correct = answer_key.get(q_num, -1)
            if correct < 0 or correct >= len(options):
                # Answer key missing for this question — skip it rather
                # than defaulting to 0 (which produces always-A bugs)
                continue
            # Build explanation: prefer parsed explanation, then option text
            explain = answer_explanations.get(q_num, "")
            if not explain:
                explain = f"{chr(65 + correct)}) {options[correct]}"
            questions.append({
                "q": question,
                "opts": options,
                "correct": correct,
                "explain": explain,
            })
    return questions


def is_stub_quiz(questions: List[Dict[str, Any]]) -> bool:
    if not questions:
        return True
    stub_pats = [r"a core concept", r"an unrelated idea", r"a synonym for",
                 r"none of the above", r"recite the textbook", r"ignore the topic",
                 r"only study for the final"]
    stub_count = sum(
        1 for q in questions
        if any(re.search(p, " ".join(q.get("opts", [])).lower()) for p in stub_pats)
    )
    return stub_count > len(questions) / 2


def _shuffle_with_correct(opts: List[str], correct_idx: int, rng: random.Random) -> Tuple[List[str], int]:
    """Shuffle options and return (shuffled_opts, new_correct_index)."""
    indices = list(range(len(opts)))
    rng.shuffle(indices)
    shuffled = [opts[j] for j in indices]
    new_correct = indices.index(correct_idx)
    return shuffled, new_correct


def generate_quiz_from_module(module_data: Dict[str, Any], seed_text: str = "") -> List[Dict[str, Any]]:
    concepts = module_data.get("key_concepts", [])
    objectives = module_data.get("objectives", [])
    # Use module-specific seed so different modules get different shuffles
    rng = random.Random(hash(seed_text) if seed_text else 42)
    questions: List[Dict[str, Any]] = []

    for i, (name, definition) in enumerate(concepts):
        opts = [definition]
        for j, (_, other_def) in enumerate(concepts):
            if j != i and len(opts) < 4:
                opts.append(other_def)
        gi = 0
        while len(opts) < 4:
            opts.append(GENERIC_WRONG[gi % len(GENERIC_WRONG)])
            gi += 1
        shuffled, correct = _shuffle_with_correct(opts, 0, rng)
        questions.append({
            "q": f'Which of the following best describes "{name}"?',
            "opts": shuffled,
            "correct": correct,
            "explain": f"{name}: {definition}",
        })

    if objectives:
        obj = objectives[0]
        opts = [obj,
                "Memorize all definitions without applying them to real situations.",
                "Skip foundational concepts and focus only on advanced material.",
                "Review content from a completely different subject area."]
        shuffled, correct = _shuffle_with_correct(opts, 0, rng)
        questions.append({
            "q": "A primary learning goal of this module is to:",
            "opts": shuffled,
            "correct": correct,
            "explain": f"This module focuses on: {obj}",
        })

    if len(objectives) > 1:
        obj = objectives[-1]
        opts = [obj,
                "Complete unrelated worksheets for extra credit.",
                "Watch videos without taking notes or reflecting.",
                "Repeat previous module content without new application."]
        shuffled, correct = _shuffle_with_correct(opts, 0, rng)
        questions.append({
            "q": "By the end of this module you should also be able to:",
            "opts": shuffled,
            "correct": correct,
            "explain": f"Another key goal: {obj}",
        })

    return questions[:7]


def get_sibling_modules(module_dir: Path) -> List[Dict[str, Any]]:
    unit_dir = module_dir.parent
    siblings: List[Dict[str, Any]] = []
    for child in sorted(unit_dir.iterdir()):
        if not child.is_dir() or not (child / "module.md").exists():
            continue
        title = ""
        try:
            for ln in (child / "module.md").read_text(encoding="utf-8").split("\n"):
                if ln.startswith("# "):
                    title = ln[2:].strip()
                    break
        except Exception:
            pass
        mod_name = child.name
        topic = prettify_name(mod_name)
        siblings.append({
            "dir": mod_name,
            "topic": topic,
            "title": title or topic,
            "is_current": child == module_dir,
        })
    return siblings


def build_concept_cards(concepts: List[Tuple], core_sections: List[Tuple],
                        overview: str = "") -> str:
    if not concepts:
        return '<p style="color:#94a3b8">No key concepts defined for this module.</p>'
    cards: List[str] = []
    for i, (name, definition) in enumerate(concepts):
        relevance = max(55, 95 - i * 10)
        detail = ""
        # Try matching core section headings
        for heading, body in core_sections:
            if name.lower().split()[0] in heading.lower():
                detail = f"<p>{escape(body[:250])}</p>"
                break
        # Fallback: extract a relevant sentence from overview text
        if not detail and overview:
            first_word = name.lower().split()[0]
            for sentence in re.split(r'(?<=[.!?])\s+', overview):
                if first_word in sentence.lower():
                    clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', sentence)
                    clean = re.sub(r'\*([^*]+)\*', r'\1', clean)
                    detail = f"<p>{escape(clean[:250])}</p>"
                    break
        # Final fallback: use a contextual note instead of duplicating brief
        if not detail:
            detail = (f"<p>Explore how {escape(name)} connects to the other "
                      f"concepts in this module through the lecture and lab materials.</p>")
        cards.append(
            f'<div class="concept-card">'
            f'<h3>{escape(name)} <span class="toggle">+</span></h3>'
            f'<p class="brief">{escape(definition)}</p>'
            f'<div class="detail">{detail}</div>'
            f'<div class="meter"><div class="meter-fill" style="width:{relevance}%"></div></div>'
            f'<p class="meter-label">Centrality to module</p>'
            f'</div>'
        )
    return "\n".join(cards)


def build_checklist(objectives: List[str]) -> str:
    if not objectives:
        return '<label><input type="checkbox"> Complete this module</label>'
    return "\n".join(
        f'<label><input type="checkbox"> {escape(obj)}</label>'
        for obj in objectives
    )


def build_module_nav(siblings: List[Dict[str, Any]]) -> str:
    links: List[str] = []
    for sib in siblings:
        cls = "module-link current" if sib["is_current"] else "module-link"
        href = "#" if sib["is_current"] else f"../{sib['dir']}/dashboard.html"
        links.append(
            f'<a class="{cls}" href="{href}">'
            f'<strong>Module {sib["dir"][:2]}: {escape(sib["topic"])}</strong>'
            f'{escape(sib["title"][:60])}</a>'
        )
    return "\n".join(links)


def generate_dashboard_html(module_dir: Path, base: Path) -> str:
    md = parse_module_md(module_dir)
    quiz = parse_practice_quiz(module_dir)
    if is_stub_quiz(quiz):
        quiz = generate_quiz_from_module(md, seed_text=str(module_dir))
    if not quiz:
        quiz = [{"q": "Quiz coming soon!", "opts": ["Check back later"],
                 "correct": 0, "explain": ""}]

    # Standardized course info extraction
    course_info = extract_course_info(module_dir / "module.md", base)
    
    theme = get_theme(course_info["course"])
    siblings = get_sibling_modules(module_dir)
    
    course_name = course_info["course_name"]
    unit = course_info["unit"]
    mod_name = module_dir.name
    mod_num = course_info["module_num"]
    topic = course_info["module_topic"]

    hero_title = md.get("title") or f"Module {mod_num}: {topic}"
    hero_subtitle = md.get("subtitle") or f"{unit} \u2014 {course_name}"
    if not md.get("subtitle"):
        hero_subtitle = f"{unit} \u2014 {course_name}"
    page_title = f"Dashboard: {topic} \u2014 {unit}"
    course_tag = f"{course_name} \u2014 {unit}"
    footer_text = f"{course_name} \u2014 {unit} \u2014 Module {mod_num}: {topic}"
    
    # Storage key using registry course ID
    storage_key = f"ai_{course_info['course']}_{unit.lower().replace(' ', '_')}_{mod_name}"

    cards_html = build_concept_cards(md.get("key_concepts", []), md.get("core_sections", []),
                                     md.get("overview", ""))
    check_html = build_checklist(md.get("objectives", []))
    nav_html = build_module_nav(siblings)
    obj_count = len(md.get("objectives", [])) or 1

    html = TEMPLATE
    replacements = {
        "__PAGE_TITLE__": escape(page_title),
        "__ACCENT__": theme["accent"],
        "__GRADIENT__": theme["gradient"],
        "__HERO_TITLE__": escape(hero_title),
        "__HERO_SUBTITLE__": escape(hero_subtitle),
        "__COURSE_TAG__": escape(course_tag),
        "__CONCEPT_CARDS__": cards_html,
        "__QUIZ_COUNT__": str(len(quiz)),
        "__QUIZ_JSON__": json.dumps(quiz, ensure_ascii=False),
        "__OBJECTIVE_ITEMS__": check_html,
        "__OBJ_COUNT__": str(obj_count),
        "__MODULE_LINKS__": nav_html,
        "__FOOTER_TEXT__": escape(footer_text),
        "__STORAGE_KEY__": storage_key,
    }
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html
