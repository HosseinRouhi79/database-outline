from .schema import QueryIntent

def build_prompt(user_text: str) -> str:
    return f"""You are an AI assistant that extracts user intent for an antivirus management platform.
Your task is to map the user's natural language request to the structured QueryIntent JSON.

# Instructions
- Understand Persian (Farsi) input perfectly.
- Output strictly in the defined JSON format.
- If any text values are generated (like scan_result or yara_source), they MUST be in Persian (Farsi).

# Field Mapping Hints
- If the user specifies an extension (like .exe, .pdf, .dll), YOU MUST set the `extension` field.
- For files, set target_table='files'. For tasks, set 'tasks'. For users, set 'users'. For yara, set 'yara_rules'. For antivirus, set 'antivirus'.
- Set ONLY the filters belonging to the selected target_table. Leave all other filters as null.
- Set `timeframe_days` ONLY if a time period is explicitly mentioned (e.g. "ماه گذشته", "last 7 days"). Otherwise leave it null.
- Set `query_type` to "count" if asked for a total/number, otherwise "list".

# User Request
{user_text}
"""
