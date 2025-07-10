import replicate
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm_response(prompt):
    try:
        # load env variables
        load_dotenv()

        # configure Replicate with API token
        api_token = os.getenv("REPLICATE_API_TOKEN")
        if not api_token:
            raise ValueError("Missing REPLICATE_API_TOKEN in .env")
        os.environ["REPLICATE_API_TOEKN"] = api_token

        # Get reponse from Claude
        # currently claude 2 change to 4
        output = replicate.run(
            "anthropic/claude-2:1d618d036dcb0c5a9a8f9a2e0c1d3b9a8a9b0e0c1d3b9a8a9b0e0c1d3b9a8a9",
            input= {
                "prompt": prompt,
                "max_tokens": 1000
            }
        )
        return "".join(output)

    except ValueError as e:
        print(f"Configuration Error: {e}")
        return "Server configuration error - please contact administrator"
    except Exception as e:
        print(f"API Error: {e}")
        return "There was an error processing your request."


