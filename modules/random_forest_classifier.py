# random_forest_classifier.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report
from modules.data_preprocessing import preprocess_stock_data, create_price_movement_labels


import ta

# Import SMOTE for handling class imbalance
from imblearn.over_sampling import SMOTE

def train_random_forest_classifier(stock_data):
    """
    Trains a Random Forest Classifier to predict stock price movements (up or down).
    :param stock_data: DataFrame containing stock data with 'Close' column.
    :return: Trained classifier, accuracy score, and classification report.
    """
    # Preprocess data and create price movement labels
    stock_data = preprocess_stock_data(stock_data)
    stock_data = create_price_movement_labels(stock_data)

    # Feature Engineering: Add technical indicators using ta
    stock_data['RSI'] = ta.momentum.RSIIndicator(
        close=stock_data['Close'], window=14
    ).rsi()

    stock_data['MA10'] = ta.trend.SMAIndicator(
        close=stock_data['Close'], window=10
    ).sma_indicator()

    stock_data['MA50'] = ta.trend.SMAIndicator(
        close=stock_data['Close'], window=50
    ).sma_indicator()


    # Drop rows with NaN values resulting from indicators
    stock_data = stock_data.dropna()

    # Features and target
    X = stock_data.drop(columns=['Price Movement', 'Close'])
    y = stock_data['Price Movement']

    # Split data (without shuffling for time series)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.2
    )

    # Address class imbalance using SMOTE
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    # Hyperparameter tuning using RandomizedSearchCV
    param_dist = {
    'n_estimators': [100, 200],        # Added parameter
    'max_depth': [None, 10, 20],       # Expanded options
    'min_samples_split': [2, 5],       # Expanded options
    'min_samples_leaf': [1, 2],        # Expanded options
    'max_features': ['sqrt', 'log2'],  # Expanded options
    'bootstrap': [True, False]         # Added parameter
    }

    random_search = RandomizedSearchCV(
        estimator=RandomForestClassifier(random_state=42),
        param_distributions=param_dist,
        n_iter=10,  # Now acceptable since we have more combinations
        cv=3,
        scoring='accuracy',
        n_jobs=-1,
        random_state=42
    )


    random_search.fit(X_train_resampled, y_train_resampled)
    classifier = random_search.best_estimator_

    # Evaluate the classifier
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)

    return classifier, accuracy, report