print("analyzer.py started")
from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    print("\nPassword Strength Analysis")
    print("Score:", result['score'], "/ 4")
    print("Crack Time (offline):", result['crack_times_display']['offline_fast_hashing_1e10_per_second'])
    print("Feedback:", result['feedback']['warning'] or "Good password!", "\n")
    if result['feedback']['suggestions']:
        print("Suggestions:", ", ".join(result['feedback']['suggestions']))

if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ")
    analyze_password(pwd)
