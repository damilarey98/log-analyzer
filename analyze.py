with open("sample_auth.log") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())