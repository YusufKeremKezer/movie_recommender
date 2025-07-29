from config import settings
from typing import Dict, Any

async def should_extend_summary(state: Dict[str, Any]):
    
    if len(state["messages"]) > settings.TOTAL_MESSAGES_SUMMARY_TRIGGER:
        return "extend_summary"
    else:
        return "summary"

