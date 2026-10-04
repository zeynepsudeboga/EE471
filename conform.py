def pleaseConformOnepass(caps):
    if not caps:
        return
    
    first_cap = None
    for c in caps:
        if c != 'H':
            first_cap = c
            break
            
    if not first_cap:
        return

    caps = caps + [first_cap]
    start = -1
    
    for i in range(len(caps)):
        if caps[i] == 'H':
            if start != -1:
                if start == i - 1:
                    print(f"Person in position {start} flip your cap!")
                else:
                    print(f"People in positions {start} through {i - 1} flip your caps!")
                start = -1
            continue
        
        if caps[i] != first_cap and start == -1:
            start = i
            
        elif caps[i] == first_cap and start != -1:
            if start == i - 1:
                print(f"Person in position {start} flip your cap!")
            else:
                print(f"People in positions {start} through {i - 1} flip your caps!")
            start = -1

cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']
pleaseConformOnepass(cap3)