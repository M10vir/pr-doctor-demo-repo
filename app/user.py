def get_user(user_id):
    # Safe pattern: parameterized queries (example placeholder)
    query = "SELECT * FROM users WHERE id = %s"
    params = (user_id,)
    return query, params
