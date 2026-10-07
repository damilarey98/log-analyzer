import random

ips = ["203.0.113.5", "198.51.100.7", "192.0.2.44", "203.0.113.99", "198.51.100.23"]
users = ["root", "admin", "ubuntu", "test", "oracle"]

with open("sample_auth.log", "w") as f:
    for i in range(500):
        ip = random.choice(ips)
        user = random.choice(users)
        port = random.randint(1024, 65535)
        if random.random() < 0.7:
            f.write(f"Oct  6 10:{i % 60:02d}:11 myserver sshd[1234]: "
                    f"Failed password for invalid user {user} from {ip} port {port} ssh2\n")
        else:
            f.write(f"Oct  6 10:{i % 60:02d}:11 myserver sshd[1234]: "
                    f"Accepted password for {user} from {ip} port {port} ssh2\n")