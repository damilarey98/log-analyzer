import argparse
import re
from collections import Counter

PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(\S+) from (\d{1,3}(?:\.\d{1,3}){3})"
)


def parse_log(path):
    ip_counts = Counter()
    user_counts = Counter()
    total = 0
    with open(path) as f:
        for line in f:
            match = PATTERN.search(line)
            if match:
                user, ip = match.groups()
                ip_counts[ip] += 1
                user_counts[user] += 1
                total += 1
    return total, ip_counts, user_counts


def print_report(total, ip_counts, user_counts, top):
    print(f"Total failed login attempts: {total}\n")
    print(f"Top {top} IP addresses:")
    for ip, count in ip_counts.most_common(top):
        print(f"  {ip:<18} {count}")
    print(f"\nTop {top} usernames tried:")
    for user, count in user_counts.most_common(top):
        print(f"  {user:<18} {count}")


def main():
    parser = argparse.ArgumentParser(description="Summarize failed SSH logins.")
    parser.add_argument("logfile", help="path to the log file")
    parser.add_argument("--top", type=int, default=10, help="how many entries to show")
    args = parser.parse_args()

    total, ip_counts, user_counts = parse_log(args.logfile)
    print_report(total, ip_counts, user_counts, args.top)


if __name__ == "__main__":
    main()