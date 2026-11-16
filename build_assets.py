import math, random
random.seed(7)
BG="#0A100F"; PANEL="#111A18"; LINE="#1E2D29"; MINT="#5EEAD4"; CORAL="#FF8A65"; TXT="#E8F1EE"; MUTED="#7C918B"; SKY="#7DD3FC"
MONO='ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace'
SANS='"Segoe UI",system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif'
def w(name, s): open(f"assets/{name}.svg","w",encoding="utf-8").write(s)
def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
STYLE=f"""<style>.m{{font-family:{MONO}}}.s{{font-family:{SANS}}}
.in{{animation:in .8s cubic-bezier(.16,1,.3,1)}}
@keyframes in{{from{{opacity:.85;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
@keyframes blink{{50%{{opacity:0}}}}@keyframes pulse{{0%,100%{{r:5;opacity:.9}}50%{{r:8;opacity:.35}}}}
@keyframes dash{{to{{stroke-dashoffset:-60}}}}@keyframes float{{50%{{transform:translateY(-6px)}}}}
@media(prefers-reduced-motion:reduce){{*{{animation:none!important;opacity:1!important;transform:none!important}}}}</style>"""
def head(id,wd,ht,title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {wd} {ht}" role="img" aria-label="{esc(title)}"><title>{esc(title)}</title>{STYLE}'
def delay(i,base=0.15,step=0.12): return f'style="animation-delay:{base+i*step:.2f}s"'

# ---------- HERO ----------
def hero():
    s=head("h",1200,440,"Utkarsh Patwa — student developer and competitive programmer")
    s+=f'''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{BG}"/><stop offset=".6" stop-color="#0F1A17"/><stop offset="1" stop-color="{BG}"/></linearGradient>
<linearGradient id="ed" x1="0" x2="1"><stop stop-color="{MINT}" stop-opacity=".7"/><stop offset="1" stop-color="{CORAL}" stop-opacity=".5"/></linearGradient>
<linearGradient id="nm" x1="0" x2="1"><stop stop-color="{TXT}"/><stop offset="1" stop-color="{MINT}"/></linearGradient>
<radialGradient id="au"><stop stop-color="{MINT}" stop-opacity=".18"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{MINT}" fill-opacity=".12"/></pattern></defs>
<rect width="1200" height="440" rx="20" fill="url(#bg)"/><rect x="1" y="1" width="1198" height="438" rx="19" fill="url(#dots)" stroke="url(#ed)"/>
<circle cx="900" cy="220" r="260" fill="url(#au)"/>'''
    # window dots
    s+=f'<g><circle cx="44" cy="40" r="6" fill="{CORAL}"/><circle cx="64" cy="40" r="6" fill="#FFD166"/><circle cx="84" cy="40" r="6" fill="{MINT}"/></g>'
    s+=f'<text class="m" x="110" y="45" fill="{MUTED}" font-size="12" letter-spacing="2">~/utkarsh/profile.js</text>'
    s+=f'<text class="m in" x="48" y="120" fill="{MINT}" font-size="13" letter-spacing="4" {delay(0)}>HELLO, WORLD — I AM</text>'
    s+=f'<text class="s in" x="46" y="195" fill="url(#nm)" font-size="76" font-weight="800" letter-spacing="-2" {delay(1)}>Utkarsh Patwa</text>'
    s+=f'<text class="s in" x="48" y="240" fill="{TXT}" font-size="24" {delay(2)}>Student Developer <tspan fill="{CORAL}">/</tspan> Problem Solver <tspan fill="{CORAL}">/</tspan> Web Builder</text>'
    code=[("const","#C792EA"),]
    lines=[[("const ",CORAL),("me ",TXT),("= {",MUTED)],
           [("  school: ",SKY),('"Mirai School of Technology"',MINT),(",",MUTED)],
           [("  base: ",SKY),('"Ghaziabad, India"',MINT),(",",MUTED)],
           [("  solves: ",SKY),('["LeetCode", "Codeforces", "CodeChef"]',MINT),(",",MUTED)],
           [("};",MUTED)]]
    y=292
    for i,l in enumerate(lines):
        x=48
        sp=''.join(f'<tspan fill="{c}">{esc(t).replace(" ","&#160;")}</tspan>' for t,c in l)
        s+=f'<text class="m in" x="{x}" y="{y}" font-size="15" {delay(3+i,0.1,0.18)}>{sp}</text>'; y+=26
    s+=f'<rect x="48" y="{y-4}" width="9" height="18" fill="{MINT}" style="animation:blink 1s steps(1) infinite"/>'
    # binary tree
    nodes={0:(905,95),1:(800,170),2:(1010,170),3:(745,255),4:(855,255),5:(960,255),6:(1065,255),7:(715,340),8:(775,340),9:(1000,340),10:(1100,340)}
    edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(3,7),(3,8),(5,9),(6,10)]
    s+='<g fill="none" stroke-linecap="round">'
    for a,b in edges:
        (x1,y1),(x2,y2)=nodes[a],nodes[b]
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MINT}" stroke-opacity=".25" stroke-width="1.5"/>'
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MINT}" stroke-width="2" stroke-dasharray="6 54" style="animation:dash 3s linear infinite"/>'
    s+='</g>'
    for i,(x,y) in nodes.items():
        col=CORAL if i in (0,5) else MINT
        s+=f'<circle cx="{x}" cy="{y}" r="5" fill="{col}" style="animation:pulse {2+i%3*.6}s ease-in-out infinite;animation-delay:{i*.2}s"/>'
        s+=f'<circle cx="{x}" cy="{y}" r="14" fill="none" stroke="{col}" stroke-opacity=".35"/>'
    s+=f'<circle cx="905" cy="95" r="26" fill="{BG}" stroke="{CORAL}" stroke-width="2"/><text class="s" x="905" y="102" text-anchor="middle" fill="{CORAL}" font-size="19" font-weight="800">UP</text>'
    s+=f'<text class="m" x="1152" y="410" text-anchor="end" fill="{MUTED}" font-size="11" letter-spacing="3">O(log n) · KEEP LEARNING</text>'
    return s+'</svg>'
