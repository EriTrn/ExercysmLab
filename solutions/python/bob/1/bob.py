def response(hey_bob):
    msg = hey_bob.strip()
    if not msg:
        return "Fine. Be that way!"

    is_shouting = msg.isupper()
    is_question = msg.endswith("?")

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shouting:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
    