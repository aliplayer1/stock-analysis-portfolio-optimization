from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from modules.data_preprocessing import preprocess_stock_data, create_price_movement_labels

def train_price_movement_classifier(stock_data):
    """
    Trains a Decision Tree Classifier to predict stock price movements (up or down).
    :param stock_data: DataFrame containing stock data with a 'Close' column.
    :return: Trained classifier, accuracy score, and classification report.
    """
    # Preprocess data and create price movement labels
    stock_data = preprocess_stock_data(stock_data)
    stock_data = create_price_movement_labels(stock_data)

    # Features and target for the classifier
    X = stock_data.drop(columns=['Price Movement', 'Close'])  # Exclude target and 'Close' from features
    y = stock_data['Price Movement']  # The target variable

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the classifier
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    # Make predictions and evaluate
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    return classifier, accuracy, report
