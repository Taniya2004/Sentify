from django import template

register = template.Library()

@register.filter
def exclude_user(users, user):
    """
    Exclude the given user from the users queryset or list.
    """
    return [u for u in users if u != user]

@register.filter
def usernames_excluding(users, user):
    """
    Return a comma-separated string of usernames excluding the given user.
    """
    filtered = [u.username for u in users if u != user]
    return ", ".join(filtered)
