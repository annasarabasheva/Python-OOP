def tags(html_tag):
    def decorator(function):
        def wrapper(*args):
            return f"<{html_tag}>{function(*args)}</{html_tag}>"
        return wrapper
    return decorator



@tags('p')
def join_strings(*args):
    return "".join(args)

print(join_strings("Hello", " you!"))
