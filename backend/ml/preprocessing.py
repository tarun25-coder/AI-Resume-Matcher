import re


def clean_text(text: str) -> str:
    """
    Clean and normalize text for NLP processing.
    """

    if not text:
        return ""

    text = text.lower()

    text = re.sub(r"[/|,;:(){}\[\]]", " ", text)

    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()