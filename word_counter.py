import re
import streamlit as st

st.title("Word & Bracketed Word Counter")

# Text input box
text = st.text_area("Paste your text here:", height=250)

def count_words(text):
    # Count all words
    all_words = re.findall(r"\b\w+\b", text)
    total_word_count = len(all_words)

    # Find all [[...]] segments
    bracketed_segments = re.findall(r"\[\[(.*?)\]\]", text)

    # Count words inside brackets
    bracketed_words = []
    for segment in bracketed_segments:
        bracketed_words.extend(re.findall(r"\b\w+\b", segment))
    bracketed_word_count = len(bracketed_words)

    return total_word_count, bracketed_word_count

if st.button("Count words"):
    total, bracketed = count_words(text)
    st.write(f"**Total words:** {total}")
    st.write(f"**Bracketed words:** {bracketed}")