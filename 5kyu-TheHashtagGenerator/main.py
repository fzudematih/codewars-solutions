def generate_hashtag(s):
    # your code here
    if not len(s.strip()): return False

    x = s.split(" ")
    strng = "#"
    for i in x:
        strng += i.capitalize()

    if len(strng) > 140: return False
    return strng

