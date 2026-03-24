import json
import matplotlib.pyplot as plt

# ------------------ INPUT FROM FILE ------------------
logs = []

try:
    with open("logs.txt", "r") as f:
        for line in f:
            if line.strip() != "":
                logs.append(line.strip())
except FileNotFoundError:
    print("logs.txt file not found!")
    exit()

# ------------------ PARSING ------------------
parsed_logs = []

for log in logs:
    parts = log.split(" ")

    if len(parts) < 4:
        continue

    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = " ".join(parts[3:])

    parsed_logs.append({
        "timestamp": timestamp,
        "level": level,
        "message": message
    })

# ------------------ ANALYSIS ------------------
info_logs = []
error_logs = []
warning_logs = []

for log in parsed_logs:
    if log["level"] == "INFO":
        info_logs.append(log)
    elif log["level"] == "ERROR":
        error_logs.append(log)
    elif log["level"] == "WARNING":
        warning_logs.append(log)

info = len(info_logs)
error = len(error_logs)
warning = len(warning_logs)

# most common error
most_error = "None"
if error_logs:
    msgs = [log["message"] for log in error_logs]
    most_error = max(set(msgs), key=msgs.count)

first_time = parsed_logs[0]["timestamp"]
last_time = parsed_logs[-1]["timestamp"]

# ------------------ COMMAND LOOP ------------------
print("\nCommands:")
print("result → show logs + full result")
print("search → filter logs")
print("json   → export JSON")
print("graph  → show graph")
print("exit   → close")

while True:
    cmd = input("\nEnter command: ").lower()

    # -------- RESULT --------
    if cmd == "result":

        # ORIGINAL LOGS
        print("\n--- ORIGINAL LOGS ---\n")
        for log in parsed_logs:
            print(f"{log['timestamp']} {log['level']} {log['message']}")

        # FULL RESULT
        print("\n--- FULL RESULT ---")
        print("Total logs:", len(parsed_logs))
        print("INFO:", info)
        print("ERROR:", error)
        print("WARNING:", warning)
        print("Most common error:", most_error)
        print("First timestamp:", first_time)
        print("Last timestamp:", last_time)

    # -------- SEARCH --------
    elif cmd == "search":
        key = input("Enter type (info/error/warning): ").lower()

        if key == "info":
            selected = info_logs
        elif key == "error":
            selected = error_logs
        elif key == "warning":
            selected = warning_logs
        else:
            print("Invalid input!")
            continue

        print(f"\n--- {key.upper()} Logs ---")

        count = 0

        for log in selected:
            print(f"{log['timestamp']} → {log['message']}")
            count += 1

        print("\nCount:", count)

    # -------- JSON --------
    elif cmd == "report":
        report = {
            "total_logs": len(parsed_logs),
            "info_count": info,
            "error_count": error,
            "warning_count": warning,
            "most_common_error": most_error,
            "first_timestamp": first_time,
            "last_timestamp": last_time
        }

        with open("report.json", "w") as f:
            json.dump(report, f, indent=4)

        print("JSON report saved")

    # -------- GRAPH --------
    elif cmd == "graph":
        x = ["INFO", "ERROR", "WARNING"]
        y = [info, error, warning]
        colors = ["green", "red", "orange"]

        plt.bar(x, y, color=colors)

        for i in range(len(x)):
            plt.text(i, y[i], str(y[i]), ha='center')

        plt.title("Log Analysis")
        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.show()

    # -------- EXIT --------
    elif cmd == "exit":
        print("Program closed")
        break

    else:
        print("Invalid command!")