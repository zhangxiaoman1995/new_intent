from typing import List, Optional, Dict, Any, Union, Literal


def read_email(
    message_id: Optional[str] = None,
    query: Optional[str] = None,
    labels: Optional[List[str]] = None,
    max_results: int = 50,
    include_body: bool = True,
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Read emails from the user's mailbox.

    Use either a specific message_id or search filters to retrieve one or more emails.

    Args:
        message_id (str, optional):
            Unique ID of the email to read. If provided, other filters are ignored.

        query (str, optional):
            Free-text search using standard email operators (e.g., `from:`, `subject:`,
            `before:`, `after:`, `label:`). Ignored if message_id is provided.

        labels (list[str], optional):
            Filter by labels/folders (e.g., ["INBOX", "STARRED"]).

        max_results (int, optional):
            Maximum number of emails to return. Default: 50.

        include_body (bool, optional):
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


def send_email(
    to: List[str],
    subject: str,
    body_text: Optional[str] = None,
    body_html: Optional[str] = None,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    in_reply_to: Optional[str] = None,
    thread_id: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None,
    priority: Literal["normal", "high", "low"] = "normal",
    schedule_time: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Send an email from the user's mailbox.

    Creates (and sends) a new message, optionally replying in an existing thread and/or attaching files.

    Args:
        to (list[str]):
            Primary recipients.

        subject (str):
            Email subject line.

        body_text (str, optional):
            Plain-text body. Provide at least one of body_text or body_html.

        body_html (str, optional):
            HTML body. Provide at least one of body_text or body_html.

        cc (list[str], optional):
            Carbon-copy recipients.

        bcc (list[str], optional):
            Blind-carbon-copy recipients.

        attachments (list[object], optional):
            Attachments to include. Each item is either:
              {filename, mime_type, content_base64} or {file_id}.

        in_reply_to (str, optional):
            Message ID this email replies to.

        thread_id (str, optional):
            Existing thread ID to continue (if known).

        headers (object, optional):
            Additional RFC-822 headers (key/value).

        priority ({"normal","high","low"}, optional):
            Message priority. Default: "normal".

        schedule_time (str, optional):
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


def write_email(
    draft_id: Optional[str] = None,
    to: Optional[List[str]] = None,
    subject: Optional[str] = None,
    body_text: Optional[str] = None,
    body_html: Optional[str] = None,
    cc: Optional[List[str]] = None,
    bcc: Optional[List[str]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    in_reply_to: Optional[str] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """
    Create or update an email draft without sending.

    Use this to compose a message and save it as a draft. You can later modify or send the draft.

    Args:
        draft_id (str, optional):
            Existing draft ID to update. If omitted, a new draft is created.

        to (list[str], optional):
            Primary recipients.

        subject (str, optional):
            Email subject line.

        body_text (str, optional):
            Plain-text body.

        body_html (str, optional):
            HTML body.

        cc (list[str], optional):
            Carbon-copy recipients.

        bcc (list[str], optional):
            Blind-carbon-copy recipients.

        attachments (list[object], optional):
            Attachments for the draft. Each item is either:
              {filename, mime_type, content_base64} or {file_id}.

        in_reply_to (str, optional):
            Message ID this draft would reply to.

        headers (object, optional):
            Additional RFC-822 headers (key/value).

    Returns:
        object: Information about the saved draft:
            - draft_id (str)
            - message_id (str)
            - thread_id (str)
            - updated_at (ISO 8601 str)
    """
    pass


def PayRepayment(
    entityName: str,
    entityId: str,
    entityGroupId: Optional[str] = None,
    displayName: str = "",
    description: str = "",
    logoURL: str = "",
    keywords: Optional[List[str]] = None,
    rankingHint: Optional[float] = None,
    expirationTime: Optional[float] = None,
    metadataModificationTime: Optional[float] = None,
    activityType: Optional[List[str]] = None,
    isPublicData: Optional[bool] = None,
    extras: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Trigger a repayment payment and write (or update) related metadata.

    Use this to initiate the repayment flow while submitting searchable/display metadata and admin fields.

    Args:
        entityName (str):
            Name of the entity (e.g., entity type "Repayment").

        entityId (str):
            Unique identifier of the record. Max length: 64 characters.

        entityGroupId (str, optional):
            Grouping identifier (for admin use such as future bulk deletion). Custom-defined
            format. Max length: 64 characters.

        displayName (str):
            Display name. Max length: 50 characters.

        description (str):
            User-facing description shown in the UI. Max length: 2000 characters.

        logoURL (str):
            Thumbnail URL. Text length ≤ 512 characters; recommended size 48×48; file size ≤ 20 KB.

        keywords (list[str], optional):
            Search keywords. Array total length recommended ≤ 1000 characters.

        rankingHint (float, optional):
            Sorting weight for ranking. Floating-point number from 0 to 100.

        expirationTime (float, optional):
            Data expiration time (e.g., copyright expiry). Numeric timestamp (seconds or
            milliseconds—integration-defined). Max 20 characters if stored as string.

        metadataModificationTime (float, optional):
            Last metadata update time (for ordering). Numeric timestamp (seconds or milliseconds—integration-defined).

        activityType (list[str], optional):
            Activity/behavior types (optional/NA).

        isPublicData (bool, optional):
            Whether this is public-domain data (i.e., not user-specific).

        extras (object, optional):
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
