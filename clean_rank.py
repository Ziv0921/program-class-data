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