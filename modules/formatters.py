def format_large_number(value):
    if value is None or value == 'N/A':
        return 'N/A'
    elif value >= 1_000_000_000_000:
        return f"{value / 1_000_000_000_000:.2f}T"
    elif value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    else:
        return f"{value:,}"

def format_ratio(value):
    if value is None or value == 'N/A':
        return 'N/A'
    return f"{value:.2f}"

def format_percentage(value):
    if value is None or value == 'N/A':
        return 'N/A'
    return f"{value * 100:.2f}%"
