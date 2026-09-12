from pydantic import BaseModel, Field
from typing import Optional, Literal

class QueryIntent(BaseModel):
    """The master query intent combining the target table and its specific filters."""
    target_table: Literal["files", "antivirus", "users", "tasks", "yara_rules", "unknown"] = Field(
        default="unknown", 
        description="The target table to query based on the user's intent. If unrelated or greeting, use 'unknown'."
    )
    
    query_type: Literal["list", "count"] = Field(
        default="list",
        description="Whether the user wants a list of records ('list') or just the total count of records ('count')"
    )

    # ── File filters ──
    extension: Optional[Literal[".exe", ".dll", ".msi", ".com", ".vsixpackage", ".docx", ".png", ".bat", ".jpg", ".rar", ".deb", ".pdf", ".flatpak", ".csv", ".zip", ".text"]] = Field(default=None, description="File extension filter, e.g. '.exe', '.dll', '.pdf'. Only for target_table='files'.")
    yara_scan_status: Optional[Literal["not_scanned", "match", "clean"]] = Field(default=None, description="Yara scan status filter. Only for target_table='files'.")
    file_status: Optional[int] = Field(default=None, description="File processing status code (2, 3, or 4). Only for target_table='files'.")
    file_name_search: Optional[str] = Field(default=None, description="Search for a specific file name using partial pattern matching. Only for target_table='files'.")

    # ── Antivirus filters ──
    is_enable: Optional[bool] = Field(default=None, description="Whether the antivirus is enabled. Only for target_table='antivirus'.")
    require_update: Optional[bool] = Field(default=None, description="Whether the antivirus requires an update. Only for target_table='antivirus'.")
    is_busy: Optional[bool] = Field(default=None, description="Whether the antivirus is busy scanning. Only for target_table='antivirus'.")

    # ── User filters ──
    is_active: Optional[bool] = Field(default=None, description="Whether the user is active. Only for target_table='users'.")
    is_online: Optional[bool] = Field(default=None, description="Whether the user is currently online. Only for target_table='users'.")
    must_change_password: Optional[bool] = Field(default=None, description="Whether the user must change password. Only for target_table='users'.")
    user_name_search: Optional[str] = Field(default=None, description="Search for a specific user name using partial pattern matching. Only for target_table='users'.")

    # ── Task filters ──
    task_status: Optional[int] = Field(default=None, description="Task status code. Only for target_table='tasks'.")
    scan_result: Optional[str] = Field(default=None, description="Result of the scan. Only for target_table='tasks'.")

    # ── Yara rule filters ──
    yara_enabled: Optional[bool] = Field(default=None, description="Whether the yara rule is enabled. Only for target_table='yara_rules'.")
    yara_source: Optional[str] = Field(default=None, description="Source of the yara rule. Only for target_table='yara_rules'.")

    # ── Common fields ──
    timeframe_days: Optional[int] = Field(default=None, description="Number of days to look back. Leave null unless the user explicitly specifies a time period.")
    sort_direction: Literal["asc", "desc"] = Field(default="desc")
    limit: int = Field(default=10, description="Number of results to return, default 10")