w("hero",hero())

# ---------- SECTION TITLES ----------
def title(slug,num,label,tag):
    s=head(slug,1200,110,f"{num} {label} — {tag}")
    s+=f'''<defs><linearGradient id="ln" x1="0" x2="1"><stop stop-color="{MINT}"/><stop offset=".7" stop-color="{MINT}" stop-opacity=".25"/><stop offset="1" stop-color="{CORAL}" stop-opacity="0"/></linearGradient></defs>
<text class="m in" x="8" y="42" fill="{CORAL}" font-size="14" letter-spacing="4" {delay(0)}>// {num} · {label.upper()}</text>
<text class="s in" x="6" y="88" fill="{TXT}" font-size="38" font-weight="800" letter-spacing="-1" {delay(1)}>{esc(tag)}</text>
<rect x="8" y="100" width="1184" height="2" fill="url(#ln)"/>'''
    return s+'</svg>'
for slug,num,label,tag in [("title-about","01","about","Code, curiosity, coffee."),("title-cp","02","problem solving","Practice makes patterns."),
    ("title-work","03","projects","Things I've built so far."),("title-toolkit","04","toolkit","What I build with."),
    ("title-activity","05","activity","One commit at a time."),("title-connect","06","connect","Let's build something.")]:
    w(slug,title(slug,num,label,tag))

