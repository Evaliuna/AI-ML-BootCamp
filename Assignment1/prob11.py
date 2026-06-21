s = 'python programming'
s_clean = s.strip()

print(f"stripped version: '{s_clean}'")
print(f"stripped + upper(): '{s_clean.upper()}'")
print(f"stripped + title(): '{s_clean.title()}'")
print(f"stripped + replace(): '{s_clean.replace('python', 'data')}'")
print(f"Length of stripped string : {len(s_clean)}")
