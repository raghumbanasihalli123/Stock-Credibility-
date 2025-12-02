import streamlit as st
import plotly.graph_objects as go
from agents.agent1 import agent1
from agents.agent2 import agent2
from agents.agent3 import agent3
from agents.agent4 import agent4  # Commented since it's not being used
from agents.agent5 import agent5
from credibility import calculate_stock_credibility  # Import the credibility calculation function

# Normalization function to ensure scores are between 1-100
def normalize(score, min_val=0, max_val=100):
    return max(min(int(score), max_val), min_val)

# Streamlit App
st.title("Explainable AI Driven-Stock Credibility Score Prediction")

# Input from user
ticker = st.text_input("Enter Stock Ticker Symbol")

if ticker:
    # Initialize progress bars for each agent
    progress_agent1 = st.progress(0)
    progress_agent2 = st.progress(0)
    progress_agent3 = st.progress(0)
    progress_agent4 = st.progress(0)  # Commented since it's not being used
    progress_agent5 = st.progress(0)

    # Call agents to calculate their scores and update progress
    # Agent 1 (Financial score)
    agent1_score = normalize(agent1(ticker))
    st.write(f"Agent 1 (Financial): {agent1_score}/100")
    progress_agent1.progress(agent1_score)  # Update progress for Agent 1

    # Agent 2 (Technical score)
    agent2_score = normalize(agent2(ticker))
    st.write(f"Agent 2 (Technical): {agent2_score}/100")
    progress_agent2.progress(agent2_score)  # Update progress for Agent 2

    # Agent 3 (Fundamental score)
    agent3_score = normalize(agent3(ticker))
    st.write(f"Agent 3 (Fundamental): {agent3_score}/100")
    progress_agent3.progress(agent3_score)  # Update progress for Agent 3

    # Agent 4 (Sentimental score)
    agent4_score = normalize(agent4(ticker))
    st.write(f"Agent 4 (Sentimental): {agent4_score}/100")
    progress_agent4.progress(agent4_score)  # Update progress for Agent 4

    # Agent 5 (Industry trend score)
    agent5_score = normalize(agent5(ticker))
    st.write(f"Agent 5 (Industry Trend): {agent5_score}/100")
    progress_agent5.progress(agent5_score)  # Update progress for Agent 5

    # Calculate final credibility score using weighted scores
    total_credibility_score = calculate_stock_credibility(
        agent1_score, agent2_score, agent3_score, agent4_score, agent5_score
    )
    total_credibility_score = normalize(total_credibility_score)

    # Visualization of final score using a big Speedometer
    st.subheader("Final Stock Credibility Score (Weighted)")

    # Create a Speedometer (Gauge chart)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_credibility_score,
        title={"text": "Credibility Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 33], "color": "green"},
                {"range": [33, 66], "color": "yellow"},
                {"range": [66, 100], "color": "red"}
            ],
            "bar": {"color": "darkblue"}  # Indicator needle color
        }
    ))
    st.plotly_chart(fig)

    # Display final score in text
    st.write(f"**Credibility Score:** {total_credibility_score:.2f}/100")
