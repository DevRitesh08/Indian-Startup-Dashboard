# Indian Startup Funding Analysis Dashboard 💰

Welcome to the **Indian Startup Funding Analysis Dashboard**! This interactive Streamlit app lets you explore, visualize, and analyze the landscape of startup funding in India. Dive deep into key investment trends, discover top startups and investors, and gain insights into the sectors shaping India’s entrepreneurial scene.

> 🚀 **Live Demo:**  
> [Indian Startup Dashboard](https://devritesh08-indian-startup-dashboard-app-xjdwry.streamlit.app/)

## Features

- **Overall Analysis**  
  - View total, maximum, and average funding amounts.
  - Month-over-month (MoM) graphs for total investment and deal count.
  - Insights into sector-wise funding and other high-level metrics.

- **Startup Analysis**  
  - Explore details for individual startups.
  - Find top-performing startups across years.

- **Investor Analysis**  
  - Discover individual investor profiles.
  - View recent investments, biggest investments, sectoral interests, investment stages, and city-wise funding breakdowns.
  - YoY (Year-over-Year) investment trends for each investor.

- **Interactive Visualizations**  
  - Bar charts, pie charts, line graphs, and more for clear and insightful analytics.

## How It Works

The application is built using [Streamlit](https://streamlit.io/), [Pandas](https://pandas.pydata.org/), and [Matplotlib](https://matplotlib.org/). It reads cleaned startup funding data and provides interactive dashboards and visualizations.

**Main modules:**

- `Overall Analysis`: High-level view of India's startup funding ecosystem.
- `StartUp`: Lookup and analyze specific startups.
- `Investor`: Deep-dive into individual investor activity and trends.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DevRitesh08/indian-startup-analysis.git
cd indian-startup-analysis
```

### 2. Install dependencies

```bash
pip install streamlit pandas matplotlib
```

### 3. Prepare the data

Ensure you have the cleaned dataset `startup_cleaned.csv` in the project directory. The CSV should have columns: `date`, `startup`, `investors`, `vertical`, `city`, `round`, `amount`, etc.

### 4. Run the app locally

```bash
streamlit run app.py
```

## Project Structure

```
├── app.py                # Main Streamlit application file
├── startup_cleaned.csv   # Cleaned startup funding dataset
├── README.md             # Project documentation
```

## Data Source

- The dashboard is powered by the `startup_cleaned.csv` dataset, which aggregates Indian startup funding information.  
- Data columns include:  
  - `date` (funding date)
  - `startup` (startup name)
  - `investors` (investor names)
  - `vertical` (industry/sector)
  - `city` (location)
  - `round` (funding round)
  - `amount` (funding amount, in crores)

## Usage

- Select **Overall Analysis** to get a quick summary and visualize funding trends.
- Choose **StartUp** to analyze details of a particular startup.
- Pick **Investor** to see the portfolio and trends of a specific investor.

## Deployment

The app is live at:  
[https://devritesh08-indian-startup-dashboard-app-xjdwry.streamlit.app/](https://devritesh08-indian-startup-dashboard-app-xjdwry.streamlit.app/)

## Contributing

Want to add more features or improve visuals? Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
