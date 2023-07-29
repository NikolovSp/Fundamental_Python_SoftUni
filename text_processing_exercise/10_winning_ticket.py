def check_ticket(ticket):
    if len(ticket) != 20:
        return 'invalid ticket'
    winning_symbols = ['@', '#', '$', '^']
    left_side = ticket[0:10]
    right_side = ticket[10:]

    for match_symbol in winning_symbols:
        for uninterrupted_symbol in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_symbol
            if winning_symbol_repetition in left_side and winning_symbol_repetition in right_side:
                if uninterrupted_symbol == 10:
                    return f'ticket "{ticket}" - {uninterrupted_symbol}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_symbol}{match_symbol}'

    return f'ticket "{ticket}" - no match'


all_tickets = [ticket.strip() for ticket in input().split(', ')]
#not additional spaces in the input

for ticket in all_tickets:
    print(check_ticket(ticket))
