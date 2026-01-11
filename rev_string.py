text = input("Enter text:")

def rev_str(inp_text):
    rev = ""
    for ch in inp_text:
        rev =  ch+rev
        
    return rev.lower()
        
print(rev_str(text))