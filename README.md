
***

# StockCredXAI- Explainable AI Driven Stock Credibility System Using Multi AI Agents.

A comprehensive, modular agent-based solution for stock credibility scoring, financial trend analysis, technical and fundamental modeling, and sentiment AI. The pipeline supports multiple explainable models, including LIME, SHAP, and interpretable neural architectures, and enables robust time series forecasting with LSTM, ARIMA, and Prophet.

## Features

- **Financial, Industry, Fundamental, Technical, Sentimental, & Credibility Scoring** for any stock ticker.[1]
- **Explainable AI & Model Interpretation:** SHAP and LIME analysis for transparency into model predictions.[1]
- **Time Series Forecasting:** Advanced prediction using LSTM, ARIMA, and Prophet; supports correlation and trend analysis.[2]
- **Visualization Suite:** Line plots, heatmaps, boxplots, attention weights, and more for feature and prediction inspection.[2]
- **Agentic Architecture:** Modular design allows for expandable agents: Financial, Industry, Technical, Sentimental.[1]
- **Sentiment Analysis:** Integrated FinBERT sentiment pipeline for financial news and headlines.[1]
- **Parallel Processing:** Efficient analysis of multiple stocks with concurrent execution.[1]
- **Streamlit Integration:** Rapid deployment as a web app.

## Table of Contents

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Pipeline Overview](#pipeline-overview)
- [Modules](#modules)
- [Data Preparation](#data-preparation)
- [Model Explainability](#model-explainability)
- [Visualization](#visualization)
- [Forecasting](#forecasting)
- [Contributing](#contributing)
- [License](#license)

***

### Installation

```bash
pip install yfinance pandas numpy matplotlib seaborn scikit-learn tensorflow statsmodels pmdarima prophet transformers lime streamlit pyngrok
```
> NLTK resources required for sentiment analysis:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

***

### Quickstart

1. Clone the repository.
2. Prepare your input stock tickers and, optionally, CSV data (`TSLA_cleaned_last_150_days.csv`, `credibility.csv`).
3. Run the main pipeline agent script.

```bash
python main.py
```

Or launch the Streamlit app:
```bash
streamlit run app.py
```
***

### Pipeline Overview

- The pipeline consists of independent agents for each analytic task:
  - FinancialAgent: Fundamental ratio scoring (P/E, P/B, PEG, Dividend Yield)
  - IndustryTrendAgent: Macro trend scores (durability, valuation, momentum)
  - FundamentalAgent: Profit/loss, growth factors, leveraging transformer-based text generation
  - TechnicalAgent: Moving averages, RSI, MACD, and aggregate technical scoring
  - SentimentalAnalyzerAgent: FinBERT and keyword-based sentiment for financial news
  - CredibilityModel: Merges all scores for final credibility forecasting
[1]

***

### Modules

| Agent           | Methodologies                       | Output Type         |
|-----------------|------------------------------------|---------------------|
| Financial       | Ratio-based scoring, SHAP          | Score; Explanation  |
| Industry Trend  | Revenue & profit macro analysis    | Score; SHAP plot    |
| Fundamental     | Text generation (transformers)     | Score; Text         |
| Technical       | TA indicators, LIME explainability | Score; Plot         |
| Sentiment       | FinBERT, NLP keywords              | Score; Attention    |
| Forecasting     | LSTM, ARIMA, Prophet               | Price/Score series  |
[2][1]

***

### Data Preparation

- Fetch with `yfinance`, preprocess for clean time series data
- Merge with custom credibility scores and sentiment scores per date
```python
import yfinance as yf
df = yf.download("TSLA", start=start_date, end=end_date)
df.to_csv("TSLA_cleaned_last_150_days.csv")
```


***

### Model Explainability

- **SHAP**: TreeSHAP explanations for feature importance across the agent's outputs
- **LIME**: Regression explainer for technical and fundamental scores
- **Attention Visualization**: For sentiment analysis, highlighting influential tokens
[2][1]

***

### Visualization

- Time series plots for all metrics
- Correlation heatmaps and distribution boxplots
- Dual-axis comparative plots for price vs. credibility scores
- Attention heatmaps for sentiment analysis
[2]

***

### Forecasting

Advanced predictive and comparative models:

- **LSTM**: Sequence modeling for price and credibility trends
- **ARIMA & Prophet**: Time series forecasting with auto hyperparameter selection and future predictions
- **Correlation Analysis**: Statistical relationship between price and credibility scores
[2]

***

### Contributing

Interested in expanding the pipeline? Submit a pull request with new agent types, model improvements, or integrations.

***

### License

Distributed under the Apache 2.0 License. See `LICENSE` for details.

***

## Contact & Support

For questions, custom integration, or deployment support, open an issue or contact the maintainer.

***

**Note:** For sample datasets and further module documentation, see the `examples/` directory and `notebooks/` included in the repo.

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/83134720/d04298c6-3e5f-48ad-9803-623be2fcf8af/vertopal.com_stock_credibility-1.pdf)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/83134720/5df2cbbd-14cf-4af3-ba62-845cca555c14/vertopal.com_lstm-arima-prophet-2-2.pdf)
