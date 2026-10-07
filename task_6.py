types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 

def remove_duplicates(tickets):
    unique_tickets = {}
    used = []
    for level in tickets:
        unique_tickets[level] = []
        for ticket in tickets[level]:
            if ticket not in used:
                unique_tickets[level].append(ticket)
                used.append(ticket)
    return unique_tickets

def tickets_by_type(types, tickets):
    unique_tickets = remove_duplicates(tickets)
    result = {}
    for level in types:
        result[types[level]] = unique_tickets[level]
    return result