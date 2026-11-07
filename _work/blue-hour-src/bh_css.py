import json
from pathlib import Path

LIB = Path(r"c:/Users/Tan Shi Bin/My Drive/DATA LIBRARY/CUSTOM SITE BUILDER/Design Library/library")

# effects whose CSS is reused verbatim (class names are unscoped inside them)
REUSE = [("scroll", "scroll-scene-stack"), ("images", "img-scroll-zoom-pin"), ("images", "img-clip-reveal"), ("scroll", "scroll-zoom-tunnel"),
         ("scroll", "scroll-number-morph"), ("scroll", "scroll-path-draw"), ("scroll", "scroll-velocity-skew"), ("cursor", "cursor-image-follow"),
         ("images", "img-rgb-split"), ("images", "img-strip-slices"), ("images", "img-mask-text"), ("text", "text-scramble"), ("buttons", "button-pointer-fill"),
         ("images", "img-liquid-distort"), ("text", "text-split-lines")]


def effect_css():
    out = []
    for cat, slug in REUSE:
        d = json.loads((LIB / "effects" / cat / slug / "effect.json").read_text(encoding="utf8"))
        out.append(f"/* ── {slug} ── */\n" + d["css"])
    return "\n".join(out)


CSS = r'''
/* Blue Hour — photo expeditions after dark. Night-violet ground, first-light gold, twilight lavender. Tokens only. */
:root{
--primary:var(--c-primary);--secondary:var(--c-secondary);--text:var(--c-text);--accent:var(--c-accent);--surface:var(--c-surface);--border:var(--c-border);
--font-heading:var(--f-head);--font-body:var(--f-body);--speed:1;
--bh-dusk:color-mix(in srgb,var(--c-surface) 84%,var(--c-secondary));
--bh-deep:color-mix(in srgb,var(--c-surface) 78%,#000);
--bh-card:color-mix(in srgb,var(--c-surface) 90%,var(--c-secondary));
--bh-ink2:color-mix(in srgb,var(--c-text) 74%,var(--c-surface));
--bh-ink3:color-mix(in srgb,var(--c-text) 56%,var(--c-surface));
--bh-rad:var(--radius);
}
body{background:var(--c-surface);color:var(--c-text);font-family:var(--f-body)}
.bh-in{max-width:var(--w,1280px);margin:0 auto;padding:0 clamp(18px,4vw,48px)}
.bh-sec{padding:var(--pad) 0}.bh-dusk{background:var(--bh-dusk)}.bh-deep{background:var(--bh-deep)}
:focus-visible{outline:3px solid var(--c-accent);outline-offset:3px}
.bh-sr{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.bh-k{display:block;font:700 12px/1.2 var(--f-head);letter-spacing:.26em;text-transform:uppercase;color:var(--c-accent);margin-bottom:18px}
.bh-h{font-size:clamp(2.1rem,5.4vw,4rem);line-height:1.02;letter-spacing:-.015em;font-weight:700}
.bh-h em{font-style:normal;color:var(--c-accent)}
.bh-lead{font:400 clamp(1.05rem,1.7vw,1.32rem)/1.6 var(--f-body);color:var(--bh-ink2);max-width:34em;margin:0}
.bh-p{color:var(--bh-ink2);max-width:36em}
.bh-actions{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.bh-link{display:inline-flex;align-items:center;gap:.6em;min-height:44px;font:700 13px/1 var(--f-head);letter-spacing:.18em;text-transform:uppercase;color:var(--c-primary);text-decoration:none;border-bottom:1.5px solid var(--c-accent);padding-bottom:4px}
.bh-link:hover{color:var(--c-accent)}
.bh-i{width:1.15em;height:1.15em;flex:none;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;vertical-align:-.2em}
.bh-chip{display:inline-flex;align-items:center;min-height:44px;padding:0 18px;border:1.5px solid var(--c-border);border-radius:99px;background:transparent;color:var(--bh-ink2);font:700 12px/1 var(--f-head);letter-spacing:.14em;text-transform:uppercase;cursor:pointer;transition:background .25s,color .25s,border-color .25s}
.bh-chip:hover{border-color:var(--c-primary);color:var(--c-primary)}
.bh-chip[aria-pressed=true]{background:var(--c-primary);color:var(--on-primary);border-color:var(--c-primary)}
.bh-chips{display:flex;gap:10px;flex-wrap:wrap}
.bh-tag{display:inline-flex;align-items:center;padding:.35em .9em;border:1px solid var(--c-border);border-radius:99px;font:600 12px/1 var(--f-head);letter-spacing:.1em;text-transform:uppercase;color:var(--bh-ink2)}
.bh-seat{color:var(--c-accent);border-color:color-mix(in srgb,var(--c-accent) 50%,transparent)}
.bh-art{border-radius:var(--bh-rad)}
.ap-art{position:relative;overflow:hidden}.ap-art svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.bh-card{background:var(--bh-card);border:1px solid var(--c-border);border-radius:var(--bh-rad)}

/* ── header ── */
.bh-top{position:sticky;top:0;z-index:60;transition:background .3s,backdrop-filter .3s,border-color .3s;border-bottom:1px solid transparent}
.bh-top.is-s{background:color-mix(in srgb,var(--c-surface) 86%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-color:var(--c-border)}
.bh-bar{display:flex;align-items:center;gap:22px;min-height:72px}
.bh-brand{display:inline-flex;align-items:center;gap:12px;text-decoration:none;color:var(--c-primary);font:700 20px/1 var(--f-head);letter-spacing:.2em;text-transform:uppercase;min-height:44px}
.bh-brand svg{width:34px;height:34px;color:var(--c-accent)}.bh-brand b{color:var(--c-accent);font-weight:700}
.bh-nav{display:flex;gap:4px;margin-left:auto}
.bh-nav a{display:inline-flex;align-items:center;min-height:44px;padding:0 16px;color:var(--bh-ink2);text-decoration:none;font:700 12px/1 var(--f-head);letter-spacing:.2em;text-transform:uppercase;position:relative}
.bh-nav a::after{content:"";position:absolute;left:16px;right:16px;bottom:8px;height:2px;background:var(--c-accent);transform:scaleX(0);transform-origin:left;transition:transform .35s cubic-bezier(.2,.8,.2,1)}
.bh-nav a:hover,.bh-nav a.on{color:var(--c-primary)}.bh-nav a:hover::after,.bh-nav a.on::after{transform:scaleX(1)}
.bh-burger{display:none;margin-left:auto;width:48px;height:48px;border:1.5px solid var(--c-border);border-radius:50%;background:transparent;color:var(--c-primary);cursor:pointer}
.bh-burger i{display:block;width:18px;height:2px;margin:5px auto;background:currentColor;transition:transform .3s,opacity .3s}
.bh-burger[aria-expanded=true] i:nth-child(1){transform:translateY(7px) rotate(45deg)}.bh-burger[aria-expanded=true] i:nth-child(2){opacity:0}.bh-burger[aria-expanded=true] i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.bh-prog{position:absolute;left:0;bottom:-1px;height:2px;width:100%;pointer-events:none}.bh-prog i{display:block;height:100%;width:calc(var(--bp,0)*100%);background:var(--c-accent)}

/* ── footer ── */
.bh-foot{background:var(--bh-deep);border-top:1px solid var(--c-border);padding:clamp(56px,8vw,96px) 0 28px;overflow:hidden}
.bh-foot .big{font:700 clamp(3rem,15vw,11rem)/.9 var(--f-head);letter-spacing:-.03em;text-transform:uppercase;color:transparent;-webkit-text-stroke:1.5px color-mix(in srgb,var(--c-primary) 28%,transparent);margin:0 0 clamp(32px,5vw,64px);white-space:nowrap}
.bh-foot .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.4fr;gap:clamp(24px,4vw,56px)}
.bh-foot h4{font:700 12px/1 var(--f-head);letter-spacing:.24em;text-transform:uppercase;color:var(--c-accent);margin-bottom:16px}
.bh-foot a{display:flex;align-items:center;min-height:36px;color:var(--bh-ink2);text-decoration:none;font-size:15px}.bh-foot a:hover{color:var(--c-primary)}
.bh-foot p{color:var(--bh-ink3);font-size:15px;max-width:26em}
.bh-foot form{display:flex;gap:8px;margin-top:14px}
.bh-foot input{flex:1;min-width:0;min-height:48px;padding:0 16px;border-radius:99px;border:1.5px solid var(--c-border);background:transparent;color:var(--c-text);font:inherit}
.bh-foot .base{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:clamp(32px,5vw,56px);padding-top:20px;border-top:1px solid var(--c-border);font-size:13px;color:var(--bh-ink3)}

/* ── hero ── */
.bh-hero{position:relative;min-height:min(100svh,900px);display:grid;align-content:end;padding:clamp(110px,14svh,150px) 0 clamp(28px,5svh,56px);overflow:hidden;margin-top:-72px}
.bh-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(60% 50% at 82% 8%,color-mix(in srgb,var(--c-secondary) 38%,transparent),transparent 70%),radial-gradient(50% 40% at 10% 100%,color-mix(in srgb,var(--c-accent) 16%,transparent),transparent 70%);pointer-events:none}
.bh-stars{position:absolute;inset:0;opacity:.7;background-image:radial-gradient(1.2px 1.2px at 8% 22%,#fff 50%,transparent),radial-gradient(1px 1px at 19% 61%,#fff 50%,transparent),radial-gradient(1.6px 1.6px at 31% 14%,#fff 50%,transparent),radial-gradient(1px 1px at 44% 48%,#fff 50%,transparent),radial-gradient(1.4px 1.4px at 57% 26%,#fff 50%,transparent),radial-gradient(1px 1px at 66% 70%,#fff 50%,transparent),radial-gradient(1.6px 1.6px at 78% 12%,#fff 50%,transparent),radial-gradient(1px 1px at 88% 52%,#fff 50%,transparent),radial-gradient(1.2px 1.2px at 93% 30%,#fff 50%,transparent),radial-gradient(1px 1px at 72% 40%,#fff 50%,transparent),radial-gradient(1.2px 1.2px at 24% 80%,#fff 50%,transparent),radial-gradient(1px 1px at 50% 8%,#fff 50%,transparent)}
.bh-hero .bh-in{position:relative}
.mt{--mp:.5}
.bh-hero .mt-t{font-size:clamp(4rem,17.5vw,12.5rem);font-weight:700;line-height:.84;letter-spacing:-.025em;margin:0 0 clamp(18px,3vw,36px)}
.bh-hero .mt-t span,.bh-art-hero .mt-t span{display:block;width:fit-content;padding:.07em .04em .03em;margin:-.03em 0}
@supports ((-webkit-background-clip:text) or (background-clip:text)){
.bh-hero .mt-a{background-image:linear-gradient(to bottom,var(--c-secondary) 0,color-mix(in srgb,var(--c-secondary) 55%,var(--c-accent)) 34%,var(--c-accent) 60%,color-mix(in srgb,var(--c-accent) 45%,var(--c-surface)) 100%);background-size:100% 230%;background-position:50% calc(var(--mp)*100%)}
.bh-hero .mt-b{background-image:conic-gradient(from calc(var(--mp)*300deg) at 50% 60%,var(--c-accent),var(--c-secondary),var(--c-primary),var(--c-secondary),var(--c-accent))}}
.bh-herorow{display:flex;justify-content:space-between;align-items:end;gap:clamp(20px,4vw,56px);flex-wrap:wrap}
.bh-cue{display:inline-flex;align-items:center;gap:12px;margin-top:clamp(28px,5vw,48px);font:700 11px/1 var(--f-head);letter-spacing:.3em;text-transform:uppercase;color:var(--bh-ink3)}
.bh-cue::after{content:"";width:56px;height:1px;background:currentColor;transform-origin:left;animation:bhcue 2.4s ease-in-out infinite}
@keyframes bhcue{0%,100%{transform:scaleX(.3)}50%{transform:scaleX(1)}}

/* ── sections ── */
.bh-state{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(24px,6vw,96px);align-items:start}
.bh-state .st{font:600 clamp(1.5rem,3.4vw,2.6rem)/1.22 var(--f-head);letter-spacing:-.01em;color:var(--c-primary)}
.bh-state .st em{font-style:normal;color:var(--c-accent)}
.bh-mini{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,3vw,32px);margin-top:clamp(28px,4vw,48px);padding-top:28px;border-top:1px solid var(--c-border)}
.bh-mini b{display:block;font:700 clamp(1.8rem,3.6vw,2.8rem)/1 var(--f-head);color:var(--c-accent);margin-bottom:8px}.bh-mini span{font-size:14px;color:var(--bh-ink2)}
.bh-head{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-bottom:clamp(28px,5vw,56px)}
.bh-ss .ss-t .bh-link{pointer-events:auto;margin-top:12px}
.bh-fr{display:grid;gap:clamp(48px,9vw,110px)}
.bh-fr .row{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(24px,5vw,72px);align-items:center}
.bh-fr .row.rev{grid-template-columns:minmax(0,1fr) minmax(0,1.1fr)}.bh-fr .row.rev .cr-fig{order:2}
.bh-fr .no{font:700 12px/1 var(--f-head);letter-spacing:.24em;color:var(--c-accent)}
.bh-fr h3{font-size:clamp(1.6rem,3.2vw,2.4rem);margin:10px 0 12px}.bh-fr p{color:var(--bh-ink2);max-width:26em}
.bh-exif{display:flex;gap:8px;flex-wrap:wrap;margin-top:16px}
.bh-dep .cf-list{border-color:var(--c-border)}
.bh-dep .cf-row{grid-template-columns:3em minmax(0,1fr) minmax(0,.7fr) auto}
.bh-dep .cf-row .y{white-space:nowrap}
.bh-dep .cf-row[hidden]{display:none}.bh-dep li[hidden]{display:none}
.bh-j{display:grid;gap:clamp(20px,4vw,40px)}
.bh-jcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,3vw,32px)}
.bh-jc{display:grid;gap:12px;color:inherit;text-decoration:none}
.bh-jc .ap-art,.bh-jc .rs{aspect-ratio:4/5;border-radius:var(--bh-rad);border:1px solid var(--c-border)}
.bh-jc small{font:700 11px/1 var(--f-head);letter-spacing:.22em;text-transform:uppercase;color:var(--c-accent)}
.bh-jc h3{font-size:clamp(1.2rem,2.2vw,1.6rem);line-height:1.15}.bh-jc p{color:var(--bh-ink3);font-size:14px}
.bh-jc:hover h3{color:var(--c-accent)}
.bh-cta{text-align:center;padding:clamp(72px,12vw,150px) 0;position:relative;overflow:hidden}
.bh-cta::before{content:"";position:absolute;left:50%;bottom:-40%;width:120%;aspect-ratio:1;transform:translateX(-50%);background:radial-gradient(circle,color-mix(in srgb,var(--c-accent) 30%,transparent),transparent 62%);pointer-events:none}
.bh-cta .bh-in{position:relative}
.bh-cta h2{font-size:clamp(2.4rem,8vw,6.4rem);line-height:.96;text-transform:uppercase;letter-spacing:-.02em;margin:0 auto 28px;max-width:11em}
.bh-cta .bh-lead{margin:0 auto 32px}.bh-cta .bh-actions{justify-content:center}

/* ── page heads ── */
.bh-ph{padding:clamp(56px,9vw,110px) 0 clamp(32px,5vw,64px)}
.bh-ph h1{font-size:clamp(2.6rem,8vw,6.2rem);line-height:.94;letter-spacing:-.02em;text-transform:uppercase;margin:0 0 20px}
.bh-ph .row{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:clamp(24px,6vw,80px);align-items:end}
.bh-ph .sp{aspect-ratio:4/5;max-height:62svh;width:100%}
.bh-facts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:1px solid var(--c-border);border-radius:var(--bh-rad);background:var(--bh-card)}
.bh-facts div{padding:clamp(16px,2.4vw,28px);border-right:1px solid var(--c-border)}.bh-facts div:last-child{border:0}
.bh-facts b{display:block;font:700 clamp(1.8rem,3.6vw,2.8rem)/1 var(--f-head);color:var(--c-primary);margin-bottom:6px}.bh-facts span{font-size:13px;letter-spacing:.08em;color:var(--bh-ink2);text-transform:uppercase}
.bh-two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(20px,4vw,48px)}
.bh-list{list-style:none;margin:16px 0 0;padding:0;display:grid;gap:12px}
.bh-list li{display:grid;grid-template-columns:1.4em 1fr;gap:10px;color:var(--bh-ink2)}.bh-list li::before{content:"";width:8px;height:8px;margin-top:.55em;border-radius:50%;background:var(--c-accent)}
.bh-no li::before{background:transparent;border:1.5px solid var(--bh-ink3)}
.bh-faq{display:grid;gap:0;border-top:1px solid var(--c-border)}
.bh-faq details{border-bottom:1px solid var(--c-border)}
.bh-faq summary{display:flex;justify-content:space-between;align-items:center;gap:20px;min-height:64px;cursor:pointer;list-style:none;font:600 clamp(1.05rem,1.8vw,1.3rem)/1.3 var(--f-head);color:var(--c-primary)}
.bh-faq summary::-webkit-details-marker{display:none}.bh-faq summary::after{content:"+";font-size:1.6em;line-height:1;color:var(--c-accent);transition:transform .3s}
.bh-faq details[open] summary::after{transform:rotate(45deg)}.bh-faq details p{padding:0 0 22px;color:var(--bh-ink2);max-width:46em}
.bh-reserve{position:sticky;top:96px;padding:clamp(20px,3vw,32px);display:grid;gap:14px}
.bh-reserve .pr{font:700 clamp(2rem,4vw,3rem)/1 var(--f-head);color:var(--c-primary)}.bh-reserve .pr small{font-size:.4em;color:var(--bh-ink3);letter-spacing:.1em;text-transform:uppercase;margin-left:6px}
.bh-reserve dl{display:grid;gap:8px;margin:0}.bh-reserve dl div{display:flex;justify-content:space-between;gap:12px;font-size:14px;border-bottom:1px dashed var(--c-border);padding-bottom:8px}.bh-reserve dt{color:var(--bh-ink3)}.bh-reserve dd{margin:0;color:var(--c-primary);font-weight:600}
.bh-lay{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:clamp(28px,5vw,72px);align-items:start}

/* ── article ── */
.bh-art-hero{padding:clamp(72px,12vw,150px) 0 clamp(28px,4vw,48px)}
.bh-art-hero .mt-t{font-size:clamp(3.2rem,15vw,11rem);font-weight:700;line-height:.86;letter-spacing:-.025em;text-transform:uppercase;margin:0 0 24px}
@supports ((-webkit-background-clip:text) or (background-clip:text)){
.bh-art-hero .mt-a{background-image:linear-gradient(to bottom,var(--c-secondary) 0,color-mix(in srgb,var(--c-secondary) 60%,var(--c-primary)) 40%,var(--c-accent) 62%,var(--c-surface) 100%);background-size:100% 220%;background-position:50% calc(var(--mp)*100%)}
.bh-art-hero .mt-b{background-image:linear-gradient(to bottom,var(--c-accent) 0,color-mix(in srgb,var(--c-accent) 55%,var(--c-secondary)) 45%,var(--c-secondary) 100%);background-size:100% 220%;background-position:50% calc(var(--mp)*100%)}}
.bh-meta{display:flex;gap:10px 24px;flex-wrap:wrap;font:600 12px/1 var(--f-head);letter-spacing:.2em;text-transform:uppercase;color:var(--bh-ink3)}.bh-meta b{color:var(--c-accent);font-weight:700}
.bh-prose{max-width:42em;margin:0 auto;font:400 clamp(1.08rem,1.5vw,1.22rem)/1.78 var(--f-body)}
.bh-prose p{margin:0 0 1.4em;max-width:none;color:var(--bh-ink2)}.bh-prose p.dc::first-letter{font:700 4.2em/.8 var(--f-head);float:left;margin:.08em .12em 0 0;color:var(--c-accent)}
.bh-prose h2{font-size:clamp(1.6rem,3.2vw,2.3rem);margin:1.8em 0 .6em;text-transform:none}
.bh-prose blockquote{margin:2em 0;padding:0 0 0 1.2em;border-left:3px solid var(--c-accent);font:600 clamp(1.4rem,3vw,2.1rem)/1.25 var(--f-head);color:var(--c-primary)}
.bh-wide{max-width:var(--w,1280px);margin:clamp(40px,6vw,72px) auto;padding:0 clamp(18px,4vw,48px)}
.bh-wide .cr-fig{aspect-ratio:16/9;max-width:100%}.bh-wide .cr-fig .ap-art{height:100%}
.bh-cap{font-size:13px;letter-spacing:.06em;color:var(--bh-ink3);margin-top:12px}
.bh-tbl{width:100%;border-collapse:collapse;margin:1.6em 0;font-size:15px}
.bh-tbl th,.bh-tbl td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--c-border)}.bh-tbl th{font:700 11px/1 var(--f-head);letter-spacing:.2em;text-transform:uppercase;color:var(--c-accent)}.bh-tbl td{color:var(--bh-ink2)}
.bh-next{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px}

/* ── prints ── */
.bh-pick{display:flex;gap:clamp(16px,3vw,40px);flex-wrap:wrap;align-items:end;margin-bottom:clamp(24px,4vw,48px)}
.bh-pick fieldset{border:0;padding:0;margin:0}.bh-pick legend{font:700 11px/1 var(--f-head);letter-spacing:.24em;text-transform:uppercase;color:var(--bh-ink3);margin-bottom:12px}
.bh-pgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(18px,3vw,36px)}
.bh-pr{display:grid;gap:12px}
.bh-pr .ld{aspect-ratio:4/5}
.bh-pr .row{display:flex;justify-content:space-between;align-items:baseline;gap:12px}.bh-pr h3{font-size:1.25rem}.bh-pr .p{font:700 1.1rem var(--f-head);color:var(--c-accent);white-space:nowrap}
.bh-pr small{color:var(--bh-ink3);font-size:13px}
.bh-add{justify-self:start}

/* ── about / contact ── */
.bh-team{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,3vw,32px)}
.bh-tm .ap-art{aspect-ratio:4/5;border-radius:var(--bh-rad);border:1px solid var(--c-border);margin-bottom:14px}.bh-tm h3{font-size:1.25rem}.bh-tm small{color:var(--bh-ink3);font-size:13px;letter-spacing:.08em;text-transform:uppercase}.bh-tm p{color:var(--bh-ink2);font-size:15px;margin-top:8px}
.bh-vals{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,3vw,32px)}
.bh-vals .bh-card{padding:clamp(20px,3vw,32px)}.bh-vals h3{font-size:1.3rem;margin:10px 0 8px}.bh-vals p{color:var(--bh-ink2);font-size:15px}
.bh-form{display:grid;gap:18px}.bh-form .g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.bh-form label{display:grid;gap:8px;font:700 11px/1 var(--f-head);letter-spacing:.22em;text-transform:uppercase;color:var(--bh-ink3)}
.bh-form input,.bh-form select,.bh-form textarea{width:100%;min-height:52px;padding:14px 16px;border-radius:12px;border:1.5px solid var(--c-border);background:color-mix(in srgb,var(--c-surface) 90%,var(--c-secondary));color:var(--c-text);font:400 16px/1.4 var(--f-body);text-transform:none;letter-spacing:0}
.bh-form textarea{min-height:140px;resize:vertical}.bh-form input:focus,.bh-form select:focus,.bh-form textarea:focus{outline:none;border-color:var(--c-accent);box-shadow:0 0 0 3px color-mix(in srgb,var(--c-accent) 28%,transparent)}
.bh-ok{display:none;padding:20px;border:1.5px solid var(--c-accent);border-radius:12px;color:var(--c-primary)}.bh-ok.on{display:block}
.bh-nf{min-height:70svh;display:grid;place-items:center;text-align:center;padding:clamp(72px,12vw,140px) 0}
.bh-nf .big{font:700 clamp(7rem,30vw,20rem)/.8 var(--f-head);color:transparent;-webkit-text-stroke:2px var(--c-accent);margin:0 0 16px}

/* ── effect hooks inside this template ── */
.zp-stage,.nm-stage,.ss-on .ss-stage{background:var(--c-surface)}
.zp-card{background:var(--bh-card);color:var(--c-text);border:1px solid var(--c-border)}
.zp-card a{background:var(--c-accent);color:var(--on-accent)}
.zt-on .zt-title h2{text-transform:uppercase;letter-spacing:.02em}
.ss-t h3,.zp-over h3{text-transform:none}
.ss-art,.zp-pic .ap-art{border:0}
.nm-num{color:var(--c-primary)}.nm-sec,.zt-sec,.zp-sec,.ss-sec{position:relative}
.vs-c .ap-art{aspect-ratio:16/10}
.pf{text-decoration:none;-webkit-tap-highlight-color:transparent}
.pf-solid{background:var(--c-accent);border-color:var(--c-accent);color:var(--on-accent);--c:var(--c-primary);--oc:var(--on-primary)}
.pf-solid.is-in{border-color:var(--c-primary)}
.pf-sm{padding:.7em 1.3em;font-size:.86em}
.pf{font-family:var(--f-head);font-weight:700;letter-spacing:.16em;text-transform:uppercase;font-size:.8em}
.sc-c.sc-u{color:var(--c-accent)}

/* ── responsive ── */
@media(max-width:960px){
.bh-nav{position:fixed;inset:72px 0 auto 0;flex-direction:column;gap:0;padding:12px clamp(18px,4vw,48px) 28px;background:var(--bh-deep);border-bottom:1px solid var(--c-border);transform:translateY(-8px);opacity:0;visibility:hidden;transition:transform .3s,opacity .3s,visibility .3s;margin:0}
.bh-nav.open{transform:none;opacity:1;visibility:visible}.bh-nav a{min-height:56px;font-size:15px;border-bottom:1px solid var(--c-border)}.bh-nav a::after{display:none}
.bh-burger{display:block}.bh-top .pf-sm{display:none}
.bh-foot .cols{grid-template-columns:1fr 1fr}.bh-lay{grid-template-columns:minmax(0,1fr)}.bh-reserve{position:static}
.bh-jcards,.bh-pgrid,.bh-team,.bh-vals{grid-template-columns:repeat(2,minmax(0,1fr))}
.bh-facts{grid-template-columns:repeat(2,minmax(0,1fr))}.bh-facts div:nth-child(2){border-right:0}.bh-facts div:nth-child(-n+2){border-bottom:1px solid var(--c-border)}
}
@media(max-width:700px){
.bh-state,.bh-fr .row,.bh-fr .row.rev,.bh-ph .row,.bh-two,.bh-next{grid-template-columns:minmax(0,1fr)}
.bh-fr .row.rev .cr-fig{order:0}
.bh-jcards,.bh-pgrid,.bh-team,.bh-vals{grid-template-columns:minmax(0,1fr)}
.bh-mini{grid-template-columns:repeat(3,minmax(0,1fr))}.bh-mini b{font-size:1.5rem}
.bh-form .g2{grid-template-columns:minmax(0,1fr)}.bh-foot .cols{grid-template-columns:minmax(0,1fr)}
.bh-dep .cf-row{grid-template-columns:2.4em minmax(0,1fr) auto}.bh-dep .cf-row .c{display:none}
.bh-hero{margin-top:-72px}.bh-ph .sp{max-height:46svh;aspect-ratio:1/1}
.bh-hero .mt-t{font-size:26vw}.bh-art-hero .mt-t{font-size:16.5vw}
}
@media(prefers-reduced-motion:reduce){.bh-cue::after{animation:none}.bh-nav a::after,.bh-top{transition:none}}
'''


def build():
    # effect rules first, so this template's own rules (later, same specificity) win
    return effect_css() + "\n" + CSS
