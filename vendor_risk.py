import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_risk_scores(df):
    # Strip whitespace from column headers
    df.columns = df.columns.str.strip()
    print("Columns in CSV after stripping:", df.columns.tolist())

    # Try to select the features columns, catch if missing
    try:
        features = df[['on_time_pct', 'claim_rate', 'geopolitical_risk', 'past_delays']]
    except KeyError as e:
        print("KeyError! Available columns:", df.columns.tolist())
        raise e

    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features)

    risk_features = features_scaled.copy()
    risk_features[:, 0] = 1 - risk_features[:, 0]

    risk_scores = risk_features.mean(axis=1)
    df['risk_score'] = risk_scores
    return df[['vendor_id', 'vendor_name', 'risk_score']]

