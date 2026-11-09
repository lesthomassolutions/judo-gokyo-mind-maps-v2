"""Reconstruct geometric diagrams as SVG; Pillow/OpenCV are build-time only.
Source GIFs remain immutable. Each map's colors and arrow directions come from
its own source pixels; no judo direction is inferred from technique names.
Run: python -m pip install pillow opencv-python-headless
     python scripts/recreate-maps.py
"""
import sys, json, math, html
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '.tools'))
from PIL import Image
import numpy as np
import cv2

WEB = ROOT / 'web'
data = json.loads((WEB / 'data.json').read_text(encoding='utf-8-sig'))
OUT = WEB / 'maps'
OUT.mkdir(exist_ok=True)
manifest = []
def hexcolor(c): return '#' + ''.join(f'{int(v):02x}' for v in c[:3])
def n(v): return f'{v:.2f}'.rstrip('0').rstrip('.')
def points(ps): return ' '.join(f'{n(x)},{n(y)}' for x,y in ps)

for src in dict.fromkeys(p['diagram'] for p in data['pages'].values() if p.get('diagram')):
    page = next(p for p in data['pages'].values() if p.get('diagram') == src and p.get('isTechnique')) if src != 'Files/Image/gnw.gif' else data['pages']['gokyo_no_waza']
    a = np.array(Image.open(WEB / src).convert('RGBA'))
    h,w = a.shape[:2]
    rgb = a[:,:,:3]; opaque = a[:,:,3] > 0
    # The source center disc has a unique pale-yellow fill.
    yellow = (rgb[:,:,0]>245)&(rgb[:,:,1]>220)&(rgb[:,:,1]<240)&(rgb[:,:,2]>140)&(rgb[:,:,2]<165)&opaque
    contours,_=cv2.findContours(yellow.astype('uint8'),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    c=max(contours,key=cv2.contourArea)
    (cx,cy),(dx,dy),_=cv2.fitEllipse(c)
    x,y,bw,bh=cv2.boundingRect(c); rx=(bw+2)/2;ry=(bh+2)/2;cx=x+(bw-1)/2;cy=y+(bh-1)/2
    disc=hexcolor(rgb[round(cy),round(cx+rx*.7)])
    yy,xx=np.indices((h,w));vx=xx-cx;vy=yy-cy;rad=np.hypot(vx,vy)
    base=rx*2.05
    sector_colors=[];vertices=[]
    for i in range(8):
        angle=-math.pi/2+i*math.pi/4
        middle=angle+math.pi/8
        sx=round(cx+base*math.cos(middle));sy=round(cy+base*math.sin(middle))
        patch=rgb[sy-3:sy+4,sx-3:sx+4].reshape(-1,3)
        vals,counts=np.unique(patch,axis=0,return_counts=True);sector_colors.append(vals[counts.argmax()].tolist())
    palette=np.array(sector_colors)
    colored=np.any(np.all(rgb[:,:,None,:]==palette[None,None,:,:],axis=3),axis=2)&opaque
    for i in range(8):
        angle=-math.pi/2+i*math.pi/4;ux,uy=math.cos(angle),math.sin(angle)
        along=vx*ux+vy*uy;across=np.abs(vx*uy-vy*ux)
        candidates=along[colored&(across<rx*.12)&(rad>rx*1.3)]
        length=float(np.max(candidates))+1
        vertices.append((cx+ux*length,cy+uy*length))
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{html.escape(page["title"])} — original directional map</title>','<desc id="desc">Vector reconstruction preserving the original sectors, arrows and success areas. Uke faces Tori. Attack links are provided by the surrounding map.</desc>']
    for i,color in enumerate(sector_colors):
        parts.append(f'<polygon points="{points([(cx,cy),vertices[i],vertices[(i+1)%8]])}" fill="{hexcolor(color)}" stroke="#c8c8c8" stroke-width="1.5"/>')
    arrows=[]
    black=(rgb.max(axis=2)<40)&opaque
    gray=(np.max(rgb,axis=2)-np.min(rgb,axis=2)<5)&(rgb[:,:,0]>180)&(rgb[:,:,0]<215)&opaque
    for i in range(8):
        angle=-math.pi/2+i*math.pi/4;ux,uy=math.cos(angle),math.sin(angle)
        along=vx*ux+vy*uy;across=np.abs(vx*uy-vy*ux)
        # Inspect the shaft only, away from center text and success labels.
        shaft=(along>rx*1.15)&(along<rx*2.45)&(across<rx*.045)
        isblack=int(np.sum(black&shaft))>int(np.sum(gray&shaft))
        color='#000000' if isblack else '#c8c8c8'
        # The eight original arrows have a shared reach; source-specific scale.
        length=rx*4.02
        candidates=along[(black if isblack else gray)&(across<rx*.16)&(along>rx*3.5)&(along<rx*4.3)]
        if len(candidates):length=float(candidates.max())
        width=rx*.14;head=rx*.35;headw=rx*.19
        def at(t,b):return(cx+ux*t-uy*b,cy+uy*t+ux*b)
        ps=[at(0,-width/2),at(length-head,-width/2),at(length-head,-headw),at(length,0),at(length-head,headw),at(length-head,width/2),at(0,width/2)]
        parts.append(f'<polygon data-direction="{i}" points="{points(ps)}" fill="{color}"/>')
        arrows.append('black' if isblack else 'gray')
    parts.append(f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}" fill="{disc}" stroke="#333" stroke-width="0.8"/>')
    if src == 'Files/Image/gnw.gif':
        parts.append(f'<text x="{n(cx)}" y="{n(cy-17)}" text-anchor="middle" font-family="Arial,sans-serif" font-size="27" font-weight="700">Uke</text>')
        # Trace the two original grey foot indicators, not a replacement stance.
        foot=(rgb[:,:,0]==132)&(rgb[:,:,1]==132)&(rgb[:,:,2]==132)&(yy>cy-6)&(yy<cy+ry)&(abs(vx)<rx*.65)&opaque
        cs,_=cv2.findContours(foot.astype('uint8'),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cs:
            if cv2.contourArea(c)>100:
                p=cv2.approxPolyDP(c,0.7,True).reshape(-1,2)
                parts.append(f'<polygon points="{points(p)}" fill="#848484"/>')
    else:
        # Preserve source label spelling/line breaks through explicit names.
        lines=page['id'].replace('kosoto','ko soto').replace('kouchi','ko uchi').replace('okuriashi','okuri ashi').replace('deashi','deashi').split('_')
        if page['id']=='harai_tsurikomi_ashi':lines=['Harai','Tsurikomi','Ashi']
        else:lines=[s.title() for s in lines]
        fs=min(rx*.43,rx*1.65/(max(map(len,lines))*.59));step=fs*1.15
        for j,line in enumerate(lines):
            ty=cy+(j-(len(lines)-1)/2)*step+fs*.34
            parts.append(f'<text x="{n(cx)}" y="{n(ty)}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{n(fs)}" font-weight="700">{html.escape(line)}</text>')
        # Locate each actual source success badge, preserving its own color/size.
        green=(rgb[:,:,1]>140)&(rgb[:,:,0]<60)&(rgb[:,:,2]<110)&opaque
        cs,_=cv2.findContours(green.astype('uint8'),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        badges=[]
        for c in cs:
            x,y,bw,bh=cv2.boundingRect(c)
            if bw>rx*1.4 and bh<ry*.9 and bh>ry*.25:
                vals,counts=np.unique(rgb[y:y+bh,x:x+bw].reshape(-1,3),axis=0,return_counts=True);fill=hexcolor(vals[counts.argmax()]);badges.append([x,y,bw,bh])
                parts.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="{n(bh*.15)}" fill="{fill}" stroke="#339933" stroke-width="{n(bh*.08)}"/>')
                parts.append(f'<text x="{n(x+bw/2)}" y="{n(y+bh*.68)}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{n(bh*.6)}" font-weight="700" fill="#006600">Success</text>')
        assert badges, page['id']+' has no success badge'
    parts.append('</svg>')
    name=Path(src).stem+'.svg';(OUT/name).write_text('\n'.join(parts),encoding='utf8')
    manifest.append({'source':src,'svg':'maps/'+name,'viewBox':[w,h],'center':[cx,cy,rx,ry],'sectorColors':list(map(hexcolor,sector_colors)),'arrowsClockwiseFromNorth':arrows})
    for p in data['pages'].values():
        if p.get('diagram')==src:p['vectorDiagram']='maps/'+name
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
(WEB/'data.json').write_text(json.dumps(data,separators=(',',':')),encoding='utf8')
print(f'Reconstructed {len(manifest)} genuine vector diagrams.')