# ---------- ABOUT CARD ----------
def about():
    s=head("a",1200,330,"About Utkarsh Patwa: student at Mirai School of Technology, based in Ghaziabad, interested in web development and problem solving.")
    s+=f'<rect x="1" y="1" width="1198" height="328" rx="18" fill="{PANEL}" stroke="{LINE}"/><rect x="1" y="1" width="1198" height="44" rx="18" fill="#0D1513"/><rect x="1" y="30" width="1198" height="15" fill="#0D1513"/>'
    s+=f'<text class="m" x="28" y="29" fill="{MUTED}" font-size="12" letter-spacing="2">about.json</text><text class="m" x="1172" y="29" text-anchor="end" fill="{CORAL}" font-size="12" letter-spacing="2">STATUS: LEARNING IN PUBLIC</text>'
    rows=[("name","Utkarsh Patwa"),("role","Student Developer"),("school","Mirai School of Technology"),("location","Ghaziabad, Uttar Pradesh"),
          ("interests","web dev · DSA · competitive programming"),("now","shipping projects & solving problems daily")]
    y=95
    for i,(k,v) in enumerate(rows):
        s+=f'<g class="in m" font-size="16" {delay(i,.1,.15)}><text x="48" y="{y}" fill="{SKY}">"{k}"</text><text x="170" y="{y}" fill="{MUTED}">:</text><text x="190" y="{y}" fill="{MINT}">"{esc(v)}"</text></g>'; y+=38
    s+=f'<text class="m" x="28" y="75" fill="{MUTED}" font-size="16">{{</text><text class="m" x="28" y="{y-8}" fill="{MUTED}" font-size="16">}}</text>'
    # right: stats tiles
    tiles=[("67","REPOSITORIES",MINT),("3","CP PLATFORMS",CORAL),("1","PULL SHARK",SKY)]
    x0=800
    for i,(n,l,c) in enumerate(tiles):
        yy=70+i*80
        s+=f'<g class="in" {delay(i+2,.2,.2)}><rect x="{x0}" y="{yy}" width="350" height="66" rx="12" fill="{BG}" stroke="{c}" stroke-opacity=".5"/><text class="s" x="{x0+24}" y="{yy+44}" fill="{c}" font-size="34" font-weight="800">{n}</text><text class="m" x="{x0+100}" y="{yy+39}" fill="{TXT}" font-size="13" letter-spacing="3">{l}</text></g>'
    return s+'</svg>'
w("about-card",about())

# ---------- COMPETITIVE PROGRAMMING ----------
def cp():
    s=head("cp",1200,200,"Competitive programming profiles on LeetCode, Codeforces and CodeChef")
    items=[("LEETCODE","Utkarsh_Patwa2025",MINT,"{ }"),("CODEFORCES","UTKARSHPATWA2026",CORAL,"</>"),("CODECHEF","utkarsh_patwa",SKY,"#")]
    for i,(n,u,c,ic) in enumerate(items):
        x=10+i*400
        s+=f'<g class="in" {delay(i,.1,.2)}><rect x="{x}" y="4" width="380" height="190" rx="18" fill="{PANEL}" stroke="{c}" stroke-opacity=".55"/>'
        s+=f'<circle cx="{x+66}" cy="100" r="42" fill="{BG}" stroke="{c}" stroke-width="2"/><text class="m" x="{x+66}" y="110" text-anchor="middle" fill="{c}" font-size="26" font-weight="700">{esc(ic)}</text>'
        s+=f'<text class="m" x="{x+126}" y="80" fill="{c}" font-size="13" letter-spacing="3">{n}</text><text class="s" x="{x+126}" y="112" fill="{TXT}" font-size="19" font-weight="700">{u}</text>'
        s+=f'<text class="m" x="{x+126}" y="142" fill="{MUTED}" font-size="12">solving · learning · repeat</text></g>'
    return s+'</svg>'
w("cp-card",cp())

# ---------- PROJECT CARDS ----------
def project(slug,name,desc,tech,c,n):
    s=head(slug,590,210,f"{name}: {desc}")
    s+=f'<rect x="2" y="2" width="586" height="206" rx="16" fill="{PANEL}" stroke="{c}" stroke-opacity=".5"/><rect x="2" y="2" width="6" height="206" rx="3" fill="{c}"/>'
    s+=f'<text class="m" x="32" y="40" fill="{c}" font-size="12" letter-spacing="3">PROJECT / {n:02d}</text>'
    s+=f'<text class="s" x="30" y="84" fill="{TXT}" font-size="30" font-weight="800">{esc(name)}</text>'
    # wrap desc
    words=desc.split(); lines=[]; cur=""
    for wd in words:
        if len(cur)+len(wd)+1>56: lines.append(cur); cur=wd
        else: cur=(cur+" "+wd).strip()
    if cur: lines.append(cur)
    for i,l in enumerate(lines[:2]): s+=f'<text class="s" x="32" y="{114+i*22}" fill="{MUTED}" font-size="15">{esc(l)}</text>'
    x=32
    for t in tech:
        wd=len(t)*8.2+24
        s+=f'<rect x="{x}" y="160" width="{wd:.0f}" height="28" rx="14" fill="{BG}" stroke="{c}" stroke-opacity=".6"/><text class="m" x="{x+wd/2:.0f}" y="179" text-anchor="middle" fill="{c}" font-size="12">{t}</text>'
        x+=wd+8
    s+=f'<text class="m" x="560" y="40" text-anchor="end" fill="{MUTED}" font-size="12">↗</text>'
    return s+'</svg>'
