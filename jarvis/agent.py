
from google.adk.agents import Agent
from google.adk.agents import ParallelAgent

# -----------------------------
# Sub-agent 1: Destination expert
# -----------------------------
destination_agent = Agent(
    name="destination_agent",
    model="gemini-2.5-flash",
    description="Recommends travel destinations based on user preferences.",
    instruction="""
    You are a travel destination expert.
    Recommend 3 suitable destinations based on the user's interests,
    travel dates, and preferences.
    Explain briefly why each destination is a good choice.
    """
)

# -----------------------------
# Sub-agent 2: Itinerary planner
# -----------------------------
itinerary_agent = Agent(
    name="itinerary_agent",
    model="gemini-2.5-flash",
    description="Creates a day-by-day travel itinerary.",
    instruction="""
    You are a travel itinerary planner.
    Create a practical day-by-day itinerary based on the user's
    destination and travel preferences.
    Include activities, sightseeing, and relaxation time.
    """
)

# -----------------------------
# Sub-agent 3: Budget planner
# -----------------------------
budget_agent = Agent(
    name="budget_agent",
    model="gemini-2.5-flash",
    description="Estimates travel expenses and creates a budget.",
    instruction="""
    You are a travel budget expert.
    Estimate expenses for accommodation, food, transportation,
    and activities based on the user's destination and trip duration.
    Clearly label estimates and state your assumptions.
    """
)

# -----------------------------
# Run all three agents in parallel
# -----------------------------
travel_team = ParallelAgent(
    name="travel_team",
    sub_agents=[
        destination_agent,
        itinerary_agent,
        budget_agent
    ]
)

# -----------------------------
# Root agent: Coordinator
# -----------------------------
root_agent = Agent(
    name="travel_coordinator",
    model="gemini-2.5-flash",
    description="Coordinates destination, itinerary, and budget agents.",
    instruction="""
    You are the main travel planning assistant.

    Delegate travel planning tasks to the travel_team.
    After the sub-agents finish, combine their results into
    one clear and organized travel plan.

    Include:
    1. Recommended destinations
    2. Day-by-day itinerary
    3. Estimated travel budget

    If important information is missing, ask the user
    for clarification before creating the plan.
    """,
    sub_agents=[travel_team]
)
