import re

def normalize_phones(s):
    pat = re.compile(r"(?:\+?91|\(?91\)?|0091)[\s-]*([\d\s-]{10,})")
    def repl(m):
        digits = re.sub(r"\D", "", m.group(1))
        digits = digits[-10:]
        return f"+91{digits}"

    return pat.sub(repl, s)


s = "Contact:+91-9876543210, Office:(91) 98765 43210, Home:0091 9876543210"
print(normalize_phones(s))
