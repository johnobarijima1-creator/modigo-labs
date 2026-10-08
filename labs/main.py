def count_cheap_rides(fares, limit):
    """
    Counts how many fares in the list are strictly less than `limit`.
    Returns the count as an integer.
    """
    count = 0  # TODO: this should start at zero — is this right?

    for fare in fares:
        if fare < limit: 
            count = count + 1
    return count