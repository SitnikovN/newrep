select max(datediff(cast(srch_co as date),cast(srch_ci as date))) max_search_days
from train
where srch_children_cnt>0
and srch_adults_cnt=2