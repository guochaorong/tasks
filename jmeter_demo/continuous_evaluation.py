import os
import sys
sys.path.append(os.environ['ceroot'])
from kpi import CostKpi, DurationKpi, AccKpi

p99_kpi = DurationKpi('99', 0.2, actived=True)
avg_kpi = DurationKpi('avg', 0.2, actived=True)
qps_kpi = AccKpi('qps', 0.2, actived=True)
err_kpi = AccKpi('err', 0.2, actived=True)

tracking_kpis = [
    p99_kpi,
    avg_kpi,
    qps_kpi,
    err_kpi
]
