def build_filter_query(filters):

    where_clauses = []
    values = []
    
    for column, value in filters.items():
        
        where_clauses.append(f"{column} = %s")
        values.append(value)
    
    where_clause = ""
    if where_clauses:
        where_clause = " WHERE " + " AND ".join(where_clauses)
    
    return where_clause, values