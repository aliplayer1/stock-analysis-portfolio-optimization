import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import io
import re

def format_axis(ax):
    def y_axis_formatter(x, pos):
        if x >= 1e9:
            return f'{x/1e9:.1f}B'
        elif x >= 1e6:
            return f'{x/1e6:.1f}M'
        else:
            return f'{x:.2f}'  # Display the actual price without scaling
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(y_axis_formatter))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()

def make_svg_responsive(svg_data):
    # Remove width and height attributes from the <svg> tag
    svg_data = re.sub(r'(<svg[^>]*?)\swidth="[^"]+"', r'\1', svg_data)
    svg_data = re.sub(r'(<svg[^>]*?)\sheight="[^"]+"', r'\1', svg_data)

    # Add responsive attributes
    svg_data = svg_data.replace('<svg ', '<svg width="100%" height="100%" preserveAspectRatio="xMinYMin meet" ')

    return svg_data

def generate_price_chart(stock_data, ticker):
    img = io.BytesIO()
    plt.figure()
    ax = plt.gca()
    plt.plot(stock_data.index, stock_data['Close'], label=f'{ticker.upper()} Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'Price Chart for {ticker.upper()}')
    plt.grid(True)
    plt.legend()

    format_axis(ax)  # Make sure prices are not unnecessarily scaled

    plt.savefig(img, format='svg')
    img.seek(0)
    svg_data = img.getvalue().decode('utf-8')
    plt.close()

    svg_data = make_svg_responsive(svg_data)

    return svg_data

def generate_clustering_chart(clustered_data, ticker):
    img = io.BytesIO()
    plt.figure()
    ax = plt.gca()
    scatter = plt.scatter(clustered_data.index, clustered_data['Close'], c=clustered_data['Cluster'], cmap='viridis')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'K-Means Clustering for {ticker.upper()}')
    plt.grid(True)

    format_axis(ax)  # Make sure prices are not unnecessarily scaled

    cbar = plt.colorbar(scatter)
    cbar.set_label('Cluster')

    plt.savefig(img, format='svg')
    img.seek(0)
    svg_data = img.getvalue().decode('utf-8')
    plt.close()

    svg_data = make_svg_responsive(svg_data)

    return svg_data
