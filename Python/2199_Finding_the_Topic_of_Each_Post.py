# Author: Kaustav Ghosh
# Problem: Finding the Topic of Each Post
# Approach: For each post, tokenize its content into a lowercased set of whole words. A topic matches when one of its keywords appears as a whole word. Collect the distinct matching topic ids, sort them ascending and join with commas; if none match, output "Ambiguous!"

import pandas as pd


def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:
    # Map each lowercased keyword to the set of topic ids it belongs to
    kw = keywords.copy()
    kw["word_lower"] = kw["word"].str.lower()

    def topics_for(content):
        words = set(content.lower().split())
        matched = kw.loc[kw["word_lower"].isin(words), "topic_id"]
        ids = sorted(set(matched.tolist()))
        if not ids:
            return "Ambiguous!"
        return ",".join(str(i) for i in ids)

    result = posts.copy()
    result["topic"] = result["content"].apply(topics_for)
    return result[["post_id", "topic"]]
