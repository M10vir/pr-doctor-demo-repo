def get_user(id):
    print("debug:", id)
    query = "SELECT * FROM users WHERE id=" + id  # SQL injection risk
    return query
