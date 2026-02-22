# Microservice Tester

A tester for **cs361_social_microservice**, **cs361_notification_microservice**, and **cs361_user_microservice**. The home page lists all microservices and their endpoints; each endpoint has its own page with inputs and results.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start your microservices (in separate terminals):
   - Social: `cd cs361_social_microservice && python3 app.py` (port 8000)
   - Notification: `cd cs361_notification_microservice && python3 app.py` (port 8001)
   - User: `cd cs361_user_microservice && python3 app.py` (port 8002)

3. Start the tester:
   ```bash
   python3 app.py
   ```

4. Open **http://127.0.0.1:5000** in your browser.
