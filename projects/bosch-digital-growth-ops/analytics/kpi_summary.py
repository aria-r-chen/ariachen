"""Strict KPI rollup on explicitly synthetic demonstration rows."""
import csv
import sys
from collections import defaultdict
from pathlib import Path

COLS = ('record_type','campaign_id','platform','views','inquiries','qualified_leads','completed_sales','spend_cny')
NUMERIC = ('views','inquiries','qualified_leads','completed_sales','spend_cny')

def pct(a,b):
    return 'N/A' if b == 0 else f'{a/b:.2%}'

def run(path):
    sums = defaultdict(lambda: {c: 0.0 for c in NUMERIC})
    with Path(path).open(encoding='utf-8-sig',newline='') as f:
        reader = csv.DictReader(f)
        if not set(COLS).issubset(reader.fieldnames or []):
            raise ValueError('Required columns missing')
        for row in reader:
            if row['record_type'] != 'SYNTHETIC':
                raise ValueError('Public demo only accepts explicitly SYNTHETIC data')
            vals = {c: float(row[c]) for c in NUMERIC}
            if any(v < 0 for v in vals.values()):
                raise ValueError('Metrics cannot be negative')
            if not vals['completed_sales'] <= vals['qualified_leads'] <= vals['inquiries'] <= vals['views']:
                raise ValueError('Funnel hierarchy invalid')
            for c in NUMERIC:
                sums[row['platform']][c] += vals[c]
    print('SYNTHETIC DEMO — NOT ACTUAL BUSINESS DATA')
    for platform,r in sorted(sums.items()):
        cpl='N/A' if not r['inquiries'] else f"{r['spend_cny']/r['inquiries']:.2f} CNY"
        print(f"{platform}: views={r['views']:g}, inquiries={r['inquiries']:g}, "
              f"inquiry/view={pct(r['inquiries'],r['views'])}, "
              f"qualified/inquiry={pct(r['qualified_leads'],r['inquiries'])}, "
              f"sales/qualified={pct(r['completed_sales'],r['qualified_leads'])}, "
              f"spend/inquiry={cpl}")
    print('LIMITATIONS: no causal attribution, profit, ROI or customer-acquisition-cost claim.')

if __name__ == '__main__':
    run(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name('example_campaigns_SYNTHETIC.csv'))
