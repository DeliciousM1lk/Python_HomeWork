"""
Этот код возвращает домены из списка e-mail адресов
"""
def extract_domains(emails):
    """
    Этa функция возвращает домены из списка e-mail адресов
    """
    domains = []
    for email in emails:
        domain = email.split('@')[1]
        domains.append(domain)
    return domains

if __name__ == "__main__":
    emails_list = [
        "user1@example.com",
        "user2@gmail.com",
        "user3@yahoo.com"
    ]
    domains_list = extract_domains(emails_list)
    print(domains_list)
