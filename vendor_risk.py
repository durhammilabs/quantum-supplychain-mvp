import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def compute_risk_scores(df):
    # Normalize features between 0 and 1
    scaler = MinMaxScaler()
    features = df[['on_time_pct', 'claim_rate', 'geopolitical_risk', 'past_delays']]
    features_scaled = scaler.fit_transform(features)

    # Higher claim_rate, geopolitical risk, and past delays increase risk
    # on_time_pct inversely affects risk
    risk_features = features_scaled.copy()
    risk_features[:, 0] = 1 - risk_features[:, 0]  # invert on_time_pct

    # Average these factors for a risk score between 0 and 1
    risk_scores = risk_features.mean(axis=1)
    df['risk_score'] = risk_scores
    return df[['vendor_id', 'vendor_name', 'risk_score']]
