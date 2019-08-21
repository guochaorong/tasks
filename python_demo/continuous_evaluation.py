import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import CostKpi, DurationKpi, AccKpi

p99_kpi = DurationKpi('99', 0.05, actived=True)
avg_kpi = DurationKpi('avg', 0.05, actived=True)
qps_kpi = AccKpi('qps', 0.05, actived=True)
#ok_kpi = AccKpi('ok', 0.05, actived=True)

tracking_kpis = [
    p99_kpi,
    avg_kpi,
    qps_kpi,
]
