from typing import List, Optional, Dict, Any, Union, Literal


def READ_EMAIL(
    MESSAGE_ID: Optional[str] = None,
    QUERY: Optional[str] = None,
    LABELS: Optional[List[str]] = None,
    MAX_RESULTS: int = 50,
    INCLUDE_BODY: bool = True,
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Read emails from the user's mailbox.

    Use either a specific MESSAGE_ID or search filters to retrieve one or more emails.

    Args:
        MESSAGE_ID (str, optional):
            Unique ID of the email to read. If provided, other filters are ignored.

        QUERY (str, optional):
            Free-text search using standard email operators (e.g., from:, subject:, before:, after:, label:).
            Ignored if MESSAGE_ID is provided.

        LABELS (list[str], optional):
            Filter by labels/folders (e.g., ["INBOX", "STARRED"]).

        MAX_RESULTS (int, optional):
            Maximum number of emails to return. Default: 50.

        INCLUDE_BODY (bool, optional):
            Whether to include the full HTML/text body for each email. Default: True.

    Returns:
        list | object:
            A list of emails or a single email. Each email may include:
            - message_id (str)
            - thread_id (str)
            - subject (str)
            - from (str)
            - to (list[str])
            - cc (list[str])
            - bcc (list[str])
            - date (ISO 8601 str)
            - snippet (str)
            - body_html (str)
            - body_text (str)
            - labels (list[str])
            - attachments (list of {filename, mime_type, size_bytes, attachment_id})
    """
    pass

def SEND_EMAIL(
    TO: List[str],
    SUBJECT: str,
    BODY_TEXT: Optional[str] = None,
    BODY_HTML: Optional[str] = None,
    CC: Optional[List[str]] = None,
    BCC: Optional[List[str]] = None,
    ATTACHMENTS: Optional[List[Dict[str, Any]]] = None,
    IN_REPLY_TO: Optional[str] = None,
    THREAD_ID: Optional[str] = None,
    HEADERS: Optional[Dict[str, str]] = None,
    PRIORITY: Literal["normal", "high", "low"] = "normal",
    SCHEDULE_TIME: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Send an email from the user's mailbox.

    Creates (and sends) a new message, optionally replying in an existing thread and/or attaching files.

    Args:
        TO (list[str]):
            Primary recipients.

        SUBJECT (str):
            Email subject line.

        BODY_TEXT (str, optional):
            Plain-text body. Provide at least one of BODY_TEXT or BODY_HTML.

        BODY_HTML (str, optional):
            HTML body. Provide at least one of BODY_TEXT or BODY_HTML.

        CC (list[str], optional):
            Carbon-copy recipients.

        BCC (list[str], optional):
            Blind-carbon-copy recipients.

        ATTACHMENTS (list[object], optional):
            Attachments to include. Each item: {filename, mime_type, content_base64} or {file_id}.

        IN_REPLY_TO (str, optional):
            Message ID this email replies to.

        THREAD_ID (str, optional):
            Existing thread ID to continue (if known).

        HEADERS (object, optional):
            Additional RFC-822 headers (key/value).

        PRIORITY ({"normal","high","low"}, optional):
            Message priority. Default: "normal".

        SCHEDULE_TIME (str, optional):
            Optional future send time in ISO 8601 (UTC). If omitted, send immediately.

    Returns:
        object: Information about the sent (or scheduled) message:
            - status: "sent" | "scheduled"
            - message_id (str)
            - thread_id (str)
            - scheduled_time (ISO 8601 str, present if scheduled)
            - date (ISO 8601 str, present if sent immediately)
    """
    pass


def WRITE_EMAIL(
    DRAFT_ID: Optional[str] = None,
    TO: Optional[List[str]] = None,
    SUBJECT: Optional[str] = None,
    BODY_TEXT: Optional[str] = None,
    BODY_HTML: Optional[str] = None,
    CC: Optional[List[str]] = None,
    BCC: Optional[List[str]] = None,
    ATTACHMENTS: Optional[List[Dict[str, Any]]] = None,
    IN_REPLY_TO: Optional[str] = None,
    HEADERS: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create or update an email draft without sending.

    Use this to compose a message and save it as a draft. You can later modify or send the draft.

    Args:
        DRAFT_ID (str, optional):
            Existing draft ID to update. If omitted, a new draft is created.

        TO (list[str], optional):
            Primary recipients.

        SUBJECT (str, optional):
            Email subject line.

        BODY_TEXT (str, optional):
            Plain-text body.

        BODY_HTML (str, optional):
            HTML body.

        CC (list[str], optional):
            Carbon-copy recipients.

        BCC (list[str], optional):
            Blind-carbon-copy recipients.

        ATTACHMENTS (list[object], optional):
            Attachments for the draft. Each item: {filename, mime_type, content_base64} or {file_id}.

        IN_REPLY_TO (str, optional):
            Message ID this draft would reply to.

        HEADERS (object, optional):
            Additional RFC-822 headers (key/value).

    Returns:
        object: Information about the saved draft:
            - draft_id (str)
            - message_id (str)
            - thread_id (str)
            - updated_at (ISO 8601 str)
    """
    pass


def PAY_REPAYMENT(
    ENTITY_NAME: str,
    ENTITY_ID: str,
    ENTITY_GROUP_ID: Optional[str] = None,
    DISPLAY_NAME: str = "",
    DESCRIPTION: str = "",
    LOGO_URL: str = "",
    KEYWORDS: Optional[List[str]] = None,
    RANKING_HINT: Optional[float] = None,
    EXPIRATION_TIME: Optional[float] = None,
    METADATA_MODIFICATION_TIME: Optional[float] = None,
    ACTIVITY_TYPE: Optional[List[str]] = None,
    IS_PUBLIC_DATA: Optional[bool] = None,
    EXTRAS: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Trigger a repayment payment and write (or update) related metadata.

    Use this to initiate the repayment flow while submitting searchable/display metadata and admin fields.

    Args:
        ENTITY_NAME (str):
            Name of the entity (e.g., entity type "Repayment").

        ENTITY_ID (str):
            Unique identifier of the record. Max length: 64 characters.

        ENTITY_GROUP_ID (str, optional):
            Grouping identifier (for admin use such as future bulk deletion). Custom-defined format.
            Max length: 64 characters.

        DISPLAY_NAME (str):
            Display name. Max length: 50 characters.

        DESCRIPTION (str):
            User-facing description shown in the UI. Max length: 2000 characters.

        LOGO_URL (str):
            Thumbnail URL. Text length ≤ 512 characters; recommended size 48×48; file size ≤ 20 KB.

        KEYWORDS (list[str], optional):
            Search keywords. Array total length recommended ≤ 1000 characters.

        RANKING_HINT (float, optional):
            Sorting weight for ranking. Floating-point number from 0 to 100.

        EXPIRATION_TIME (float, optional):
            Data expiration time. Numeric timestamp (seconds or milliseconds—integration-defined).

        METADATA_MODIFICATION_TIME (float, optional):
            Last metadata update time (for ordering). Numeric timestamp (seconds or milliseconds—integration-defined).

        ACTIVITY_TYPE (list[str], optional):
            Activity/behavior types (optional/NA).

        IS_PUBLIC_DATA (bool, optional):
            Whether this is public-domain data (i.e., not user-specific).

        EXTRAS (object, optional):
            Additional extension fields; structure defined by the integrating business.

    Returns:
        object: Execution result and a snapshot of saved metadata:
            - status: "success" | "pending" | "failed"
            - paymentId (str): Payment transaction ID
            - entityId (str): Echoed unique entity ID
            - processedAt (ISO 8601 str): Processing time
            - message (str): Human-readable status message
            - snapshot (object): Saved key fields snapshot
    """
    pass
