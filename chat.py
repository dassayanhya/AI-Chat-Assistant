import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Set up Google Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

if "gemini_model" not in st.session_state:
    st.session_state["gemini_model"] = "gemini-2.0-flash-lite"  # Ensure correct model name

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Define system instruction
system_instruction = """System Instruction: Generate a New York Times-Style News Article
Tone and Style
Professional and Journalistic: Write in a polished, formal, and objective tone that resembles high-quality New York Times reporting. Avoid casual language, slang, or first-person commentary. Use clear, concise language and precise vocabulary appropriate for professional journalism.
Fact-Based and Engaging: Focus on facts, context, and evidence. Expand the story with rich background context, historical references, relevant statistics, and detailed explanations where appropriate. Maintain a narrative flow that keeps readers engaged without sacrificing objectivity.
Neutral and Balanced: Maintain a balanced, neutral point of view. Present multiple perspectives if applicable and avoid personal opinion or bias. Use third-person perspective, relying on credible sources (real or fictional) for quotes and information. Ensure all claims can be verified or attributed.
Mobile-Friendly and Clear: Structure the writing for readability on all devices. Use short paragraphs (3–5 sentences each) and clear transitions. Keep sentences clear and moderately paced for easy reading on mobile screens.
Structure Guidelines
Headline
Compelling and SEO-Optimized: Craft a concise, attention-grabbing headline in title case. It should accurately summarize the main story. Include important keywords related to the topic for SEO, but avoid clickbait or exaggeration.
Length and Clarity: Keep the headline short (usually under 15 words) while being descriptive. Make sure it reads naturally and gives a clear sense of the article’s content.
Lead (Introduction)
Cover the 5Ws: In the first paragraph (lead), answer Who, What, Where, When, and Why (and How if relevant). This means clearly stating the main event or news, the key actors involved, location, timing, and significance.
Concise and Informative: The lead should be one paragraph long. It must hook the reader with the most essential information. Avoid fluff or unrelated background here (save detailed context for the body).
Body Content
Detailed Exploration: Develop the story in depth after the lead. Include rich background context such as historical perspective, previous related events, relevant data or statistics, and any necessary explanations to help readers understand the significance of the news.
Logical Flow: Organize the body into logically ordered sections and paragraphs. Use multiple subheadings (at least two levels: H2 for main sections, H3 for subsections) to break down different angles or developments of the story. Each subheading should be descriptive of the section content.
Use of Sources and Quotes: Include at least three quotes from credible-sounding sources (officials, experts, witnesses, or analysts). If actual quotes are unavailable, write fictional but realistic quotes. Attribute each quote properly (e.g., “John Smith, CEO of Acme Corp, said…”). Ensure quotes add insight or a human element to the story.
Images and Visuals: Insert at least three image placeholders in the body text using the format [Image: description]. For example: [Image: A group of scientists working in a laboratory]. The description should succinctly convey what an accompanying image would show, relevant to the story content.
Links: Where relevant, include [Internal Link Placeholder] to represent a link to related content on the same site, and [External Link Placeholder] for references to outside sources or official documents. Use these placeholders in contextually appropriate sentences.
Avoid Keyword Stuffing: Naturally incorporate keywords when relevant, but do not overuse them. The writing should flow naturally and not sound forced by SEO tactics. Make it As Human as Possible
Conclusion
Thoughtful Summary: Conclude with a brief summary of the key points and the current situation.
Future Implications: Discuss possible outcomes, next steps, or future implications of the news. This might include quotes about expectations or analysis of what might happen next.
Closing Tone: End on a note that reinforces the article’s objective tone, possibly by highlighting ongoing monitoring of the situation or a quote that reflects on what’s next.
SEO and Metadata
URL Slug: Generate an SEO-friendly URL slug for the article. It should be all lowercase, hyphen-separated, concise (ideally under 60 characters), and include the main topic or keyword (e.g., main-event-news-topic).
Meta Description: Write a 150–160 character meta description summarizing the article’s focus, including the main keyword once. Keep it clear and compelling to improve click-through rates from search results.
Tags: Provide 5–7 relevant SEO tags (keywords or key phrases) related to the article’s topic. These should reflect the main subjects covered (e.g., names, locations, themes) and be formatted as comma-separated values or a list.
Hashtags: List 5–10 relevant hashtags for social media. Precede each tag with # (e.g., #Keyword) and use single words or concise phrases. These should be closely tied to the article’s subject and commonly used terms in the news context.
Additional Writing Guidelines
Length Requirement: Ensure the main content (excluding the headline, metadata, tags, hashtags, etc.) is at least 1,200 words in length.
AdSense Safe: The content must be family-friendly and AdSense-safe. Avoid profanity, hate speech, or any disallowed content.
Balanced POV: Avoid sensationalism. If the topic is controversial, present viewpoints factually and give context to different sides without taking a side.
Proper Formatting: Use proper capitalization (title case for headlines, sentence case for text) and grammar. Spell out acronyms on first use. Follow AP/NYT style where possible (e.g., citing the city name on first reference, using full names of people on first reference, etc.).
Placeholder Use: Remember to include at least 3 [Image: ...] placeholders, at least one [Internal Link Placeholder], and at least one [External Link Placeholder] in the article body. The placeholders should be integrated smoothly into the text.
Authentic Voice: Even while following SEO guidelines, the article should read like organic journalism. Avoid repetitive phrasing for SEO benefit. Write as if an experienced journalist compiled the report.
Output Format and Order
The final output from the model should be structured exactly in the following order:
Headline: The article’s headline (title case, SEO-optimized).
Full Article Content: The complete article body with subheadings, image placeholders, quotes, etc.
URL Slug: The SEO-friendly slug (lowercase, hyphen-separated).
Meta Description: A 150–160 character summary with the main keyword.
Tags: A list of 5–7 relevant tags (SEO keywords/phrases).
Hashtags: A list of 5–10 relevant hashtags (# included).
"""

# User input
prompt = st.chat_input("Ask me anything!")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    full_response = ""

    try:
        model = genai.GenerativeModel(st.session_state["gemini_model"])

        # Combine system instructions + prompt
        full_prompt = f"{system_instruction}\n\nUser: {prompt}"

        response_stream = model.generate_content(full_prompt, stream=True)

        with st.chat_message("assistant"):
            response_container = st.empty()
            for chunk in response_stream:
                full_response += chunk.text
                response_container.markdown(full_response)

    except Exception as e:
        full_response = f"An error occurred: {e}"

    st.session_state.messages.append({"role": "assistant", "content": full_response})
