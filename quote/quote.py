def lawn_quote(size, same_day):
    if size == 'small':
        price = 10
    elif size == 'medium':
        price = 15
    elif size == 'large':
        price = 20
    else:
        return
    
    if same_day:
        price+=5

    return price