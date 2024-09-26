from flask import Flask, render_template, request, flash
from modules.data_fetcher import get_financial_data
from modules.price_prediction import train_decision_tree_model
from modules.chart_generator import generate_price_chart, generate_clustering_chart
from modules.price_movement_classifier import train_price_movement_classifier
from modules.statistics_calculator import calculate_descriptive_statistics, calculate_rolling_statistics
from modules.stock_clustering import apply_kmeans  # Import clustering logic

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    ticker = request.form['ticker']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    analysis_type = request.form['analysis_type']  # Get the analysis type from the form

    # Fetch financial data and stock data
    financial_metrics, stock_data = get_financial_data(ticker, start_date, end_date)

    if stock_data.empty:
        flash(f"Not enough data available for {ticker}.", "error")
        return render_template('index.html')

    # Calculate descriptive and rolling statistics
    descriptive_stats = calculate_descriptive_statistics(stock_data)
    rolling_stats = calculate_rolling_statistics(stock_data)

    # Always generate price chart
    price_svg = generate_price_chart(stock_data, ticker)

    # Handle the user's selection for the second chart
    if analysis_type == 'price_clustering':
        try:
            # Apply K-Means clustering and generate clustering chart
            clustered_data, kmeans_model = apply_kmeans(stock_data, num_clusters=5)
            cluster_svg = generate_clustering_chart(clustered_data, ticker)
            return render_template(
                'results.html',
                ticker=ticker.upper(),
                financial_metrics=financial_metrics,
                price_svg_base64=price_svg,  # Always include the price chart
                cluster_svg_base64=cluster_svg,  # Include clustering chart
                descriptive_stats=descriptive_stats,
                rolling_stats=rolling_stats
            )
        except ValueError as e:
            flash(str(e), "error")
            return render_template('index.html')

    elif analysis_type == 'price_decision_tree':
        # Train decision tree classifier and calculate its accuracy
        classifier, accuracy, report = train_price_movement_classifier(stock_data)
        return render_template(
            'results.html',
            ticker=ticker.upper(),
            financial_metrics=financial_metrics,
            price_svg_base64=price_svg,  # Always include the price chart
            accuracy=accuracy,  # Include classifier accuracy
            classification_report=report,  # Include classification report
            descriptive_stats=descriptive_stats,
            rolling_stats=rolling_stats
        )

if __name__ == '__main__':
    app.run(debug=True)