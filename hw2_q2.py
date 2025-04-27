
Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: Tuple[Agent, ...]) -> List[Agent]:
    """Model the outcome of the meetings of pairs of agents."""

    from enum import Enum
    from collections import namedtuple
    from itertools import filterfalse, zip_longest
    from typing import Tuple, List

    # Filter out healthy and dead
    active_agents = list(filterfalse(lambda ag: ag.category in {Condition.HEALTHY, Condition.DEAD}, agent_listing))
    
    # Pair up using zip_longest to handle odd count
    pairs = zip_longest(*([iter(active_agents)] * 2), fillvalue=None)
    
    # Resolve each pair
    updated_active = []
    for a, b in pairs:
        updated_active.extend(resolve_pair(a, b))
    
    # Combine updated active with untouched healthy and dead
    untouched = [ag for ag in agent_listing if ag.category in {Condition.HEALTHY, Condition.DEAD}]
    
    return updated_active + untouched

def resolve_pair(a: Agent, b: Agent) -> List[Agent]:
    # Helper functions for category transitions
    upgrade = {Condition.SICK: Condition.HEALTHY, Condition.DYING: Condition.SICK}
    degrade = {Condition.SICK: Condition.DYING, Condition.DYING: Condition.DEAD}
    # If one agent is None (odd leftover), return the other unchanged
    if a is None:
        return [b]
    if b is None:
        return [a]
    
    cat_a, cat_b = a.category, b.category
    
    # Cure interactions
    if cat_a == Condition.CURE and cat_b != Condition.CURE:
        return [a, Agent(b.name, upgrade.get(cat_b, cat_b))]
    if cat_b == Condition.CURE and cat_a != Condition.CURE:
        return [Agent(a.name, upgrade.get(cat_a, cat_a)), b]
    # Both cures or no cure involved: degrade both if non-cure
    if cat_a != Condition.CURE and cat_b != Condition.CURE:
        return [
            Agent(a.name, degrade.get(cat_a, cat_a)),
            Agent(b.name, degrade.get(cat_b, cat_b))
        ]
    # Both are cures or unaffected
    return [a, b]