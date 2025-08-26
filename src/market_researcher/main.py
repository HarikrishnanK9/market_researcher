import sys
import warnings
from market_researcher.crew import MarketResearcher
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
                'topic': 'Electric Vehicles',
                'input_text': """
                            According to recent industry data, the global electric vehicle (EV) market saw a 35% year-over-year growth in 2024, driven largely by surging demand in Asia and Europe.
                            China accounted for over 60% of global EV sales, while European countries saw a 20% increase due to new government subsidies and stricter emission policies.
                            Major automakers are accelerating their EV lineup, with Ford, GM, and Volkswagen announcing over $50 billion in combined investment for battery innovation by 2026.
                            Additionally, consumers are increasingly prioritising range efficiency and fast-charging capabilities when selecting EV models.
                """
                }
        
    try:
        MarketResearcher().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     {
#         'topic': 'Electric Vehicles',
#         'input_text': """
#                     According to recent industry data, the global electric vehicle (EV) market saw a 35% year-over-year growth in 2024, driven largely by surging demand in Asia and Europe.
#                     China accounted for over 60% of global EV sales, while European countries saw a 20% increase due to new government subsidies and stricter emission policies.
#                     Major automakers are accelerating their EV lineup, with Ford, GM, and Volkswagen announcing over $50 billion in combined investment for battery innovation by 2026.
#                     Additionally, consumers are increasingly prioritising range efficiency and fast-charging capabilities when selecting EV models.
#         """
#         }


    try:
        MarketResearcher().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
