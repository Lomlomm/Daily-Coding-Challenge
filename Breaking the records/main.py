def breakingRecords(scores):
    min_score = float('inf')
    max_score = float('-inf')
    cnt_min, cnt_max = 0,0 
    for i, score in enumerate(scores): 
        if i == 0: 
            min_score = score
            max_score = score
            continue
        if score < min_score:
            cnt_min += 1 
            min_score = score
        if score > max_score: 
            cnt_max += 1
            max_score = score
            
    return [cnt_max, cnt_min]