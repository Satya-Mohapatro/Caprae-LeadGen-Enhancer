funding_rank = {
    "Seed": 1,
    "Series A": 2,
    "Series B": 3,
    "Series C": 4,
    "Series D": 5
}

def score_row(row, preferred_industries, min_funding_stage, emp_min, emp_max, preferred_location):
    score = 0
    if 'industry' in row and any(ind.lower() in str(row['industry']).lower() for ind in preferred_industries):
        score += 20

    if 'funding_stage' in row and funding_rank.get(row['funding_stage'], 0) >= funding_rank.get(min_funding_stage, 0):
        score += 20

    if 'employee_count' in row:
        try:
            emp_count = int(row['employee_count'])
            if emp_min <= emp_count <= emp_max:
                score += 15
        except:
            pass

    if 'location' in row and preferred_location.lower() in str(row['location']).lower():
        score += 10

    if 'email_status' in row and row['email_status'] == 'Valid':
        score += 10

    return score

def score_leads(df, preferred_industries, min_funding_stage, emp_min, emp_max, preferred_location):
    df['lead_score'] = df.apply(
        lambda row: score_row(row, preferred_industries, min_funding_stage, emp_min, emp_max, preferred_location),
        axis=1
    )
    return df
