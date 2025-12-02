# credibility.py
from agents.agent1 import agent1
from agents.agent2 import agent2
from agents.agent3 import agent3
from agents.agent4 import agent4
from agents.agent5 import agent5

def calculate_stock_credibility(agent1_score,agent2_score,agent3_score,agent4_score,agent5_score):
    """
    Calculate the Stock Credibility Score based on the outputs of the five agents.

    Parameters:
    financial_score (float): Score from the financial agent.
    technical_score (float): Score from the technical agent.
    fundamental_score (float): Score from the fundamental agent.
    sentimental_score (float): Score from the sentimental agent.
    industry_trend_score (float): Score from the industry trend analyzer agent.

    Returns:
    float: The total Stock Credibility Score.
    """
    # Define weightage for each agent
    financial_weight = 0.25
    technical_weight = 0.25
    fundamental_weight = 0.20
    sentimental_weight = 0.20
    industry_trend_weight = 0.10

    # Calculate the weighted sum
    total_score = (
        (agent1_score * financial_weight) +
        (agent2_score * technical_weight) +
        (agent3_score * fundamental_weight) +
        (agent4_score * sentimental_weight) +
        (agent5_score * industry_trend_weight)
    )

    return total_score
