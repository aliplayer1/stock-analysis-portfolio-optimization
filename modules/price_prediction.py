from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from modules.data_preprocessing import preprocess_stock_data

def train_decision_tree_model(df, target_column):
    """
    Train a Decision Tree model to predict stock prices.
    """
    df = preprocess_stock_data(df)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    
    return model

def predict_stock_price(model, input_data):
    """
    Use the trained model to predict future stock prices.
    """
    return model.predict(input_data)
