def clean_rank(rank_value):
    if isinstance(rank_value, (int, float)):
        return int(rank_value)
    
    rank_str = str(rank_value)
    
    # Handle intervals (e.g., "1000-1200" -> average)
    if '-' in rank_str:
        parts = rank_str.split('-')
        if len(parts) == 2:
            try:
                start = int(parts[0])
                end = int(parts[1])
                return int((start + end) / 2)
            except ValueError:
                return rank_value
    
    # Handle "+" cases (e.g., "1400+" -> 1400)
    if '+' in rank_str:
        try:
            return int(rank_str.replace('+', ''))
        except ValueError:
            return rank_value
    
    # Try to convert to int directly
    try:
        return int(rank_value)
    except ValueError:
        return rank_value
    
def clean_size(size_value):
    if isinstance(size_value, (int, float)):
        return int(size_value)
    
    # data: S,M,L,XL
    size_str = str(size_value).strip().upper()
    size_str = size_str.replace(' ', '')  # Remove spaces
    size_str = size_str.replace('XL', '4').replace('S', '1').replace('M', '2').replace('L', '3')
    
    # Try to convert to int directly
    try:
        return int(size_str)
    except ValueError:
        return size_value
    
def clean_res(res_value):
    if isinstance(res_value, (int, float)):
        return int(res_value)
    
    res_str = str(res_value).strip().upper()
    
    # data: LO,MD,HI,VH
    res_str = res_str.replace(' ', '')  # Remove spaces
    res_str = res_str.replace('LO', '1').replace('MD', '2').replace('HI', '3').replace('VH', '4')
    
    # Try to convert to int directly
    try:
        return int(res_str)
    except ValueError:
        return res_value