# learn-flask
will be read in 02-08-2025
Part 1: Build the API
You are required to build a simple API using Python and Flask with the following specifications:

The API must support at least two endpoints:

1. GET /items – return a list of todo items
2. POST /items – add a new item to the list
Store data in memory (no database required)
The server must be runnable locally ( python app.py or Docker)

Part 2: Interact With the API
Test your API using:
curl or Postman
A browser (if rendering JSON)
Add 10–100 items to simulate real use


Part 3: Analyze the Performance
Use at least two of the following:
curl -w to measure request time
Chrome DevTools → Network tab
top or htop to monitor CPU and memory
time command in terminal
Optional: ab (ApacheBench) or wrk to simulate load

Bonus Ideas (Optional)
1. Run a stress test using tools like ab
2. Refactor using asyncio , multiprocessing , or a DB
Report Guidelines
Write a 1-page report with the following:
Overview of the API (What does it do?)
How you tested it (Which tools did you use?)
What you observed (response times, CPU, memory, etc.)
What would you improve if traffic increased (add caching? use a DB? async?)
