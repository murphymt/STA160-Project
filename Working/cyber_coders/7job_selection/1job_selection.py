# Candidate 1: skills, location preferences, search terms, and preferred salary
# Candidate 2: skills, location preferences, search terms, and preferred salary
# Candidate 3: skills, location preferences, search terms, and preferred salary
# Candidate 4: skills, location preferences, search terms, and preferred salary

# Match each candidates profile to the overall job data and return a subset

# Criteria:
# Exceptional Candidate:
# Locations -> exact matches
# Search terms -> exact matches
# Preferred salary -> within the minimum and maximum salary range
# Skills -> Matched with ~80% of listed skills

# Good Candidate:
# Locations -> exact matches and same states
# Search terms -> exact matches
# Preferred salary -> within minus 20,000 minimum salary
# Skills -> Matched with ~60% of listed skills

# Poor Candidate:
# Locations -> state is not included in preferences
# Search terms -> not a match
# Preferred salary -> less than minus 20,000 minimum salary
# Skills -> less than ~50% of listed skills

# Return exceptional and good candidate listing along with their URLs
