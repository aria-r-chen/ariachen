"""Build editor-neutral shotlist and prompt. No editing/publishing automation."""
import argparse
import csv
import json
from pathlib import Path

def build(src,outdir):
    brief=json.loads(Path(src).read_text(encoding='utf-8'))
    segments=brief.get('segments')
    if not isinstance(segments,list) or not segments:
        raise ValueError('A nonempty segments array is required')
    rows=[]
    prev=0.
    for idx,s in enumerate(segments,1):
        a,b=float(s['start_sec']),float(s['end_sec'])
        if a<prev or b<=a:
            raise ValueError(f'Segment {idx}: overlap or invalid duration')
        keys=['asset_key','visual_direction','narration','on_screen_text']
        if any(not str(s.get(k,'')).strip() for k in keys):
            raise ValueError(f'Segment {idx}: missing asset/visual/narration/caption')
        rows.append(dict(segment=idx,start_sec=a,end_sec=b,**{k:s[k] for k in keys}))
        prev=b
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)
    with (outdir/'shotlist.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    msg=['# Structured editor brief',f"Campaign: {brief.get('campaign_id','UNKNOWN')}",
         f"Status: {brief.get('status','UNVERIFIED')}",f"Audience: {brief.get('audience','')}",
         f"Customer problem: {brief.get('customer_problem','')}",
         f"Objective: {brief.get('objective','')}",f"Offer: {brief.get('offer','')}",
         f"Verification: {brief.get('source_check','')}",'']
    for r in rows:
        msg += [f"## Scene {r['segment']} · {r['start_sec']:g}–{r['end_sec']:g}s",
                f"Asset key: {r['asset_key']}",f"Visual: {r['visual_direction']}",
                f"Draft voiceover: {r['narration']}",f"Overlay: {r['on_screen_text']}",'']
    msg += ['## Human QA required','Check product claims, footage rights, timing, audio/subtitles, customer CTA and brand approval.',
            'No footage is assembled, synchronized, rendered or published by this script.']
    (outdir/'editor_prompt.md').write_text('\n\n'.join(msg)+'\n',encoding='utf-8')
    print('Created editor_prompt.md and shotlist.csv in',outdir)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('brief')
    p.add_argument('--outdir',default='output/demo')
    a=p.parse_args()
    build(a.brief,a.outdir)
