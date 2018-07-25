# -*- coding: utf-8 -*-



nums =[1,2,3,4,7,12]
if len(nums) < 2:
    return 0

# Init bucket.
max_val, min_val = max(nums), min(nums)
gap = max(1, (max_val - min_val) / (len(nums) - 1))
bucket_size = int((max_val - min_val) / gap + 1)
bucket = [{'min':float("inf"), 'max':float("-inf")} \
            for _ in range(bucket_size)]


# Find the bucket where the n should be put.

n=9
for n in nums:
    # min_val / max_val is in the first / last bucket.
    if n in (max_val, min_val):
        print(n)
        continue
    i = int((n - min_val) / gap)
    bucket[i]['min'] = min(bucket[i]['min'], n)
    bucket[i]['max'] = max(bucket[i]['max'], n)

# Count each bucket gap between the first and the last bucket.
max_gap, pre_bucket_max = 0, min_val
for i in range(bucket_size):
    # Skip the bucket it empty.
    if bucket[i]['min'] == float("inf") and \
        bucket[i]['max'] == float("-inf"):
        continue
    max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
    pre_bucket_max = bucket[i]['max']
# Count the last bucket.
max_gap = max(max_gap, max_val - pre_bucket_max)

n=6

i = int((n - min_val) / gap)
bucket[i]['min'] = min(bucket[i]['min'], n)
bucket[i]['max'] = max(bucket[i]['max'], n)

i=1
max_gap = max(max_gap, bucket[i]['min'] - pre_bucket_max)
pre_bucket_max = bucket[i]['max']
