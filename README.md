# 🚀 Smart Log Analyzer (Mini AI Tool)

# 🚀 Smart Log Analyzer (Mini AI Tool)
#### Smart Log Analyzer is a Python-based tool that reads server logs from a file, analyzes them, and provides useful insights. It helps in understanding system behavior by categorizing logs, generating summaries, and visualizing data.

## 🎯 Objective
### To build a simple log analysis tool that:

#### Extracts useful insights
#### Allows filtering and searching
#### Allows filtering and searching


# 📂 Input

## The program reads logs from a file named logs.txt

#### 2026-03-20 10:15:32 INFO User login successful user_id=101 
#### 2026-03-20 10:17:45 ERROR Database connection failed
#### 2026-03-20 10:18:10 INFO User logout user_id=101
#### 2026-03-20 10:25:11 ERROR Timeout while connecting API
#### 2026-03-20 10:20:01 WARNING Disk space low

# ⚙️ Features

### ✅ Parse logs (timestamp, level, message)
### ✅ Display original logs
### ✅ Generate insights:

#### . Total logs
#### . INFO / ERROR / WARNING count
#### . Most common error
#### . First and last timestamp

#✅ Search logs by type:

#### . INFO
#### . ERROR
#### . WARNING

# ✅ Show filtered logs with:

#### . Timestamp
#### . Message
#### . Count

#### ✅ Export report in JSON format
#### ✅ Data visualization using matplotlib
#### ✅ Command-based interactive system

# 💻 Commands            Command	Description

     #### result	             Show original logs + full analysis
     #### search	             Filter logs by type (info/error/warning)
     #### json	               Export analysis report to JSON file
     #### graph	             Show log distribution graph
     #### exit	               Exit the program


# 📊 Output

 ### 1. Console Output
   #### . Original logs
   #### . Summary insights
   #### . Filtered logs  


 ### 2. JSON File (report.json)
{
  "total_logs": 5,
  "info_count": 2,
  "error_count": 2,
  "warning_count": 1,
  "most_common_error": "Timeout while connecting API",
  "first_timestamp": "2026-03-20 10:15:32",
  "last_timestamp": "2026-03-20 10:25:11"
}
### 3. Graph
Bar chart showing INFO, ERROR, WARNING counts



 # 🧠 Concepts Used
  #### . File Handling
  #### . String Manipulation
  #### . Data Structures (List, Dictionary)
  #### . Conditional Logic
  #### . JSON Handling
  #### . Data Visualization (Matplotlib)


# 🎯 Use Case
  #### . Server log monitoring
  #### . Error tracking
  #### . System analysis
  #### . Beginner data analytics project
  