projects=[("project-jio","Jio Clone","Repository initialized for a Jio clone project, with initial README setup.",["README","Git"],MINT),
("project-phone","Phone Seller Site","Android phone storefront on AWS using private S3, CloudFront OAC, and CloudFormation.",["HTML/CSS","AWS S3","CloudFront"],CORAL),
("project-weather","Weather","Repository reserved on GitHub for a weather project; no commits published yet.",["Pending","GitHub"],SKY),
("project-snake","Snake","Repository reserved on GitHub for a snake game; no code published yet.",["Pending","GitHub"],MINT),
("project-portfolio","Portfolio","Developer portfolio command center built with React 19 and Tailwind CSS, hosted on Vercel.",["React","Tailwind","Vite","Vercel"],CORAL),
("project-mirai","Mirai Web Beta","Forked frontend curriculum repository covering HTML, CSS, and JavaScript lectures.",["HTML","CSS","JavaScript","Fork"],SKY)]
for i,(sl,nm,d,t,c) in enumerate(projects): w(sl,project(sl,nm,d,t,c,i+1))

# ---------- TOOLKIT ----------
def toolkit():
    groups=[("LANGUAGES",["C++","Python","JavaScript","HTML","CSS"],MINT),("LIBRARIES",["React","Node.js","Express","Tailwind CSS"],CORAL),("WORKFLOW",["Git","GitHub","AWS","Vercel","VS Code"],SKY)]
    s=head("tk",1200,260,"Toolkit: C++, Python, JavaScript, HTML, CSS, React, Node.js, Express, Tailwind CSS, Git, GitHub, AWS, Vercel, and VS Code")
    s+=f'<rect x="1" y="1" width="1198" height="258" rx="18" fill="{PANEL}" stroke="{LINE}"/>'
    y=50; k=0
    for g,items,c in groups:
        s+=f'<text class="m" x="36" y="{y+18}" fill="{c}" font-size="12" letter-spacing="3">{g}</text>'
        x=230
        for t in items:
            wd=len(t)*10+34
            s+=f'<g class="in" {delay(k,.1,.08)}><rect x="{x}" y="{y}" width="{wd}" height="32" rx="16" fill="{BG}" stroke="{c}" stroke-opacity=".6"/><text class="m" x="{x+wd/2:.0f}" y="{y+21}" text-anchor="middle" fill="{TXT}" font-size="14">{t}</text></g>'
            x+=wd+12; k+=1
        y+=72
    return s+'</svg>'
w("toolkit-card",toolkit())

# ---------- FOOTER ----------
def footer():
    s=head("f",1200,150,"Building things, one commit at a time.")
    s+=f'''<defs><linearGradient id="fg" x1="0" x2="1"><stop stop-color="{MINT}" stop-opacity=".0"/><stop offset=".5" stop-color="{MINT}"/><stop offset="1" stop-color="{CORAL}" stop-opacity="0"/></linearGradient></defs>
<rect x="1" y="1" width="1198" height="148" rx="18" fill="{BG}" stroke="{LINE}"/><rect x="60" y="24" width="1080" height="2" fill="url(#fg)"/>
<text class="s" x="600" y="78" text-anchor="middle" fill="{TXT}" font-size="26" font-weight="700">Still learning. Always shipping.</text>
<text class="m" x="600" y="110" text-anchor="middle" fill="{MUTED}" font-size="13" letter-spacing="2">while (alive) {{ learn(); build(); repeat(); }}</text>
<rect x="60" y="126" width="1080" height="2" fill="url(#fg)"/>'''
    return s+'</svg>'
w("footer",footer())
print("ok")
