# Stock News Alert System 📈

A Python application that retrieves daily stock prices, calculates price movements, and fetches relevant company news using external APIs.

The project currently uses Tesla (TSLA) as its example stock.

## Features

- Retrieves daily stock market data using Alpha Vantage.
- Compares consecutive trading-day closing prices.
- Calculates percentage price movement.
- Fetches relevant company news using NewsAPI.
- Prepares stock movement and news information for notifications.
- Includes Twilio integration code for SMS notifications.

## Tech Stack

- Python
- Requests
- Alpha Vantage API
- NewsAPI
- Twilio
- Python-dotenv

## Getting Started

### Prerequisites

- Python 3.x
- Alpha Vantage API key
- NewsAPI API key

Install dependencies:

```bash
pip install requests twilio python-dotenv
```

### Environment Variables

Create a `.env` file in the project root:

```env
AV_API_KEY=your_alpha_vantage_api_key
Newapi_API_KEY=your_newsapi_key
Twilio_account_sid=your_twilio_account_sid
Twilio_auth_token=your_twilio_auth_token
```

Never commit your `.env` file.

### Run the application

```bash
python main.py
```

## How It Works

1. Requests daily stock price information.
2. Retrieves the latest two available closing prices.
3. Calculates their percentage movement.
4. Fetches relevant company news.
5. Displays the stock movement and related news information.

## What I Learned

- Integrating multiple external APIs.
- Making HTTP requests using Requests.
- Processing JSON responses.
- Working with environment variables.
- Connecting financial data with relevant news information.
- Exploring automated notification services.

## Current Limitations

- Tesla (TSLA) is currently hardcoded.
- The current implementation prints stock and news information.
- The Twilio SMS-sending section is present but commented out.
- API usage is subject to the respective provider's limits.

This project is an educational demonstration and is not intended for financial advice or trading decisions.
